from selenium.webdriver.common.by import By


class MainPageLocators:
    LOCATOR_LOGIN_BTN = (By.XPATH, '//a[contains(text(), \'Log in\')]')
    LOCATOR_SIGN_UP_BTN = (By.XPATH, '//a[contains(text(), \'Sign up\')]')
    LOCATOR_CATERERS_MENU = (By.XPATH, '//a[@href = \'/caterers\']')
