from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpers.generic_helpers import generate_random_email_and_password
from ssqatest.src.pages.locators.CheckoutPageLocators import CheckoutPageLocators


class CheckoutPage(CheckoutPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def enter_first_name(self, first_name=None):
        first_name = first_name if first_name else "testFname"
        self.sl.wait_and_input_text(self.FIRST_NAME_FIELD, first_name)

    def enter_last_name(self, last_name=None):
        last_name = last_name if last_name else "testLname"
        self.sl.wait_and_input_text(self.LAST_NAME_FIELD, last_name)

    def select_country(self, country_val=None):
        country_val = country_val if country_val else "US"
        self.sl.wait_and_select_by_value(self.COUNTRY_DROPDOWN, country_val)

    def enter_street_address(self, street_address=None):
        street_address = street_address if street_address else "123 Main St."
        self.sl.wait_and_input_text(self.STREET_ADDRESS_FIELD, street_address)

    def enter_city(self, city=None):
        city = city if city else "Minneapolis"
        self.sl.wait_and_input_text(self.CITY_FIELD, city)

    def select_state(self, state_val=None):
        state_val = state_val if state_val else "MN"
        self.sl.wait_and_select_by_value(self.STATE_DROPDOWN, state_val)

    def enter_post_code(self, post_code=None):
        post_code = post_code if post_code else "55414"
        self.sl.wait_and_input_text(self.POST_CODE_FIELD, post_code)

    def enter_phone_number(self, phone_number=None):
        phone_number = phone_number if phone_number else "6126692842"
        self.sl.wait_and_input_text(self.PHONE_NUMBER_FIELD, phone_number)

    def enter_email(self, email=None):
        if not email:
            email = generate_random_email_and_password()["email"]
        self.sl.wait_and_input_text(self.EMAIL_FIELD, email)

    def place_order(self):
        self.sl.wait_and_click(self.PLACE_ORDER_BTN)

    def fill_in_billing_info(
            self,
            first_name=None,
            last_name=None,
            country_val=None,
            street_address=None,
            city=None,
            state_val=None,
            post_code=None,
            phone_number=None,
            email=None

    ):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.select_country(country_val)
        self.enter_street_address(street_address)
        self.enter_city(city)
        self.select_state(state_val)
        self.enter_post_code(post_code)
        self.enter_phone_number(phone_number)
        self.enter_email(email)

    def check_create_account_box(self):
        self.sl.wait_and_click(self.CREATE_ACC_CHECKBOX)

    def enter_account_password(self, password):
        self.sl.wait_and_input_text(self.ACC_PASSWORD_FIELD, password)
