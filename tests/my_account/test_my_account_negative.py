import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    def test_login_non_existing_user(self):
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username("TestUser")
        my_account.input_login_password("TestPassword1234*")
        my_account.click_login_button()
        err_text = my_account.get_err_text()
        expected_err_text = 'Errror: The username TestUser is not registered on this site. If you are unsure of your ' \
                              'username, try your email address instead.'
        assert err_text == expected_err_text


