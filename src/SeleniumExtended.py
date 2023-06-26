from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10

    def wait_and_get_elements(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).click()

    def wait_and_get_text(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        text = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).text

        return text

    def wait_for_visibility(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )
