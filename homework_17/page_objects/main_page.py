from selenium.webdriver.common.by import By
from homework_17.page_objects.login_page import LoginPage
from homework_17.page_objects.search_page import SearchPage
from homework_17.utilities.web_ui.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __my_cabinet = (By.CSS_SELECTOR, "[class='head_elem singin_v']")
    __search_input = (By.XPATH, "//*[@id='search_submit']/*[@id='autocomplete']")
    __search_button = (By.CSS_SELECTOR, "#search_submit > input.search_btn")

    def click_my_cabinet_button(self):
        self._click_via_js(self.__my_cabinet)
        return LoginPage(self.driver)

    def set_search_value(self, search_word):
        self._send_keys(locator=self.__search_input, value=search_word)
        return self

    def click_search_button(self):
        self._click_via_js(self.__search_button)
        return SearchPage
