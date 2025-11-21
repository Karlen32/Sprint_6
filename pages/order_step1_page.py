import time
from selenium.webdriver.support.ui import WebDriverWait
from locators.order_page_step1_locators import OrderStep1Locators
from config.settings import SHORT_WAIT



class OrderStep1Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, SHORT_WAIT)

    def fill_first_name(self, name):
        self.driver.find_element(*OrderStep1Locators.FIRST_NAME_INPUT).send_keys(name)

    def fill_last_name(self, last_name):
        self.driver.find_element(*OrderStep1Locators.LAST_NAME_INPUT).send_keys(last_name)

    def fill_address(self, address):
        self.driver.find_element(*OrderStep1Locators.ADDRESS_INPUT).send_keys(address)

    def fill_metro(self, station):
        
        input_field = self.driver.find_element(*OrderStep1Locators.METRO_INPUT)
        input_field.send_keys(station)
        time.sleep(0.5)

        options = self.driver.find_elements(*OrderStep1Locators.METRO_OPTION)

        
        options[0].click()


    def fill_phone(self, phone):
        self.driver.find_element(*OrderStep1Locators.PHONE_INPUT).send_keys(phone)

    def click_next(self):
        self.driver.find_element(*OrderStep1Locators.NEXT_BUTTON).click()
