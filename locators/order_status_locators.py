from selenium.webdriver.common.by import By

class OrderStatusLocators:
    TRACK_NUMBER_INPUT = (By.CSS_SELECTOR, "input.Track_Input__1g7lq")
    GO_BUTTON = (By.XPATH, "//button[text()='Go!' or text()='Отследить']")