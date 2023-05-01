from homework_17.utilities.config_reader import get_user_creds, get_search_data


def test_login(open_main_page):
    main_page = open_main_page
    login_page = main_page.click_my_cabinet_button()
    profile_page = login_page.set_email(get_user_creds()[0]).set_password(get_user_creds()[1]).click_login_button()
    assert profile_page.is_profile_panel_displayed(), 'Profile panel element is not displayed'
    actual_text = profile_page.is_password_text_displayed()
    assert actual_text == 'Пароль', 'There is not text'

def test_search(open_main_page):
    main_page = open_main_page
    search_page = main_page.set_search_value(get_search_data()).click_search_button()
    assert search_page.is_search_complete(), 'Search is not complete'
    actual_text = search_page.are_search_results_displayed()
    assert actual_text == f'" За вашим запитом знайдено:', 'There is not text'
