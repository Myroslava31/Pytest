from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(self.driver, 10, 1)

    def _wait_until_element_located(self, locator):
        return self.__wait.until(EC.presence_of_element_located(locator))

    def _wait_until_to_be_clickable(self, locator):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def _send_keys(self, locator, value, is_clear=True):
        element = self._wait_until_element_located(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    def _click(self, locator):
        self._wait_until_to_be_clickable(locator).click()

    def _click_via_js(self, locator):
        self.driver.execute_script('arguments[0].click()', self._wait_until_to_be_clickable(locator))

    def _get_text(self, locator):
        element = self._wait_until_element_located(locator)
        return element.text

    def _wait_until_elements_are_visible(self, locator):
        return self.__wait.until(EC.visibility_of_all_elements_located(locator))

    def _is_displayed(self, locator):
        return self._wait_until_element_located(locator).is_displayed

    def _wait_until_element_visible(self, locator):
        return self.__wait.until(EC.visibility_of_element_located(locator))

