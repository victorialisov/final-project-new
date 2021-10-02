from pages.base_page import BasePage
from locators.passwd_reset_page_locators import PasswordResetLocators


class PasswordReset(BasePage):

    def should_be_password_reset_page(self):
        password_reset_lbl = self.find_element(PasswordResetLocators.LOCATOR_PASSWORD_RESET_HEADER)
        assert password_reset_lbl.text == "Password Reset:"

    def password_reset(self, passwd: str):
        passwd_field = self.find_element(PasswordResetLocators.LOCATOR_PASSWORD_FIELD)
        passwd_field.send_keys(passwd)

        confirm_passwd_field = self.find_element(PasswordResetLocators.LOCATOR_CONFIRM_PASSWORD_FIELD)
        confirm_passwd_field.send_keys(passwd)

        submit_btn = self.find_element(PasswordResetLocators.LOCATOR_CHANGE_PASSWORD_BTN)
        submit_btn.click()

        complete_request_lbl = self.find_element(PasswordResetLocators.LOCATOR_REQUEST_COMPLETE_LBL)
        assert complete_request_lbl.text == "Password successfully changed!"

    def navigate_to_profile_page(self):
        open_profile_btn = self.find_element(PasswordResetLocators.LOCATOR_OPEN_PROFILE_BTN)
        open_profile_btn.click()


