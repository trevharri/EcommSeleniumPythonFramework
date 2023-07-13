from selenium.webdriver.common.by import By


class HeaderLocators:
    CART_BTN = (By.CSS_SELECTOR, '.page-item-7')
    CART_ITEMS = (By.CSS_SELECTOR, 'ul#site-header-cart span.count')
    MY_ACCOUNT = (By.LINK_TEXT, 'My account')
