from selenium.webdriver.common.by import By


class MyAccountSignedOutLocators:
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[name='login']")
    ALERT_LI = (By.CSS_SELECTOR, ".woocommerce-error li")
