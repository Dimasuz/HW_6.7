import time
import pytest

from tests.conftest import base_request
from models import Base, Users, Adv, get_engine, get_session_maker
from views import hash_password



@pytest.fixture(scope='session', autouse=True)
def init_database():
    engine = get_engine()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    engine.dispose()


def create_user(email: str = None, password: str = None):
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
    return create_user('123@123.em', '123')


@pytest.fixture()
def second_user():
    return create_user('321@123.em', '321')


def create_adv(title: str = None, descr: str = None, user_id: int = None, password: str = None):
    title = title or 'title_def'
    descr = descr or 'descr_def'
    user_id = user_id or '1'
    password = password or 'password_def'
    Session = get_session_maker()
    with Session() as session:
        new_adv = Adv(title=title, descr = descr, user_id = user_id)
        session.add(new_adv)
        session.commit()
        return {
            "id": new_adv.id,
            "title": new_adv.title,
            "descr": new_adv.descr,
            "user_id": new_adv.user_id,
            "password": password,
        }


def test_post_adv(title = 'test_title', descr = 'test_descr', user_id = 1, password = '123'):
    params = {'title': title, 'descr': descr, 'user_id': user_id, 'password': password}
    adv = base_request('post', 'adv/', json=params)
    adv_in_db = base_request('get', f'users/{adv["id"]}')
    assert adv_in_db['title'] == title


def test_get_adv():
    adv = base_request('get', f'adv/1/')
    assert adv['id'] == 1


def test_patch_adv(adv_id = 1, title = 'alt_title', descr = 'alt_descr', user_id = 1, password = '123'):
    params = {'title': title, 'descr': descr, 'user_id': user_id, 'password': password}
    adv = base_request('patch', f'adv/{adv_id}/', json=params)
    assert adv['titlie'] == title


def test_delete_adv(adv_id = 1, user_id = 1, password = '123'):
    params = {'user_id': user_id, 'password': password}
    result = base_request('delete', f'adv/{adv_id}/', json=params)
    assert result is True
