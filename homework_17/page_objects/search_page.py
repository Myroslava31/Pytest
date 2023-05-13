from homework_17.utilities.web_ui.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __search_word = (By.XPATH, "//*[@class='f13']")
    __catalog = (By.CSS_SELECTOR, "#catalog")
    __carcassonne_grundspiel_item = (By.XPATH, "//*[@alt='Carcassonne Grundspiel 3.0']//ancestor::a")
    __carcassonne_header = (By.XPATH, "//h1")
    __carcassonne_found_items = (By.CLASS_NAME, 'product')


    def are_search_results_displayed(self):
        return self._get_text(self.__search_word)

    def is_search_complete(self):
        catalog_elements = self._wait_until_element_located(self.__catalog)
        return catalog_elements.is_displayed()

    def click_on_game_button(self):
        self._click_via_js(self.__carcassonne_grundspiel_item)
        return self

    def is_game_page_displayed(self):
        return self._get_text(self.__carcassonne_header)

    def are_all_search_items_displayed(self):
        return self._wait_until_elements_are_located(self.__carcassonne_found_items)

