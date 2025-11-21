from selenium.webdriver.common.by import By


class OrderStep2Locators:
    # Поле даты
    DATE_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]')

    # все дни месяца (видимые)
    DATE_DAY = (By.CSS_SELECTOR, ".react-datepicker__day")

    # Выпадающий список срока аренды
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")

    # Элементы списка срока аренды (Dropdown-menu создаётся при клике)
    RENTAL_PERIOD_OPTIONS = (By.CLASS_NAME, "Dropdown-option")

    # Чекбоксы цвета самоката
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")

    # Поле комментария
    COMMENT_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]')

    # Кнопка "Заказать"
    ORDER_BUTTON = (By.CSS_SELECTOR,"button.Button_Button__ra12g.Button_Middle__1CSJM:not(.Button_Inverted__3IF-i)")
    
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    
    STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
    
    ORDER_NUMBER_TEXT = (By.CSS_SELECTOR, ".Order_Text__2broi")
    
