from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def open_login_page(self):
        login_btn = self.find_element(MainPageLocators.LOCATOR_LOGIN_BTN)
        login_btn.click()

    def open_sign_in_page(self):
        sign_in_btn = self.find_element(MainPageLocators.LOCATOR_SIGN_UP_BTN)
        sign_in_btn.click()

    def open_passwd_reset_page(self):
        sign_in_btn = self.find_element(MainPageLocators.LOCATOR_SIGN_UP_BTN)
        sign_in_btn.click()
