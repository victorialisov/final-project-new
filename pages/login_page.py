from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        login_lbl = self.find_element(LoginPageLocators.LOCATOR_LOGIN_LABEL)
        assert login_lbl.get_attribute("innerText") == "Log in"

    def login(self, email: str, passwd: str):
        email_field = self.find_element(LoginPageLocators.LOCATOR_EMAIL_LOGIN_FIELD)
        email_field.send_keys(email)

        passwd_field = self.find_element(LoginPageLocators.LOCATOR_PASSWD_LOGIN_FIELD)
        passwd_field.send_keys(passwd)

        submit_btn = self.find_element(LoginPageLocators.LOCATOR_SUBMIT_BTN)
        submit_btn.click()
