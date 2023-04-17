import pytest
from homework_17.utilities.driver_factory import driver_factory
from homework_17.utilities.config_reader import get_application_url, get_browser_id

@pytest.fixture()
def create_browser():
    driver = driver_factory(get_browser_id())
    driver.maximize_window()
    driver.get(get_application_url())
    yield driver
    driver.quit()
