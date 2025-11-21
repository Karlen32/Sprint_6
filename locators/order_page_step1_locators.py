from selenium.webdriver.common.by import By

class OrderStep1Locators:
    # Поля ввода
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
    METRO_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]')
    METRO_OPTION = (By.CLASS_NAME, "select-search__option")
    PHONE_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]')

    # Кнопка Далее
    NEXT_BUTTON = (By.CSS_SELECTOR, ".Button_Button__ra12g.Button_Middle__1CSJM")
