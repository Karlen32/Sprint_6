from pages.base_page import BasePage
from locators.home_locators import HomeLocators
from locators.base_locators import BaseLocators
from selenium.webdriver.support import expected_conditions as EC
import allure


class HomePage(BasePage):

    @allure.step("Принимаем куки")
    def accept_cookies(self):
        self.click(BaseLocators.COOKIE_ACCEPT_BUTTON)

    @allure.step("Кликаем кнопку Заказать в хедере")
    def click_order_header_button(self):
        self.click(BaseLocators.ORDER_BUTTON_HEADER)

    @allure.step("Кликаем кнопку Заказать внизу страницы")
    def click_order_footer_button(self):
        self.scroll_to(BaseLocators.ORDER_BUTTON_BOTTOM)
        self.click(BaseLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Кликаем кнопку Заказать ({entry})")
    def click_order_button(self, entry):
        if entry == "header":
            self.click(BaseLocators.ORDER_BUTTON_HEADER)
        elif entry == "bottom":
            self.scroll_to(BaseLocators.ORDER_BUTTON_BOTTOM)
            self.click(BaseLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Кликаем по логотипу Самоката")
    def click_scooter_logo_button(self):
        self.click(BaseLocators.LOGO_SCOOTER)

    @allure.step("Кликаем по логотипу Яндекса")
    def click_yandex_logo_button(self):
        self.click(BaseLocators.LOGO_YANDEX)

    @allure.step("Скроллим до FAQ-блока")
    def scroll_to_faq(self):
        self.scroll_to(HomeLocators.FAQ_BLOCK)

    @allure.step("Кликаем по вопросу FAQ: {text}")
    def click_question_by_text(self, text):
        questions = self.find_all(HomeLocators.FAQ_QUESTION_BUTTONS)

        for q in questions:
            if q.text.strip() == text.strip():
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", q)
                q.click()
                return

    @allure.step("Получаем ответ по индексу FAQ: {index}")
    def get_answer_by_index(self, index):
        answers = self.find_all(HomeLocators.FAQ_ANSWER_TEXTS)
        self.wait.until(EC.visibility_of(answers[index]))
        return answers[index].text.strip()

