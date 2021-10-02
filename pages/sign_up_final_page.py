from pages.base_page import BasePage
from locators.sign_up_locators import SignUpLocators


class SignUpFinalPage(BasePage):

    def should_be_sign_up_final_page(self):
        got_it_btn = self.find_element(SignUpLocators.LOCATOR_GOT_IT_BTN)
        assert got_it_btn.get_attribute("innerText") == "Check Your Email"

    def final_sign_up(self):
        got_it_btn = self.find_element(SignUpLocators.LOCATOR_GOT_IT_BTN)
        got_it_btn.click()

    def navigate_to_passwd_reset_page(self, url):
        self.driver.get(url)
