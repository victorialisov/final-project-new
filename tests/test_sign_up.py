from pages.main_page import MainPage
from pages.sign_up_start_page import SignUpStartPage
from pages.sign_up_continue_page import SignUpContinuePage
from pages.sign_up_final_page import SignUpFinalPage
from pages.account_page import AccountPage


def test_user_can_sign_in(browser):
    main_page = MainPage(browser)
    main_page.open_main_page()
    main_page.open_sign_in_page()
    sign_up_start_page = SignUpStartPage(browser)
   # sign_up_start_page.should_be_sign_up_start_page()
   # will be generate random name + email
    sign_up_start_page.start_sign_up("fxuuqqh fztqtsuutf", "txwruupt@hjok.tqy")
    sign_up_continue_page = SignUpContinuePage(browser)
    sign_up_continue_page.should_be_sign_up_continue_page()
    sign_up_continue_page.continue_sign_up()
    sign_up_final_page = SignUpFinalPage(browser)
    sign_up_final_page.should_be_sign_up_final_page()
    sign_up_final_page.final_sign_up()
    # account_page = AccountPage(browser)
    # account_page.should_be_account_page()
