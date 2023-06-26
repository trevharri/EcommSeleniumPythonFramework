import pytest
import os
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium import webdriver


@pytest.fixture(scope="class")
def init_driver(request):
    supported_browsers = ['chrome', 'ch', 'headlesschrome', 'firefox', 'ff', 'headlessfirefox']

    browser = os.environ.get('BROWSER', 'ch')
    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set.")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception (f"Provided browser '{browser}' is not supported"
                         f"Supported options are f{supported_browsers}.")

    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome()
    elif browser in ('firefox', 'ff'):
        driver = webdriver.Firefox()
    elif browser == 'headlesschrome':
        chrome_options = ChOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == 'headlessfirefox':
        firefox_options = FFOptions()
        firefox_options.add_argument('--disable-gpu')
        firefox_options.add_argument('--no-sandbox')
        firefox_options.add_argument('--headless')
        driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()