from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from homework_17.page_objects.user_profile_page import UserProfilePage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(self.driver, 10, 1)

    __email_input = (By.CSS_SELECTOR, "[name='email']")
    __password_input = (By.CSS_SELECTOR, "[name='pass']")
    __login_button = (By.CSS_SELECTOR, "[name='submit']")

    def set_email(self, email: str):
        element = self.__wait.until(EC.presence_of_element_located(self.__email_input))
        element.clear()
        element.send_keys(email)
        return self

    def set_password(self, password: str):
        password_element = self.__wait.until(EC.presence_of_element_located(self.__password_input))
        password_element.clear()
        password_element.send_keys(password)
        return self

    def click_login_button(self):
        login_button = self.__wait.until(EC.visibility_of_element_located(self.__password_input))
        login_button.click()
        return UserProfilePage(self.driver)
