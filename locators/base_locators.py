from selenium.webdriver.common.by import By


class BaseLocators:

    # Кнопка принятия cookies
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")

    # Логотипы
    LOGO_YANDEX = (By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI")
    LOGO_SCOOTER = (By.CSS_SELECTOR, ".Header_LogoScooter__3lsAR")

    # Кнопки в хедере
    ORDER_BUTTON_HEADER = (By.CSS_SELECTOR, ".Header_Nav__AGCXC .Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (By.CSS_SELECTOR, ".Home_FinishButton__1_cWm .Button_Button__ra12g")
    STATUS_BUTTON_HEADER = (By.CSS_SELECTOR, ".Header_Link__1TAG7")

    # Поле ввода номера заказа
    ORDER_INPUT = (By.CSS_SELECTOR, ".Header_Input__xIoUq")

    # Кнопка Go!
    GO_BUTTON = (By.CSS_SELECTOR, ".Header_Button__28dPO")

    

   
