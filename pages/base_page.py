import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import SHORT_WAIT


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, SHORT_WAIT)

    @allure.step("Открываем страницу: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Находим элемент: {locator}")
    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Находим элементы: {locator}")
    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Кликаем по элементу: {locator}")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Вводим текст '{text}' в элемент: {locator}")
    def type(self, locator, text):
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(text)

    @allure.step("Скроллим к элементу: {locator}")
    def scroll_to(self, locator):
        elem = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elem)

    def get_current_url(self):
        return self.driver.current_url

    def get_window_handles(self):
        return self.driver.window_handles

    def get_current_window(self):
        return self.driver.current_window_handle

    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    def wait_new_window_opened(self, old_handles):
        self.wait.until(lambda d: len(d.window_handles) > len(old_handles))
        new = [h for h in self.driver.window_handles if h not in old_handles]
        return new[0]

    def wait_url_to_be(self, url):
        self.wait.until(EC.url_to_be(url))

    def wait_url_contains(self, text):
        self.wait.until(EC.url_contains(text))
