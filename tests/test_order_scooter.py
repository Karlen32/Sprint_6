import pytest
from pages.home_page import HomePage
from pages.order_step1_page import OrderStep1Page
from pages.order_step2_page import OrderStep2Page
from pages.order_status_page import OrderStatusPage
from config.urls import HOME_PAGE as URL
from data.order_test_data import ORDER_DATA
import allure


@allure.feature("Оформление заказа")
class TestOrderScooter:

    @pytest.mark.parametrize("data", ORDER_DATA)
    @allure.title("Позитивный сценарий заказа самоката ({data[entry]})")
    def test_order_full_positive(self, driver, data):

        with allure.step("Открываем главную страницу"):
            home = HomePage(driver)
            home.open(URL)

        with allure.step(f"Нажимаем кнопку Заказать ({data['entry']})"):
            home.click_order_button(data["entry"])

        step1 = OrderStep1Page(driver)

        with allure.step("Заполняем первый шаг заказа"):
            step1.fill_first_name(data["first_name"])
            step1.fill_last_name(data["last_name"])
            step1.fill_address(data["address"])
            step1.fill_metro(data["metro"])
            step1.fill_phone(data["phone"])
            step1.click_next()

        step2 = OrderStep2Page(driver)

        with allure.step("Заполняем второй шаг"):
            step2.set_delivery_date(data["date"])
            step2.select_rental_period(data["period"])
            step2.select_color(data["color"])
            step2.write_comment(data["comment"])

        with allure.step("Подтверждаем заказ"):
            step2.click_order()
            step2.confirm_order()

        with allure.step("Получаем номер заказа"):
            order_number = step2.get_order_number()

        with allure.step("Переходим на страницу статуса"):
            step2.go_to_status_page()

        status_page = OrderStatusPage(driver)

        with allure.step("Проверяем, что номер введён автоматически"):
            assert status_page.get_track_number() == order_number