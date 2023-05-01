from homework_17.utilities.web_ui.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __search_word = (By.XPATH, "//*[@class='f13']")
    __catalog = (By.CSS_SELECTOR, "#catalog")

    def are_search_results_displayed(self):
        return self._get_text(self.__search_word)

    def is_search_complete(self):
        catalog_elements = self._wait_until_element_located(self.__catalog)
        return catalog_elements.is_displayed()
