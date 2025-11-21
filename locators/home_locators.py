from selenium.webdriver.common.by import By

class HomeLocators:
    # Кнопка вопроса (все вопросы)
    FAQ_QUESTION_BUTTONS = (By.CSS_SELECTOR, ".accordion__button")

    # Ответы (панели)
    FAQ_ANSWER_TEXTS = (By.CSS_SELECTOR, ".accordion__panel p")

    FAQ_BLOCK = (By.CSS_SELECTOR, ".Home_FAQ__3uVm4")