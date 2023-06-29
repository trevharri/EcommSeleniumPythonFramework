import pytest

from ssqatest.src.pages.MyAccountSignedIn import MyAccountSignedIn
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.helpers.generic_helpers import generate_random_email_and_password
from ssqatest.src.helpers.logger_helper import get_logger


@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.tcid13
    def test_register_valid_new_user(self):
        log = get_logger()
        my_account_signed_out = MyAccountSignedOut(self.driver)
        my_account_signed_in = MyAccountSignedIn(self.driver)
        random_credentials = generate_random_email_and_password()
        password = "QwertyQwerty1234!@#$"

        log.debug("Going to my account page")
        my_account_signed_out.go_to_my_account()
        log.info(f'Generating/inputting email: {random_credentials["email"]} and password: {password} ')
        my_account_signed_out.input_reg_email(random_credentials["email"])
        my_account_signed_out.input_reg_password(password)
        log.debug("Clicking register button")
        my_account_signed_out.click_reg_button()
        log.info("Asserting Log out button present on new page")
        logout_link_text = my_account_signed_in.get_logout_link_text()
        assert logout_link_text == 'Log out'