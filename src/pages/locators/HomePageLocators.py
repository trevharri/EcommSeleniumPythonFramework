from selenium.webdriver.common.by import By

class HomePageLocators:
    PRODUCT_BTNS = (By.CSS_SELECTOR, 'a.product_type_simple')
    VIEW_CART_BTN = (By.LINK_TEXT, 'View cart')