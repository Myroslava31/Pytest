from homework_18.utilities.web_ui.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __search_word = (By.XPATH, "//*[@class='f13']")
    __catalog = (By.CSS_SELECTOR, "#catalog")
    __carcassonne_grundspiel_item = (By.XPATH, "//*[@alt='Carcassonne Grundspiel 3.0']//ancestor::a")
    __carcassonne_header = (By.XPATH, "//h1")
    __carcassonne_found_items = (By.CLASS_NAME, 'product')


    def get_text_after_search(self):
        return self._get_text(self.__search_word)

    def is_catalog_displayed(self):
        return self._is_displayed(self.__catalog)

    def click_on_game_button(self):
        self._click_via_js(self.__carcassonne_grundspiel_item)
        return self

    def get_game_page_header_text(self):
        return self._get_text(self.__carcassonne_header)

    def create_list_with_search_items_displayed(self):
        return self._crate_list_of_visible_elements(self.__carcassonne_found_items)

