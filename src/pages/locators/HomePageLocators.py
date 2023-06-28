from selenium.webdriver.common.by import By

class HomePageLocators:
    PRODUCT_BTN = (By.LINK_TEXT, 'Add to cart')
    VIEW_CART_BTN = (By.LINK_TEXT, 'View cart')
    PRODUCT_CARDS = (By.CSS_SELECTOR, 'li.product-type-simple')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.woocommerce-loop-product__title')
