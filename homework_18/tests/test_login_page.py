import pytest


@pytest.mark.smoke
def test_presence_of_login_inputs(open_login_page):
    login_page = open_login_page
    elements = len(login_page.get_list_of_visible_input_fields())
    assert elements == 2, 'There is not all items'

@pytest.mark.smoke
def test_go_to_registration(open_login_page):
    login_page = open_login_page.go_to_registration()
    assert login_page.click_on_registration_button(), "It is not clickable"

@pytest.mark.smoke
def test_presence_of_registration_inputs(open_login_page):
    login_page = open_login_page.go_to_registration()
    elements = len(login_page.get_list_of_visible_input_fields())
    assert elements == 5, 'There is not all items'

@pytest.mark.regression
def test_go_to_refresh_password(open_login_page):
    login_page = open_login_page.go_to_refresh_password()
    assert login_page.click_on_refresh_password_button(), "It is not clickable"

@pytest.mark.regression
def test_presence_of_refresh_password_inputs(open_login_page):
    login_page = open_login_page.go_to_refresh_password()
    elements = len(login_page.get_list_of_visible_input_fields())
    assert elements == 1, 'There is not all items'

@pytest.mark.smoke
def test_login(open_login_page, env):
    login_page = open_login_page
    profile_page = login_page.set_email(env.email).set_password(env.password).click_login_button()
    assert profile_page.is_profile_panel_displayed(), 'Profile panel element is not displayed'
    actual_text = profile_page.get_password_text()
    assert actual_text == 'Пароль', 'There is not text'
