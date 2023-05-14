import requests
from  http import HTTPStatus

from homework_19.users_api import UsersApi


def test_get_users_api():
    url = "https://reqres.in/api/users?page=2"
    response = UsersApi(env).get_users()
    response_data = response.json()
    assert response.status_code == HTTPStatus.OK, 'Status code is not as expected'





