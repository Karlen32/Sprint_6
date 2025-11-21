from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.home_locators import HomeLocators
from config.settings import SHORT_WAIT
from locators.base_locators import BaseLocators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, SHORT_WAIT)

    def open(self, url):
        self.driver.get(url)

    def accept_cookies(self):
        self.driver.find_element(*BaseLocators.COOKIE_ACCEPT_BUTTON).click()


    def click_order_header_button(self):
        """Кнопка Заказать в хедере — скролл не нужен"""
        self.driver.find_element(*BaseLocators.ORDER_BUTTON_HEADER).click()


    def click_scooter_logo_button(self):
        self.driver.find_element(*BaseLocators.LOGO_SCOOTER).click()

    def click_yandex_logo_button(self):
        self.driver.find_element(*BaseLocators.LOGO_YANDEX).click()


    def click_order_button(self, entry):
        if entry == "header":
            btn = self.driver.find_element(*BaseLocators.ORDER_BUTTON_HEADER)

        elif entry == "bottom":
            btn = self.driver.find_element(*BaseLocators.ORDER_BUTTON_BOTTOM)
            # для нижней кнопки делаем скролл
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)

        btn.click()


    def scroll_to_faq(self):
        faq_block = self.driver.find_element(*HomeLocators.FAQ_BLOCK)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", faq_block)


    def click_question_by_text(self, text):
        questions = self.driver.find_elements(*HomeLocators.FAQ_QUESTION_BUTTONS)

        for q in questions:
            if text.strip() == q.text.strip():
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", q)
                self.wait.until(EC.element_to_be_clickable(q))
                q.click()
                return
                

    def get_answer_by_index(self, index):
        """Возвращает текст ответа по индексу FAQ_DATA."""
        answers = self.driver.find_elements(*HomeLocators.FAQ_ANSWER_TEXTS)

        self.wait.until(EC.visibility_of(answers[index]))

        return answers[index].text.strip()

