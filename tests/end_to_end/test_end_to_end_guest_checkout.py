import pytest
import time

from ssqatest.src.pages.Header import Header
from ssqatest.src.pages.HomePage import HomePage


@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGuestUser:

    def test_end_to_end_checkout_guest_user(self):
        home_page = HomePage(self.driver)
        coupon_code = 'ssqa100'
        # navigate to home page
        home_page.go_to_home_page()
        # add item to carts
        home_page.add_random_product_to_cart()
        # go to cart
        header = Header(self.driver)
        header.wait_until_cart_item_count(1)
        header.click_on_nav_cart()
        time.sleep(2)
        # apply coupon code
        # proceed to checkout
        # enter shipping details
        # place oder
        # confirm Order Received
        # confirm order in db
