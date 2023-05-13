import pytest
from homework_17.page_objects.login_page import LoginPage
from homework_17.page_objects.main_page import MainPage
from homework_17.utilities.driver_factory import driver_factory
from homework_17.utilities.config_reader import get_application_url, get_browser_id, get_user_creds


@pytest.fixture()
def create_browser():
    driver = driver_factory(get_browser_id())
    driver.maximize_window()
    driver.get(get_application_url())
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
def open_user_profile_page(open_login_page):
    return open_login_page.login(get_user_creds()[0], get_user_creds()[1])
