from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    FIRST_NAME_FIELD = (By.ID, 'billing_first_name')
    LAST_NAME_FIELD = (By.ID, 'billing_last_name')
    COUNTRY_DROPDOWN = (By.ID, 'billing_country')
    STREET_ADDRESS_FIELD = (By.ID, 'billing_address_1')
    CITY_FIELD = (By.ID, 'billing_city')
    STATE_DROPDOWN = (By.ID, 'billing_state')
    POST_CODE_FIELD = (By.ID, 'billing_postcode')
    PHONE_NUMBER_FIELD = (By.ID, 'billing_phone')
    EMAIL_FIELD = (By.ID, 'billing_email')
    PLACE_ORDER_BTN = (By.ID, 'place_order')
