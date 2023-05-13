from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from homework_17.utilities.web_ui.base_page import BasePage


class UserProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __profile_panel = (By.CSS_SELECTOR, "#prof_navi")
    __password_text = (By.XPATH, "//*[@id='prof_cont']//legend")
    __orders_button = (By.XPATH, "//*[text()= 'Замовлення']")
    __header_my_orders = (By.XPATH, "//h1")
    __wishlist_button = (By.XPATH, "//b[contains(text(), 'Cписок бажань')]")
    __header_wishlist = (By.XPATH, "//h1")
    __waiting_list = (By.XPATH, "//*[text()= 'Лист очікування']")
    __header_waiting_list = (By.XPATH, "//h1")
    __user_info_panels = (By.CLASS_NAME, 'prof')


    def is_profile_panel_displayed(self):
        profile_panel_element = self._wait_until_element_located(self.__profile_panel)
        return profile_panel_element.is_displayed()

    def is_password_text_displayed(self):
        return self._get_text(self.__password_text)

    def click_on_orders_button(self):
        self._click_via_js(self.__orders_button)
        return self

    def are_my_orders_displayed(self):
        return self._get_text(self.__header_my_orders)

    def click_on_wishlist_button(self):
        self._click_via_js(self.__wishlist_button)
        return self

    def is_my_wishlist_displayed(self):
        return self._get_text(self.__header_wishlist)

    def click_on_waiting_list_button(self):
        self._click_via_js(self.__waiting_list)
        return self

    def is_my_waiting_list_displayed(self):
        return self._get_text(self.__header_waiting_list)

    def are_user_info_panels_displayed(self):
        return self._wait_until_elements_are_located(self.__user_info_panels)

