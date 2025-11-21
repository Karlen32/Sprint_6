import pytest
from pages.home_page import HomePage
from pages.order_step1_page import OrderStep1Page
from pages.order_step2_page import OrderStep2Page
from pages.order_status_page import OrderStatusPage
from config.urls import HOME_PAGE as URL
from data.order_test_data import ORDER_DATA
import allure


class TestOrderScooter:
    
    @allure.title("Проверка успешного оформления заказа и совпадения номера на странице статуса")
    @allure.description("""
    Тест проходит позитивный сценарий оформления заказа.
    Шаги:
    1. Открыть главную страницу.
    2. Нажать кнопку 'Заказать' (точка входа зависит от переданных данных).
    3. Заполнить данные шага 1: имя, фамилию, адрес, метро, телефон.
    4. Перейти на шаг 2.
    5. Выбрать дату, срок аренды, цвет, оставить комментарий.
    6. Подтвердить заказ.
    7. Получить номер заказа.
    8. Перейти на страницу статуса заказа.
    9. Проверить, что отображаемый номер совпадает с полученным.
    """)
    @pytest.mark.parametrize("data", ORDER_DATA)
    def test_order_full_positive(driver, data):

        home = HomePage(driver)
        home.open(URL)

        # точка входа берётся из данных
        home.click_order_button(data["entry"])

        # Шаг 1
        step1 = OrderStep1Page(driver)
        step1.fill_first_name(data["first_name"])
        step1.fill_last_name(data["last_name"])
        step1.fill_address(data["address"])
        step1.fill_metro(data["metro"])
        step1.fill_phone(data["phone"])
        step1.click_next()

        # Шаг 2
        step2 = OrderStep2Page(driver)
        step2.set_delivery_date(data["date"])
        step2.select_rental_period(data["period"])
        step2.select_color(data["color"])
        step2.write_comment(data["comment"])
        step2.click_order()
        step2.confirm_order()

        order_number = step2.get_order_number()
        step2.go_to_status_page()

        status_page = OrderStatusPage(driver)
        assert status_page.get_track_number() == order_number
