from pages.base_page import BasePage
from locators.home_locators import HomeLocators
from locators.base_locators import BaseLocators
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    def accept_cookies(self):
        self.click(BaseLocators.COOKIE_ACCEPT_BUTTON)

    def click_order_header_button(self):
        self.click(BaseLocators.ORDER_BUTTON_HEADER)

    def click_order_footer_button(self):
        self.scroll_to(BaseLocators.ORDER_BUTTON_BOTTOM)
        self.click(BaseLocators.ORDER_BUTTON_BOTTOM)

    def click_order_button(self, entry):
        if entry == "header":
            self.click(BaseLocators.ORDER_BUTTON_HEADER)
        elif entry == "bottom":
            self.scroll_to(BaseLocators.ORDER_BUTTON_BOTTOM)
            self.click(BaseLocators.ORDER_BUTTON_BOTTOM)

    def click_scooter_logo_button(self):
        self.click(BaseLocators.LOGO_SCOOTER)

    def click_yandex_logo_button(self):
        self.click(BaseLocators.LOGO_YANDEX)

    def scroll_to_faq(self):
        self.scroll_to(HomeLocators.FAQ_BLOCK)

    def click_question_by_text(self, text):
        questions = self.find_all(HomeLocators.FAQ_QUESTION_BUTTONS)

        for q in questions:
            if q.text.strip() == text.strip():
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", q)
                q.click()
                return

    def get_answer_by_index(self, index):
        answers = self.find_all(HomeLocators.FAQ_ANSWER_TEXTS)
        self.wait.until(EC.visibility_of(answers[index]))
        return answers[index].text.strip()


