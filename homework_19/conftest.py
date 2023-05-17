import json
import pytest
from homework_19.page_objects.main_page import MainPage
from homework_19.utilities.driver_factory import driver_factory
from homework_19.constants import ROOT_DIR
from homework_19.utilities.configuration import Configuration
from homework_19.api_collections.user_data import UsersData
from homework_19.api_collections.user_data_post_put import UsersDataPostPut

@pytest.fixture()
def user_mock():
    return UsersData({'id': 1, 'email': 'george.bluth@reqres.in', 'first_name': 'George', 'last_name': 'Bluth',
                      'avatar': 'https://reqres.in/img/faces/1-image.jpg'},
                     {'url': 'https://reqres.in/#support-heading',
                      'text': 'To keep ReqRes free, contributions towards server costs are appreciated!'})


@pytest.fixture()
def user_post_mock():
    return UsersDataPostPut("morpheus", "leader")

@pytest.fixture()
def user_put_mock():
    return UsersDataPostPut("morpheus", "manager")

@pytest.fixture(scope='session', autouse=True)
def env():
    with open((f'{ROOT_DIR}/configurations/config.json'), 'r') as file:
        result = file.read()
    config = json.loads(result)
    return Configuration(**config)


@pytest.fixture()
def create_browser(env):
    driver = driver_factory(int(env.browser_id))
    driver.maximize_window()
    driver.get(env.app_url)
    yield driver
    driver.quit()


@pytest.fixture()
def open_main_page(create_browser):
    return MainPage(create_browser)


@pytest.fixture()
def open_login_page(open_main_page):
    main_page = open_main_page
    return main_page.click_my_cabinet_button()


@pytest.fixture()
def open_catalog_page(open_main_page):
    main_page = open_main_page
    return main_page.click_all_board_games_button()


@pytest.fixture()
def open_user_profile_page(open_login_page, env):
    return open_login_page.login(env.email, env.password)
