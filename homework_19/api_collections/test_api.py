from http import HTTPStatus

from homework_19.api_collections.user_data import UsersData
from homework_19.api_collections.user_data_post_put import UsersDataPostPut
from homework_19.api_collections.users_api import UsersApi
from homework_19.conftest import env


def test_get_users_api(env, user_mock):
    expected_user = user_mock
    response = UsersApi(env).get_user(1)
    response_data = response.json()
    actual_user = UsersData.from_json(**response_data)
    assert response.status_code == HTTPStatus.OK, 'Status code is not as expected'
    assert actual_user == expected_user, 'User data is not as expected'

def test_post_users_api(env, user_post_mock):
    expected_user = user_post_mock
    response = UsersApi(env).post_user(env.post_user)
    response_data = response.json()
    actual_user = UsersDataPostPut.from_json(**response_data)
    assert response.status_code == HTTPStatus.CREATED, 'Status code is not as expected'
    assert actual_user == expected_user, 'User data is not as expected'

def test_put_users_api(env, user_put_mock):
    expected_user = user_put_mock
    response = UsersApi(env).put_user(2, env.put_user)
    response_data = response.json()
    actual_user = UsersDataPostPut.from_json(**response_data)
    assert response.status_code == HTTPStatus.OK, 'Status code is not as expected'
    assert actual_user == expected_user, 'User data is not as expected'
