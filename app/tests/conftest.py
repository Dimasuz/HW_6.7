import time
import json
import pytest
import requests
from typing import Literal
from urllib.parse import urljoin
from views import hash_password
from models import Base, Users, Adv, Session, get_engine, get_session_maker
from errors import ApiError
from config import API_URL

session = requests.Session()

@pytest.fixture(scope='session', autouse=True)
def init_database():
    engine = get_engine()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    engine.dispose()


def create_user(name: str = None, email: str = None, password: str = None):
    name = name or 'user_1'
    email = email or f'user{time.time()}@email.email'
    password = password or '123'
    Session = get_session_maker()
    with Session() as session:
        new_user = Users(email=email, password=hash_password(password))
        session.add(new_user)
        session.commit()
        return {
            "id": new_user.id,
            "email": new_user.email,
            "password": password,}

@pytest.fixture(scope="session")
def first_user():
    return create_user('user1', '123@123.em', '123')

@pytest.fixture()
def second_user():
    return create_user('user2', '321@123.em', '321')


def base_request(http_method: Literal['get', 'post', 'delete', 'patch'],
                 path: 'str', *args, **kwargs) -> dict:
    method = getattr(session, http_method)
    response = method(urljoin(API_URL, path), *args, **kwargs)
    if response.status_code >= 400:
        try:
            message = response.json()
        except json.JSONDecodeError:
            message = response.text
        raise ApiError(response.status_code, message)
    return response.json()
