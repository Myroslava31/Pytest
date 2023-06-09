from selenium.webdriver.common.by import By
from homework_17.page_objects.user_profile_page import UserProfilePage
from homework_17.utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __email_input = (By.CSS_SELECTOR, "[name='email']")
    __password_input = (By.CSS_SELECTOR, "[name='pass']")
    __login_button = (By.CSS_SELECTOR, "[class='input-button']")
    __login_panel = (By.CSS_SELECTOR, "div.login_set")
    __all_inputs = (By.CLASS_NAME, 'input-text')
    __registration_button = (By.XPATH, "//*[@href='https://desktopgames.com.ua/ua/user/registration']")
    __submit_button = (By.XPATH, "//*[@name='submit']")
    __refresh_password = (By.XPATH, "//*[@href='https://desktopgames.com.ua/ua/user/recoverpass']")

    def set_email(self, email: str):
        self._send_keys(locator=self.__email_input, value=email)
        return self

    def set_password(self, password: str):
        self._send_keys(locator=self.__password_input, value=password)
        return self

    def click_login_button(self):
        self._click_via_js(self.__login_button)
        return UserProfilePage(self.driver)

    def login(self, email, password):
        self.set_email(email).set_password(password).click_login_button()
        return UserProfilePage(self.driver)

    def is_login_panel_displayed(self):
        return self._is_displayed(self.__login_panel)

    def get_list_of_visible_input_fields(self):
        return self._crate_list_of_visible_elements(self.__all_inputs)

    def go_to_registration(self):
        self._click_via_js(self.__registration_button)
        return self

    def click_on_registration_button(self):
        self._click(self.__submit_button)
        return self

    def go_to_refresh_password(self):
        self._click_via_js(self.__refresh_password)
        return self

    def click_on_refresh_password_button(self):
        self._click(self.__submit_button)
        return self
