from selenium.webdriver.common.by import By


class CartPageLocators:

    COUPON_INPUT = (By.ID, 'coupon_code')
    APPLY_COUPON_BTN = (By.CSS_SELECTOR, "button[name='apply_coupon']")
    PRODUCT_NAMES = (By.CSS_SELECTOR, 'td.product-name')
    COUPON_ALERT = (By.CSS_SELECTOR, '.woocommerce-message')
    CHECKOUT_BTN = (By.CLASS_NAME, 'checkout-button')