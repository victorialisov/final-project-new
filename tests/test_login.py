import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage


@allure.story("Check valid user can login")
def test_user_can_login(browser):
    with allure.step('Open login page'):
        main_page = MainPage(browser)
        main_page.open_main_page()
        main_page.open_login_page()
    with allure.step('Check login page displays'):
        login_page = LoginPage(browser)
        login_page.should_be_login_page()
    with allure.step('Login as a user "victoria.lisouskaya@gmail.com"'):
        login_page.login("victoria.lisouskaya@gmail.com", "111222")
    with allure.step('Check account page displays'):
        account_page = AccountPage(browser)
        account_page.should_be_account_page()
