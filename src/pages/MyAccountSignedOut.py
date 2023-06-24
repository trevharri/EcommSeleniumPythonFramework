from ssqatest.src.pages.locators.MyAccountSignedOutLocators import MyAccountSignedOutLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpers.config_helpers import get_base_url


class MyAccountSignedOut(MyAccountSignedOutLocators):
    base_url = get_base_url()
    url = f"{base_url}/my-account/"

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        self.driver.get(MyAccountSignedOut.url)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USERNAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_login_button(self):
        self.sl.wait_and_click(self.LOGIN_BTN)

    def get_err_text(self):
        return self.sl.wait_and_get_text(self.ALERT_LI)



