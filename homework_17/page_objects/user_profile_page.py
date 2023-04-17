from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(self.driver, 10, 1)

    __profile_panel = (By.CSS_SELECTOR, "#prof_navi")

    def is_profile_panel_displayed(self):
        profile_panel_element = self.__wait.until(EC.visibility_of_element_located(self.__profile_panel))
        return profile_panel_element.is_displayed()

