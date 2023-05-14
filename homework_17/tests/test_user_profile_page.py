import pytest

from homework_17.utilities.config_reader import get_user_creds

@pytest.mark.regression
def test_my_orders(open_login_page):
    login_page = open_login_page
    profile_page = login_page.login(get_user_creds()[0], get_user_creds()[1])
    my_orders = profile_page.click_on_orders_button()
    actual_text = my_orders.get_header_text_my_orders()
    assert actual_text == "Мої замовлення", 'Orders are not displayed'

@pytest.mark.regression
def test_my_wishlist(open_login_page):
    login_page = open_login_page
    profile_page = login_page.login(get_user_creds()[0], get_user_creds()[1])
    my_wishlist = profile_page.click_on_wishlist_button()
    actual_text = my_wishlist.get_header_text_wishlist()
    assert actual_text == "Cписок бажань", 'Wishlist is not displayed'

@pytest.mark.regression
def test_waiting_list(open_login_page):
    login_page = open_login_page
    profile_page = login_page.login(get_user_creds()[0], get_user_creds()[1])
    my_orders = profile_page.click_on_waiting_list_button()
    actual_text = my_orders.get_header_text_waiting_list()
    assert actual_text == "Лист очікування", 'Waiting list not displayed'

@pytest.mark.regression
def test_user_info_panels(open_login_page):
    login_page = open_login_page
    profile_page = login_page.login(get_user_creds()[0], get_user_creds()[1])
    elements = len(profile_page.are_user_info_panels_visible())
    assert elements == 2, 'There is not all items'
