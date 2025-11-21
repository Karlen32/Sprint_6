import pytest
from pages.home_page import HomePage
from config.urls import HOME_PAGE as URL
from data.expected_texts import FAQ_DATA
import allure


@allure.feature("FAQ")
class TestFAQ:

    @pytest.mark.parametrize("index", range(len(FAQ_DATA)))
    @allure.title("FAQ: проверка вопроса №{index}")
    def test_faq_questions_and_answers(self, driver, index):

        with allure.step("Открываем главную страницу"):
            page = HomePage(driver)
            page.open(URL)

        with allure.step("Скроллим до секции FAQ"):
            page.scroll_to_faq()

        expected_q = FAQ_DATA[index]["question"]
        expected_a = FAQ_DATA[index]["answer"]

        with allure.step(f"Открываем вопрос: {expected_q}"):
            page.click_question_by_text(expected_q)

        with allure.step("Считываем ответ"):
            actual_answer = page.get_answer_by_index(index)

        with allure.step("Проверяем соответствие ответа"):
            assert actual_answer == expected_a