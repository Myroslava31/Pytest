import json
import pytest
from homework_18.page_objects.main_page import MainPage
from homework_18.utilities.driver_factory import driver_factory
from homework_18.constants import ROOT_DIR
from homework_18.utilities.configuration import Configuration


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
