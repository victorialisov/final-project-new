from pages.base_page import BasePage
from locators.sign_up_locators import SignUpLocators


class SignUpContinuePage(BasePage):

    def should_be_sign_up_continue_page(self):
        continue_sign_up_header = self.find_element(SignUpLocators.LOCATOR_CONTINUE_SIGN_UP_HEADER)
        assert continue_sign_up_header.text == "Stay Super Organized!"

    def continue_sign_up(self):
        submit_btn = self.find_element(SignUpLocators.LOCATOR_SUBMIT_BTN)
        submit_btn.click()
