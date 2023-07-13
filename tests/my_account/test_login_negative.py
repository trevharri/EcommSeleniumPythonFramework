import pytest

from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.helpers.logger_helper import get_logger


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:
    @pytest.mark.tcid12
    def test_login_non_existing_user(self):
        log = get_logger()
        my_account = MyAccountSignedOut(self.driver)
        user_name = "TestUser"
        password = "TestPassword1234*"
        expected_err_text = 'Error: The username TestUser is not registered on this site. If you are unsure of your ' \
                            'username, try your email address instead.'
        log.debug("Going to my account page.")
        my_account.go_to_my_account()
        log.info(f"Entering unregistered username/password ({user_name}/{password})")
        my_account.input_login_username(user_name)
        my_account.input_login_password(password)
        log.debug("Click login button")
        my_account.click_login_button()
        log.info(f"Asserting error message appears: {expected_err_text}")
        err_text = my_account.get_err_text()
        assert err_text == expected_err_text
