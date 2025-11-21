from pages.home_page import HomePage
from config.urls import HOME_PAGE as URL
import allure


class TestLogoNavigation:
    
    @allure.title("Проверка перехода по логотипу Самоката на главную страницу")
    @allure.description("""
    Проверяем, что при клике на логотип Самоката происходит переход на главную страницу.
    Тест открывает форму заказа, затем нажимает на логотип и убеждается, что URL правильный.
    """)
    def test_click_scooter_logo_returns_home(self, driver):
        page = HomePage(driver)

        page.open(URL)
        page.click_order_header_button()
        page.click_scooter_logo_button()

        page.wait_url_to_be(URL)

        assert page.get_current_url() == URL
        

    @allure.title("Переход по логотипу Яндекса → открывается Дзен в новом окне")
    @allure.description("""
    1. Открываем главную страницу.
    2. Кликаем по логотипу Яндекса.
    3. Переключаемся на новое окно.
    4. Ждём редиректа на https://dzen.ru.
    5. Проверяем, что открыт Дзен.
    """)
    def test_click_yandex_logo_opens_dzen_in_new_tab(self, driver):
        
        home = HomePage(driver)
        home.open(URL)

        old_windows = home.get_window_handles()

        home.click_yandex_logo_button()

        # ждём появления нового окна
        new_window = home.wait_new_window_opened(old_windows)

        # переключаемся в новое окно
        home.switch_to_window(new_window)

        # ждём редирект на Дзен
        home.wait_url_contains("dzen.ru")

        assert "dzen.ru" in home.get_current_url()

    
