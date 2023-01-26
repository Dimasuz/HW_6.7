import time
import pytest

import requests
from urllib.parse import urljoin
from models import Base, Users, Adv, get_engine, get_session_maker
from views import hash_password
from config import API_URL
from typing import Literal
import json

def base_request(http_method: str, path: 'str', *args, **kwargs) -> dict:
    method = getattr(session, http_method)
    response = method(urljoin(API_URL, path), *args, **kwargs)
    if response.status_code >= 400:
        try:
            message = response.json()
        except json.JSONDecodeError:
            message = response.text
        raise ApiError(response.status_code, message)
    return response.json()

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


def test_get_user(first_user):
    # adv = base_request('get', f'user/1/')
    adv = requests.get('http://127.0.0.1:5000/users/1/').json()
    assert adv['id'] == 1

# def test_post_adv(title = 'test_title', descr = 'test_descr', user_id = 1, password = '123'):
#     params = {'title': title, 'descr': descr, 'user_id': user_id, 'password': password}
#     adv = base_request('post', 'adv/', json=params)
#     adv_in_db = base_request('get', f'users/{adv["id"]}')
#     assert adv_in_db['title'] == title


# def test_get_adv():
#     adv = base_request('get', f'adv/1/')
#     assert adv['id'] == 1
#
#
# def test_patch_adv(adv_id = 1, title = 'alt_title', descr = 'alt_descr', user_id = 1, password = '123'):
#     params = {'title': title, 'descr': descr, 'user_id': user_id, 'password': password}
#     adv = base_request('patch', f'adv/{adv_id}/', json=params)
#     assert adv['titlie'] == title
#
#
# def test_delete_adv(adv_id = 1, user_id = 1, password = '123'):
#     params = {'user_id': user_id, 'password': password}
#     result = base_request('delete', f'adv/{adv_id}/', json=params)
#     assert result is True
