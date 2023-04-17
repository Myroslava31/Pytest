from homework_17.page_objects.login_page import LoginPage
from homework_17.utilities.config_reader import get_user_creds


def test_login(create_browser):
    driver_chrome = create_browser
    login_page = LoginPage(driver_chrome)
    profile_page = login_page.set_email(get_user_creds()[0]).set_password(get_user_creds()[1]).click_login_button()
    assert profile_page.is_displayed(), 'Profile panel element is not displayed'
