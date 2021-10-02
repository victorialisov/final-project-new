from pages.main_page import MainPage
from pages.sign_up_start_page import SignUpStartPage
from pages.sign_up_continue_page import SignUpContinuePage
from pages.sign_up_final_page import SignUpFinalPage
from pages.passwd_reset_page import PasswordReset
from pages.profile_page import UserProfile
from temp_mail.temp_mail_api import TempUserEmail
from help_functions.mail_helper import get_link
from help_functions.random_generator import random_word_generator
import json
import time


def test_user_can_sign_in(browser):
    user_email = TempUserEmail()

    main_page = MainPage(browser)
    main_page.open_main_page()
    main_page.open_sign_in_page()

    sign_up_start_page = SignUpStartPage(browser)
    sign_up_start_page.should_be_sign_up_start_page()
    user_first_name = random_word_generator()
    user_second_name = random_word_generator()
    user_full_name = user_first_name + " " + user_second_name
    email_box = user_email.create_email_box()
    print("!!!!!" + email_box['email'])
    sign_up_start_page.start_sign_up(user_full_name, email_box['email'])

    sign_up_continue_page = SignUpContinuePage(browser)
    sign_up_continue_page.should_be_sign_up_continue_page()
    sign_up_continue_page.continue_sign_up()

    sign_up_final_page = SignUpFinalPage(browser)
    sign_up_final_page.should_be_sign_up_final_page()
    sign_up_final_page.final_sign_up()
    print("!!!!!" + email_box['key'])
    email_box_key = email_box['key']
    # sleep is needed for registration mail will be sent to user_email
    time.sleep(5)
    mail_list = user_email.get_mails_list(email_box_key)
    print("!!!!! mail_list: " + json.dumps(mail_list))
    sign_up_email_msg = user_email.get_mail_msg(mail_list[0]['id'], email_box_key)
    print("!!!!! email_msg: " + sign_up_email_msg)
    passwd_reset_link = get_link(sign_up_email_msg)
    sign_up_final_page.navigate_to_passwd_reset_page(passwd_reset_link)

    sign_up_final_page.navigate_to_passwd_reset_page(passwd_reset_link)
    passwd_reset_page = PasswordReset(browser)
    passwd_reset_page.should_be_password_reset_page()
    user_passwd = random_word_generator()
    print("!!!!! passwd: " + user_passwd)
    passwd_reset_page.password_reset(user_passwd)
    passwd_reset_page.navigate_to_profile_page()

    # user_profile_page = UserProfile(browser)
    # user_profile_page.should_be_user_profile_page(user_full_name)
