from ssqatest.src.pages.locators.HeaderLocators import HeaderLocators
from ssqatest.src.pages.locators.HomePageLocators import HomePageLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpers.config_helpers import get_base_url


class Header(HeaderLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def click_on_nav_cart(self):
        self.sl.wait_and_click(self.CART_BTN)

    def wait_until_cart_item_count(self, count):
        if count == 1:
            expected_text = str(count) + ' item'
        else:
            expected_text = str(count) + ' items'
        self.sl.wait_until_element_contains_text(self.CART_ITEMS, expected_text)

