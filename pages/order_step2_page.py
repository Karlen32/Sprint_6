import time
from selenium.webdriver.support.ui import WebDriverWait
from locators.order_page_step2_locators import OrderStep2Locators
from selenium.webdriver.support import expected_conditions as EC
from config.settings import SHORT_WAIT


class OrderStep2Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, SHORT_WAIT)

    def set_delivery_date(self, day):
     
        self.driver.find_element(*OrderStep2Locators.DATE_INPUT).click()
        time.sleep(0.3)
        days = self.driver.find_elements(*OrderStep2Locators.DATE_DAY)

        for d in days:
            if d.text.strip() == str(day):
                d.click()
                return


    def select_rental_period(self, period_text):
        self.driver.find_element(*OrderStep2Locators.RENTAL_PERIOD_DROPDOWN).click()
        time.sleep(0.2)

        options = self.driver.find_elements(*OrderStep2Locators.RENTAL_PERIOD_OPTIONS)
        for opt in options:
            if opt.text.strip() == period_text.strip():
                opt.click()
                return

    def select_color(self, color):
        if color == "black":
            self.driver.find_element(*OrderStep2Locators.COLOR_BLACK).click()
        elif color == "grey":
            self.driver.find_element(*OrderStep2Locators.COLOR_GREY).click()

    def write_comment(self, text):
        self.driver.find_element(*OrderStep2Locators.COMMENT_INPUT).send_keys(text)

    def click_order(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(OrderStep2Locators.ORDER_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", btn)

    def confirm_order(self):
        yes_btn = self.wait.until(
            EC.element_to_be_clickable(OrderStep2Locators.CONFIRM_YES_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", yes_btn)
        
        time.sleep(3)

    def get_order_number(self):
        self.wait.until(
            EC.text_to_be_present_in_element(
                OrderStep2Locators.ORDER_NUMBER_TEXT,
                "Номер заказа"
            )
        )
        elem = self.driver.find_element(*OrderStep2Locators.ORDER_NUMBER_TEXT)
        import re
        match = re.search(r"\d+", elem.text)
        return match.group(0)

    def go_to_status_page(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(OrderStep2Locators.STATUS_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", btn)