import pytest
import time

from ssqatest.src.pages.CheckoutPage import CheckoutPage
from ssqatest.src.pages.Header import Header
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.configs.generic_configs import GenericConfigs
from ssqatest.src.pages.OrderReceivedPage import OrderReceivedPage
from ssqatest.src.helpers.database_helpers import get_order_from_db_by_order_no, get_item_from_db_by_order_no


@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGuestUser:

    def test_end_to_end_checkout_guest_user(self):
        home_page = HomePage(self.driver)
        header = Header(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        order_received_page = OrderReceivedPage(self.driver)

        coupon_code = GenericConfigs.COUPON_CODE
        coupon_success_alert = GenericConfigs.COUPON_SUCCESS_ALERT

        home_page.go_to_home_page()
        chosen_product = home_page.add_random_product_to_cart()

        header.wait_until_cart_item_count(1)
        header.click_on_nav_cart()

        product_names = cart_page.get_all_product_names_in_cart()
        assert len(product_names) == 1, f"Expected one item in cart but found {len(product_names)}"
        cart_page.input_coupon_code(coupon_code)
        cart_page.click_apply_coupon()
        coupon_alert = cart_page.get_coupon_alert_text()
        assert coupon_alert == coupon_success_alert, "Unexpected message when applying coupon"
        cart_page.go_to_checkout()

        checkout_page.fill_in_billing_info()
        checkout_page.place_order()

        order_received_page.confirm_page_loaded()
        order_received_message = order_received_page.get_order_received_header()
        assert order_received_message == 'Order received'
        order_number = order_received_page.get_order_number()
        db_order = get_order_from_db_by_order_no(order_number)
        assert db_order, f"After creating order with FE, not found in DB"\
                         f"Order no: {order_number}"
        db_product = get_item_from_db_by_order_no(order_number)
        assert db_product == chosen_product, f"Product name ordered on FE doesn't match product name in DB"\
                                            f"Product name FE:{chosen_product}"

