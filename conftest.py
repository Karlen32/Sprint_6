import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options 
from config.settings import BASE_URL

from pages.home_page import HomePage


@pytest.fixture
def driver():
    options = Options()
    options.set_preference("browser.tabs.remote.autostart", False)
    driver = webdriver.Firefox(options=options)
    driver.get(BASE_URL)
    HomePage(driver).accept_cookies()
    yield driver
    driver.quit()