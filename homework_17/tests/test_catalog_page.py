import pytest

from homework_17.utilities.config_reader import get_prices

@pytest.mark.smoke
def test_open_catalog_page(open_main_page):
    main_page = open_main_page
    catalog_page = main_page.click_all_board_games_button()
    actual_text = catalog_page.get_text_from_catalog_header()
    assert actual_text == 'Каталог настільних ігор', 'There is not text'

@pytest.mark.regression
def test_price_filter(open_catalog_page):
    catalog_page = open_catalog_page
    filter_result = catalog_page.set_start_price(get_prices()[0]).set_end_price(get_prices()[1]).click_ok_button()
    assert filter_result.get_price_filter_results(), "There are not results"
    actual_text = filter_result.get_text_at_prices_filter()
    assert actual_text == f'{get_prices()[0]}-{get_prices()[1]} грн. ✖', 'There is not text'

@pytest.mark.regression
def test_filter_for_two(open_catalog_page):
    catalog_page = open_catalog_page
    filter_result = catalog_page.click_on_for_two()
    assert filter_result.get_filter_results(), "There are not results"
    actual_text = filter_result.get_text_at_for_two_filter()
    assert actual_text == 'Для двох ✖', 'There is not text'

@pytest.mark.regression
def test_price_and_for_two_filters(open_catalog_page):
    catalog_page = open_catalog_page
    filter_result = catalog_page.set_start_price(get_prices()[0]).set_end_price(get_prices()[1]).click_ok_button().click_on_for_two()
    actual_text_price = filter_result.get_text_at_prices_filter()
    assert actual_text_price == f'{get_prices()[0]}-{get_prices()[1]} грн. ✖', 'There is not text'
    actual_text_for_two = filter_result.get_text_at_for_two_filter()
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
    elements = len(catalog_page.get_list_of_visible_products())
    assert elements == 60, 'There is not all items'
