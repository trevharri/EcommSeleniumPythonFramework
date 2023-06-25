import pytest

from ssqatest.src.pages.MyAccountSignedIn import MyAccountSignedIn
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
import time
from ssqatest.src.helpers.generic_helpers import generate_random_email_and_password


@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    def test_register_valid_new_user(self):
        my_account_signed_out = MyAccountSignedOut(self.driver)
        my_account_signed_out.go_to_my_account()
        random_credentials = generate_random_email_and_password()
        my_account_signed_out.input_reg_email(random_credentials["email"])
        my_account_signed_out.input_reg_password('QwertyQwerty1234!@#$')
        my_account_signed_out.click_reg_button()

        my_account_signed_in = MyAccountSignedIn(self.driver)
        logout_link_text = my_account_signed_in.get_logout_link_text()
        assert logout_link_text == 'Log out'

        time.sleep(1)
