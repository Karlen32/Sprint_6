from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.home_page import HomePage
from config.urls import HOME_PAGE as URL
from config.settings import SHORT_WAIT
import allure


class TestLogoNavigation:
    
    @allure.title("Проверка перехода по логотипу Самоката на главную страницу")
    @allure.description("""
    Проверяем, что при клике на логотип Самоката происходит переход на главную страницу.
    Тест открывает форму заказа, затем нажимает на логотип и убеждается, что URL правильный.
    """)
    def test_click_scooter_logo_returns_home(driver):
        page = HomePage(driver)
        page.open(URL)

        page.click_order_header_button()
        page.click_scooter_logo_button()

        WebDriverWait(driver, SHORT_WAIT).until(EC.url_to_be(URL))
        assert driver.current_url == URL
        

    @allure.title("Переход по логотипу Яндекса → открывается Дзен в новом окне")
    @allure.description("""
    1. Открываем главную страницу.
    2. Кликаем по логотипу Яндекса.
    3. Переключаемся на новое окно.
    4. Ждём редиректа на https://dzen.ru.
    5. Проверяем, что открыт Дзен.
    """)
    def test_click_yandex_logo_opens_dzen_in_new_tab(driver):
        home = HomePage(driver)
        home.open(URL)

        main_window = driver.current_window_handle
        old_windows = driver.window_handles

        home.click_yandex_logo_button()

        WebDriverWait(driver, SHORT_WAIT).until(
            lambda d: len(d.window_handles) > len(old_windows)
        )

        new_window = [w for w in driver.window_handles if w != main_window][0]

        driver.switch_to.window(new_window)

        WebDriverWait(driver, SHORT_WAIT).until(
            EC.url_contains("dzen.ru")
        )

        assert "dzen.ru" in driver.current_url

    
