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
