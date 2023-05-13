import pytest

from homework_17.utilities.config_reader import get_user_creds, get_search_data, get_prices

@pytest.mark.smoke
def test_banner_is_present(open_main_page):
    main_page = open_main_page
    assert main_page.is_banner_displayed(), 'There is not banner'

@pytest.mark.smoke
def test_text_on_top_menu(open_main_page):
    main_page = open_main_page
    actual_text = main_page.is_top_menu_text_displayed()
    assert actual_text == "Оплата і доставкаКонтакти м. Київ, вул. Івана Франка, 12 Пн-Пт: 10:00-20:00 | Сб-Нд: 12:00-18:00", 'There is not text'

@pytest.mark.smoke
def test_my_cabinet_present(open_main_page):
    main_page = open_main_page
    assert main_page.is_my_cabinet_button_displayed(), 'There is not button'

@pytest.mark.smoke
def test_presence_of_login_inputs(open_login_page):
    login_page = open_login_page
    elements = len(login_page.are_all_inputs_displayed())
    assert elements == 2, 'There is not all items'

@pytest.mark.smoke
def test_go_to_registration(open_login_page):
    login_page = open_login_page.go_to_registration()
    assert login_page.check_if_registration_is_clickable(), "It is not clickable"

@pytest.mark.smoke
def test_presence_of_registration_inputs(open_login_page):
    login_page = open_login_page.go_to_registration()
    elements = len(login_page.are_all_inputs_displayed())
    assert elements == 5, 'There is not all items'

@pytest.mark.regression
def test_go_to_refresh_password(open_login_page):
    login_page = open_login_page.go_to_refresh_password()
    assert login_page.check_if_refresh_password_is_clickable(), "It is not clickable"

@pytest.mark.regression
def test_presence_of_refresh_password_inputs(open_login_page):
    login_page = open_login_page.go_to_refresh_password()
    elements = len(login_page.are_all_inputs_displayed())
    assert elements == 1, 'There is not all items'

@pytest.mark.smoke
def test_login(open_login_page):
    login_page = open_login_page
    profile_page = login_page.set_email(get_user_creds()[0]).set_password(get_user_creds()[1]).click_login_button()
    assert profile_page.is_profile_panel_displayed(), 'Profile panel element is not displayed'
    actual_text = profile_page.is_password_text_displayed()
    assert actual_text == 'Пароль', 'There is not text'

@pytest.mark.regression
def test_my_orders(open_login_page):
    login_page = open_login_page
    profile_page = login_page.login(get_user_creds()[0], get_user_creds()[1])
    my_orders = profile_page.click_on_orders_button()
    actual_text = my_orders.are_my_orders_displayed()
    assert actual_text == "Мої замовлення", 'Orders are not displayed'

@pytest.mark.regression
def test_my_wishlist(open_login_page):
    login_page = open_login_page
    profile_page = login_page.login(get_user_creds()[0], get_user_creds()[1])
    my_wishlist = profile_page.click_on_wishlist_button()
    actual_text = my_wishlist.is_my_wishlist_displayed()
    assert actual_text == "Cписок бажань", 'Wishlist is not displayed'

@pytest.mark.regression
def test_waiting_list(open_login_page):
    login_page = open_login_page
    profile_page = login_page.login(get_user_creds()[0], get_user_creds()[1])
    my_orders = profile_page.click_on_waiting_list_button()
    actual_text = my_orders.is_my_waiting_list_displayed()
    assert actual_text == "Лист очікування", 'Orders are not displayed'

@pytest.mark.regression
def test_user_info_panels(open_login_page):
    login_page = open_login_page
    profile_page = login_page.login(get_user_creds()[0], get_user_creds()[1])
    elements = len(profile_page.are_user_info_panels_displayed())
    assert elements == 2, 'There is not all items'

@pytest.mark.smoke
def test_is_search_present(open_main_page):
    main_page = open_main_page
    assert main_page.is_search_input_displayed(), 'There is not search'

