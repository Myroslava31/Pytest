import pytest

from homework_17.utilities.config_reader import get_search_data

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
