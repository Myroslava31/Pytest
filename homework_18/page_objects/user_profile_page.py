from selenium.webdriver.common.by import By
from homework_18.utilities.web_ui.base_page import BasePage


class UserProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __profile_panel = (By.CSS_SELECTOR, "#prof_navi")
    __password_text = (By.XPATH, "//*[@id='prof_cont']//legend")
    __orders_button = (By.XPATH, "//*[@href='https://desktopgames.com.ua/ua/user/orders']")
    __header_my_orders = (By.XPATH, "//h1")
    __wishlist_button = (By.XPATH, "//b[contains(text(), 'Cписок бажань')]")
    __header_wishlist = (By.XPATH, "//h1")
    __waiting_list = (By.XPATH, "//*[@href='https://desktopgames.com.ua/ua/user/waitlist']")
    __header_waiting_list = (By.XPATH, "//h1")
    __user_info_panels = (By.CLASS_NAME, 'prof')


    def is_profile_panel_displayed(self):
        return self._is_displayed(self.__profile_panel)

    def get_password_text(self):
        return self._get_text(self.__password_text)

    def click_on_orders_button(self):
        self._click_via_js(self.__orders_button)
        return self

    def get_header_text_my_orders(self):
        return self._get_text(self.__header_my_orders)

    def click_on_wishlist_button(self):
        self._click_via_js(self.__wishlist_button)
        return self

    def get_header_text_wishlist(self):
        return self._get_text(self.__header_wishlist)

    def click_on_waiting_list_button(self):
        self._click_via_js(self.__waiting_list)
        return self

    def get_header_text_waiting_list(self):
        return self._get_text(self.__header_waiting_list)

    def get_list_with_user_info_panels(self):
        return self._crate_list_of_visible_elements(self.__user_info_panels)