@pytest.mark.smoke
def test_search(open_main_page):
    main_page = open_main_page
    search_page = main_page.set_search_value(get_search_data()).click_search_button()
    assert search_page.is_search_complete(), 'Search is not complete'
    actual_text = search_page.are_search_results_displayed()
    assert actual_text == f'"{get_search_data()}" За вашим запитом знайдено:', 'There is not text'

@pytest.mark.regression
def test_open_found_item(open_main_page):
    main_page = open_main_page
    search_page = main_page.set_search_value(get_search_data()).click_search_button()
    item_page = search_page.click_on_game_button()
    actual_text = item_page.is_game_page_displayed()
    assert actual_text == "Настільна гра Carcassonne Grundspiel 3.0 / Каркасон 3.0", 'There is not text'

@pytest.mark.regression
def test_check_amount_of_found_items(open_main_page):
    main_page = open_main_page
    search_page = main_page.set_search_value(get_search_data()).click_search_button()
    elements = len(search_page.are_all_search_items_displayed())
    assert elements == 23, 'There is not all items'

@pytest.mark.smoke
def test_check_items_on_the_main_page(open_main_page):
    main_page = open_main_page
    elements = len(main_page.are_main_page_items_displayed())
    assert elements == 28, 'There is not all items'

@pytest.mark.smoke
def test_all_games_button_present(open_main_page):
    main_page = open_main_page
    assert main_page.is_all_games_button_displayed(), 'There is not button'

@pytest.mark.smoke
def test_open_catalog_page(open_main_page):
    main_page = open_main_page
    catalog_page = main_page.click_all_board_games_button()
    actual_text = catalog_page.is_page_open()
    assert actual_text == 'Каталог настільних ігор', 'There is not text'

@pytest.mark.regression
def test_price_filter(open_catalog_page):
    catalog_page = open_catalog_page
    filter_result = catalog_page.set_start_price(get_prices()[0]).set_end_price(get_prices()[1]).click_ok_button()
    assert filter_result.get_price_filter_results(), "There are not results"
    actual_text = filter_result.are_search_prices_correct()
    assert actual_text == f'{get_prices()[0]}-{get_prices()[1]} грн. ✖', 'There is not text'

@pytest.mark.regression
def test_filter_for_two(open_catalog_page):
    catalog_page = open_catalog_page
    filter_result = catalog_page.click_on_for_two()
    assert filter_result.get_filter_results(), "There are not results"
    actual_text = filter_result.are_search_results_correct()
    assert actual_text == 'Для двох ✖', 'There is not text'

@pytest.mark.regression
def test_price_and_for_two_filters(open_catalog_page):
    catalog_page = open_catalog_page
    filter_result = catalog_page.set_start_price(get_prices()[0]).set_end_price(get_prices()[1]).click_ok_button().click_on_for_two()
    actual_text_price = filter_result.are_search_prices_correct()
    assert actual_text_price == f'{get_prices()[0]}-{get_prices()[1]} грн. ✖', 'There is not text'
    actual_text_for_two = filter_result.are_search_results_correct()
    assert actual_text_for_two == 'Для двох ✖', 'There is not text'

@pytest.mark.regression
def test_two_filters_and_remove_one(open_catalog_page):
    catalog_page = open_catalog_page
    filter_result = catalog_page.click_on_for_two().click_on_rest_and_entertainment().click_on_for_parties()
    assert filter_result.get_filter_results(), "There are not results"
    assert filter_result.get_second_filter_results(), "There are not results"
    filter_result.click_on_skip_filter_for_two()
    with pytest.raises(Exception):
        filter_result.get_second_filter_results()

@pytest.mark.regression
def test_amount_of_items_on_catalog_page(open_catalog_page):
    catalog_page = open_catalog_page
    elements = len(catalog_page.are_all_products_displayed())
    assert elements == 60, 'There is not all items'
