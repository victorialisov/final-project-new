from selenium.webdriver.common.by import By


class UserProfileLocators:
    LOCATOR_SUBMIT_BTN = (By.XPATH, '//button[@class = \'btn btn-red\']')
    LOCATOR_USER_NAME_LBL = (By.XPATH, '//div[@class = \'dashboard-info__name\']')
