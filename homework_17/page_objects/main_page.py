from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(self.driver, 10, 1)

    __my_cabinet = (By.CSS_SELECTOR, "[class='head_elem singin_v']")

    def click_my_cabinet_button(self):
        my_cabinet_button = self.__wait.until(EC.presence_of_element_located(self.__my_cabinet))
        my_cabinet_button.click()
        return LoginPage(self, driver)
