from selenium.webdriver.common.by import By


class PasswordResetLocators:
    LOCATOR_PASSWORD_RESET_HEADER = (By.XPATH, '//h2[contains(text(), \'Password Reset:\')]')
    LOCATOR_PASSWORD_FIELD = (By.XPATH, '//input[@name = \'password\']')
    LOCATOR_CONFIRM_PASSWORD_FIELD = (By.XPATH, '//input[@name = \'confirmPassword\']')
    LOCATOR_CHANGE_PASSWORD_BTN = (By.XPATH, '//button[@class = \'btn btn-red reset-confirm-btn\']')
    LOCATOR_REQUEST_COMPLETE_LBL = (By.XPATH, '//label[@class = \'request-complete\']')
    LOCATOR_OPEN_PROFILE_BTN = (By.XPATH, '//a[contains(text(), \'Take me to my Profile\')]')
