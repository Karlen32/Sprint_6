import time
from pages.base_page import BasePage
from locators.order_page_step1_locators import OrderStep1Locators
import allure


class OrderStep1Page(BasePage):

    @allure.step("Заполняем имя: {name}")
    def fill_first_name(self, name):
        self.type(OrderStep1Locators.FIRST_NAME_INPUT, name)

    @allure.step("Заполняем фамилию: {last_name}")
    def fill_last_name(self, last_name):
        self.type(OrderStep1Locators.LAST_NAME_INPUT, last_name)

    @allure.step("Заполняем адрес: {address}")
    def fill_address(self, address):
        self.type(OrderStep1Locators.ADDRESS_INPUT, address)

    @allure.step("Выбираем станцию метро: {station}")
    def fill_metro(self, station):
        field = self.find(OrderStep1Locators.METRO_INPUT)
        field.send_keys(station)
        time.sleep(0.5)

        options = self.find_all(OrderStep1Locators.METRO_OPTION)
        options[0].click()

    @allure.step("Заполняем телефон: {phone}")
    def fill_phone(self, phone):
        self.type(OrderStep1Locators.PHONE_INPUT, phone)

    @allure.step("Переходим на второй шаг заказа")
    def click_next(self):
        self.click(OrderStep1Locators.NEXT_BUTTON)
