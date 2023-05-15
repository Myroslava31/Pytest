import pytest


@pytest.mark.smoke
def test_banner_is_visible(open_main_page):
    main_page = open_main_page
    assert main_page.is_banner_visible(), 'There is not banner'

@pytest.mark.smoke
def test_text_on_top_menu(open_main_page):
    main_page = open_main_page
    actual_text = main_page.get_top_menu_text()
    assert actual_text == "Оплата і доставкаКонтакти м. Київ, вул. Івана Франка, 12 Пн-Пт: 10:00-20:00 | Сб-Нд: 12:00-18:00", 'There is not text'

@pytest.mark.smoke
def test_my_cabinet_present(open_main_page):
    main_page = open_main_page
    assert main_page.is_my_cabinet_button_visible(), 'There is not button'

@pytest.mark.smoke
def test_is_search_present(open_main_page):
    main_page = open_main_page
    assert main_page.is_search_input_visible(), 'There is not search'

@pytest.mark.smoke
def test_check_items_on_the_main_page(open_main_page):
    main_page = open_main_page
    elements = len(main_page.get_list_of_main_page_items_displayed())
    assert elements == 28, 'There is not all items'

@pytest.mark.smoke
def test_all_games_button_present(open_main_page):
    main_page = open_main_page
    assert main_page.is_all_games_button_visible(), 'There is not button'
