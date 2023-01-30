import time
import pytest
from views import hash_password
from models import Base, Users, Adv, get_engine, get_session_maker


@pytest.fixture(scope='session', autouse=True)
def init_database():
    engine = get_engine()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    engine.dispose()


@pytest.fixture()
def create_user():
    name = f'name{time.time()}'
    email = f'email{time.time()}@email.email'
    password = 'password'
    Session = get_session_maker()
    with Session() as session:
        user = Users(name=name, email=email, password=hash_password(password))
        session.add(user)
        session.commit()
        # user = session.query(Users).get(new_user.id)
        return {
            f"id": user.id,
            f"name": user.name,
            f"email": user.email,
            f"password": user.password,}
