from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage


def test_user_can_login(browser):
    main_page = MainPage(browser)
    main_page.open_main_page()
    main_page.open_login_page()
    login_page = LoginPage(browser)
    login_page.should_be_login_page()
    # will be added api test for create user
    login_page.login("victoria.lisouskaya@gmail.com", "111222")
    account_page = AccountPage(browser)
    account_page.should_be_account_page()
