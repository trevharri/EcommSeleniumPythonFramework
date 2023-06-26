from ssqatest.src.pages.locators.HomePageLocators import HomePageLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpers.config_helpers import get_base_url
import random


class HomePage(HomePageLocators):
    home_url = get_base_url()

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_home_page(self):
        self.driver.get(HomePage.home_url)

    def add_random_product_to_cart(self):
        products = self.sl.wait_and_get_elements(self.PRODUCT_BTNS)
        product = random.choice(products)
        product.click()
