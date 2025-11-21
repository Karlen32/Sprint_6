from pages.home_page import HomePage
from config.urls import HOME_PAGE as URL
import allure


@allure.feature("Переход по логотипам")
class TestLogoNavigation:
    
    @allure.title("Проверка перехода по логотипу Самоката на главную страницу")
    def test_click_scooter_logo_returns_home(self, driver):
        page = HomePage(driver)

        with allure.step("Открываем главную страницу"):
            page.open(URL)

        with allure.step("Кликаем по кнопке 'Заказать' в хедере"):
            page.click_order_header_button()

        with allure.step("Кликаем по логотипу Самоката"):
            page.click_scooter_logo_button()

        with allure.step("Ожидаем переход на главную страницу"):
            page.wait_url_to_be(URL)

        with allure.step("Проверяем, что URL соответствует главной странице"):
            assert page.get_current_url() == URL
    

    @allure.title("Переход по логотипу Яндекса → открывается Дзен в новом окне")
    def test_click_yandex_logo_opens_dzen_in_new_tab(self, driver):
        home = HomePage(driver)

        with allure.step("Открываем главную страницу"):
            home.open(URL)

        with allure.step("Сохраняем список текущих окон"):
            old_windows = home.get_window_handles()

        with allure.step("Кликаем по логотипу Яндекса"):
            home.click_yandex_logo_button()

        with allure.step("Ожидаем открытие новой вкладки"):
            new_window = home.wait_new_window_opened(old_windows)

        with allure.step("Переключаемся в новую вкладку"):
            home.switch_to_window(new_window)

        with allure.step("Ждём редирект на Дзен"):
            home.wait_url_contains("dzen.ru")

        with allure.step("Проверяем, что открыт Дзен"):
            assert "dzen.ru" in home.get_current_url()


    
