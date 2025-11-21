import pytest
from pages.home_page import HomePage
from config.urls import HOME_PAGE as URL
from data.expected_texts import FAQ_DATA
import allure


class TestFAQ:
    
    @allure.title("FAQ: проверка отображения ответа по вопросу №{index}")
    @allure.story("Проверка выпадения ответов по каждому вопросу из раздела FAQ")
    @allure.description("""
    Тест проверяет работу аккордеона FAQ:
    1. Открываем главную страницу.
    2. Находим нужный вопрос по его тексту.
    3. Скроллим к нему.
    4. Нажимаем на вопрос.
    5. Проверяем, что открылся корректный ответ.
    """)
    @pytest.mark.parametrize("index", range(len(FAQ_DATA)))
    def test_faq_questions_and_answers(driver, index):
        
        page = HomePage(driver)
        page.open(URL)

        page.scroll_to_faq()

        expected_question = FAQ_DATA[index]["question"]
        expected_answer = FAQ_DATA[index]["answer"]

        page.click_question_by_text(expected_question)
        actual_answer = page.get_answer_by_index(index)

        assert actual_answer == expected_answer