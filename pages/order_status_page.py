from pages.base_page import BasePage
from locators.order_status_locators import OrderStatusLocators
import allure


class OrderStatusPage(BasePage):

    @allure.step("Получаем номер из строки состояния заказа")
    def get_track_number(self):
        elem = self.find(OrderStatusLocators.TRACK_NUMBER_INPUT)
        return elem.get_attribute("value")
