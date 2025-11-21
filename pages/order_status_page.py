from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.order_status_locators import OrderStatusLocators
from config.settings import SHORT_WAIT


class OrderStatusPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, SHORT_WAIT)

    def get_track_number(self):
        elem = self.wait.until(
            EC.visibility_of_element_located(OrderStatusLocators.TRACK_NUMBER_INPUT)
        )
        return elem.get_attribute("value")