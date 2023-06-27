from ssqatest.src.pages.locators.CartPageLocators import CartPageLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpers.config_helpers import get_base_url


class CartPage(CartPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def get_all_product_names_in_cart(self):
        products = self.sl.wait_and_get_elements(self.PRODUCT_NAMES)
        return [product.text for product in products]

    def input_coupon_code(self, code):
        self.sl.wait_and_input_text(self.COUPON_INPUT, code)

    def click_apply_coupon(self):
        self.sl.wait_and_click(self.APPLY_COUPON_BTN)

    def get_coupon_alert_text(self):
        return self.sl.wait_and_get_text(self.COUPON_ALERT)

    def go_to_checkout(self):
        self.sl.wait_and_click(self.CHECKOUT_BTN)

