from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.OrderReceivedPageLocators import OrderReceivedPageLocators


class OrderReceivedPage(OrderReceivedPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def confirm_page_loaded(self):
        self.sl.wait_until_url_contains('order-received')


    def get_order_received_header(self):
        return self.sl.wait_and_get_text(self.ORDER_RECEIVED_HEADER)