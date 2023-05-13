from selenium.webdriver.common.by import By

from homework_17.page_objects.catalog_page import CatalogPage
from homework_17.page_objects.login_page import LoginPage
from homework_17.page_objects.search_page import SearchPage
from homework_17.utilities.web_ui.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __my_cabinet = (By.CSS_SELECTOR, "[class='head_elem singin_v']")
    __search_input = (By.XPATH, "//*[@id='search_submit']/*[@id='autocomplete']")
    __search_button = (By.CSS_SELECTOR, "#search_submit > input.search_btn")
    __all_board_games_button = (By.XPATH, "//*[@title='Всі настільні ігри']")
    __main_page_items = (By.CLASS_NAME, 'product')
    __main_banner = (By.XPATH, "//*[@class='main-banners']")
    __top_menu = (By.XPATH, "//*[@class='head_cont_desk']")

    def is_my_cabinet_button_displayed(self):
        return self._wait_until_element_located(self.__my_cabinet)

    def is_all_games_button_displayed(self):
        return self._wait_until_element_located(self.__all_board_games_button)

    def click_my_cabinet_button(self):
        self._click_via_js(self.__my_cabinet)
        return LoginPage(self.driver)

    def is_search_input_displayed(self):
        return self._wait_until_element_located(self.__search_input), self._wait_until_element_located(self.__search_button)

    def set_search_value(self, search_word):
        self._send_keys(locator=self.__search_input, value=search_word)
        return self

    def click_search_button(self):
        self._click_via_js(self.__search_button)
        return SearchPage(self.driver)

    def click_all_board_games_button(self):
        self._click_via_js(self.__all_board_games_button)
        return CatalogPage(self.driver)

    def are_main_page_items_displayed(self):
        return self._wait_until_elements_are_located(self.__main_page_items)

    def is_banner_displayed(self):
        return self._wait_until_elements_are_located(self.__main_banner)

    def is_top_menu_text_displayed(self):
        return self._get_text(self.__top_menu)

