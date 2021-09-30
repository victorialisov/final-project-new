from pages.base_page import BasePage
from locators.sign_up_locators import SignUpLocators


class SignUpStartPage(BasePage):
    def should_be_sign_up_start_page(self):
        start_sign_up_header = self.find_element(SignUpLocators.LOCATOR_START_SIGN_UP_HEADER)
        assert start_sign_up_header.text == "EventSource Sign up"

    def start_sign_up(self, full_name: str, email: str):
        full_name_field = self.find_element(SignUpLocators.LOCATOR_FULL_NAME_FIELD)
        full_name_field.send_keys(full_name)

        email_field = self.find_element(SignUpLocators.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(email)

        continue_btn = self.find_element(SignUpLocators.LOCATOR_CONTINUE_BTN)
        continue_btn.click()
