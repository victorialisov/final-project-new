from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators


class AccountPage(BasePage):

    def should_be_account_page(self):
        account_navbar = self.find_element(AccountPageLocators.LOCATOR_ACCOUNT_NAVBAR)
