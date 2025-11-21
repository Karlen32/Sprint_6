# Автотесты для сервиса «Самокат»

Проект содержит автотесты на Selenium + Pytest для учебного сервиса «Самокат».

## Установка и запуск

### Установить зависимости

- `pip install -r requirements.txt`

### Запуск тестов

- `pytest -v tests/...  .py`

### Запуск тестов с Allure

- `pytest --alluredir=allure_results`
- `allure generate allure_results -o allure-report --clean`
- `allure open allure-report`

### Основные разделы автотестов

- `FAQ — проверка вопросов и ответов`
- `Оформление заказа — два позитивных сценария`
- `Переход по логотипам (Самокат / Яндекс)`
- `Проверка страницы статуса заказа`

### Стек

- `Python 3.12`
- `Selenium`
- `Pytest`
- `Allure`
- `Firefox + geckodriver`