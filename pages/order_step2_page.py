import time
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_step2_locators import OrderStep2Locators
import allure


class OrderStep2Page(BasePage):

    @allure.step("Выбираем дату доставки: {day}")
    def set_delivery_date(self, day):
        self.click(OrderStep2Locators.DATE_INPUT)
        time.sleep(0.3)

        days = self.find_all(OrderStep2Locators.DATE_DAY)
        for d in days:
            if d.text.strip() == str(day):
                d.click()
                return

    @allure.step("Выбираем срок аренды: {period}")
    def select_rental_period(self, period):
        self.click(OrderStep2Locators.RENTAL_PERIOD_DROPDOWN)
        time.sleep(0.2)

        options = self.find_all(OrderStep2Locators.RENTAL_PERIOD_OPTIONS)
        for o in options:
            if o.text.strip() == period.strip():
                o.click()
                return

    @allure.step("Выбираем цвет: {color}")
    def select_color(self, color):
        if color == "black":
            self.click(OrderStep2Locators.COLOR_BLACK)
        elif color == "grey":
            self.click(OrderStep2Locators.COLOR_GREY)

    @allure.step("Пишем комментарий: {text}")
    def write_comment(self, text):
        self.type(OrderStep2Locators.COMMENT_INPUT, text)

    @allure.step("Кликаем кнопку Заказать")
    def click_order(self):
        btn = self.find(OrderStep2Locators.ORDER_BUTTON)
        self.driver.execute_script("arguments[0].click();", btn)

    @allure.step("Подтверждаем заказ")
    def confirm_order(self):
        btn = self.find(OrderStep2Locators.CONFIRM_YES_BUTTON)
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(1)

    @allure.step("Получаем номер заказа")
    def get_order_number(self):
        self.wait.until(
            EC.text_to_be_present_in_element(
                OrderStep2Locators.ORDER_NUMBER_TEXT, "Номер заказа"
            )
        )
        elem = self.find(OrderStep2Locators.ORDER_NUMBER_TEXT)

        import re
        return re.search(r"\d+", elem.text).group(0)

    @allure.step("Переходим на страницу статуса заказа")
    def go_to_status_page(self):
        btn = self.find(OrderStep2Locators.STATUS_BUTTON)
        self.driver.execute_script("arguments[0].click();", btn)
