from pages.base_page import BasePage
from locators.order_status_locators import OrderStatusLocators


class OrderStatusPage(BasePage):

    def get_track_number(self):
        elem = self.find(OrderStatusLocators.TRACK_NUMBER_INPUT)
        return elem.get_attribute("value")
