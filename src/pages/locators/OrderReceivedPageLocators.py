from selenium.webdriver.common.by import By


class OrderReceivedPageLocators:
    PAGE_MAIN_HEADER = (By.CLASS_NAME, "entry-title")
    ORDER_NUMBER = (By.CSS_SELECTOR, 'li.order strong')