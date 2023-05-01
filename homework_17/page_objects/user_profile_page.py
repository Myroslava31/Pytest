from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from homework_17.utilities.web_ui.base_page import BasePage


class UserProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __profile_panel = (By.CSS_SELECTOR, "#prof_navi")
    __password_text = (By.XPATH, "//*[@id='prof_cont']//legend")

    def is_profile_panel_displayed(self):
        profile_panel_element = self._wait_until_element_located(self.__profile_panel)
        return profile_panel_element.is_displayed()

    def is_password_text_displayed(self):
        return self._get_text(self.__password_text)

