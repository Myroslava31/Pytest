from homework_17.utilities.web_ui.base_page import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    __catalog_header = (By.XPATH, "//h1")
    __min_price_input = (By.CSS_SELECTOR, "[name='price_min']")
    __max_price_input = (By.CSS_SELECTOR, "[name='price_max']")
    __ok_button = (By.CSS_SELECTOR, "[value='ОК']")
    __filter_for_price = (By.XPATH, "//a[contains(text(), 'грн')]")
    __filter_for_two = (By.XPATH, "//*[@title= 'Скинути фільтр Для двох']")
    __filter_for_parties = (By.XPATH, "//*[@title= 'Скинути фільтр Для вечірок']")
    __for_two_checkbox = (By.CSS_SELECTOR, "[title='Для двох']")
    __rest_and_entertainment_button = (By.XPATH, "//*[text()= 'Відпочинок та розваги']")
    __for_parties_checkbox = (By.CSS_SELECTOR, "[title='Для вечірок']")
    __all_products = (By.CLASS_NAME, 'product')


    def is_page_open(self):
        return self._get_text(self.__catalog_header)

    def set_start_price(self, price: int):
        self._send_keys(locator=self.__min_price_input, value=price)
        return self

    def set_end_price(self, price: int):
        self._send_keys(locator=self.__max_price_input, value=price)
        return self

    def click_ok_button(self):
        self._click_via_js(self.__ok_button)
        return self

    def get_price_filter_results(self):
        filter_result = self._wait_until_element_located(self.__filter_for_price)
        return filter_result.is_displayed()

    def get_filter_results(self):
        filter_result = self._wait_until_element_located(self.__filter_for_two)
        return filter_result.is_displayed()

    def get_second_filter_results(self):
        filter_result = self._wait_until_element_located(self.__filter_for_parties)
        return filter_result.is_displayed()

    def remove_one_filter(self):
        self._click_via_js(self.__filter_for_two)
        return self

    def are_search_prices_correct(self):
        return self._get_text(self.__filter_for_price)

    def are_search_results_correct(self):
        return self._get_text(self.__filter_for_two)

    def click_on_for_two(self):
        self._click_via_js(self.__for_two_checkbox)
        return self

    def click_on_rest_and_entertainment(self):
        self._click_via_js(self.__rest_and_entertainment_button)
        return self

    def click_on_for_parties(self):
        self._click_via_js(self.__for_parties_checkbox)
        return self

    def click_on_skip_filter_for_two(self):
        self._click_via_js(self.__filter_for_parties)
        return self

    def are_all_products_displayed(self):
        return self._wait_until_elements_are_located(self.__all_products)
