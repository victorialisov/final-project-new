from pages.base_page import BasePage
from locators.profile_page_locators import UserProfileLocators
import time


class UserProfile(BasePage):

    def should_be_user_profile_page(self, full_name: str):
        submit_btn = self.find_element(UserProfileLocators.LOCATOR_SUBMIT_BTN)
        submit_btn.click()

        user_name_lbl = self.find_element(UserProfileLocators.LOCATOR_USER_NAME_LBL)
        time.sleep(5)
        assert full_name in user_name_lbl.text

