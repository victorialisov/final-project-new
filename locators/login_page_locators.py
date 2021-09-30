from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOCATOR_EMAIL_LOGIN_FIELD = (By.XPATH, '//input[@type =\'email\']')
    LOCATOR_PASSWD_LOGIN_FIELD = (By.XPATH, '//input[@type =\'password\']')
    LOCATOR_SUBMIT_BTN = (By.XPATH, '//button[@type =\'submit\']')
    LOCATOR_LOGIN_LABEL = (By.XPATH, '//p[contains(text(), \'Log in\')]')
