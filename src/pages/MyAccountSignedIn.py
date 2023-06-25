from ssqatest.src.pages.locators.MyAccountSignedInLocators import MyAccountSignedInLocators
from ssqatest.src.pages.locators.MyAccountSignedOutLocators import MyAccountSignedOutLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended


class MyAccountSignedIn(MyAccountSignedInLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def get_logout_link_text(self):
        return self.sl.wait_and_get_text(self.LEFT_NAV_LOGOUT_LINK)

