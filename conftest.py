import pytest
import os
import allure

import pytest_html
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
        raise Exception(f"Provided browser '{browser}' is not supported"
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


## for pytest-html report generation
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             is_frontend_test = True if 'init_driver' in item.fixturenames else False
#             if is_frontend_test:
#                 results_dir = os.environ.get("RESULTS_DIR")
#                 if not results_dir:
#                     raise Exception("Environment variable 'RESULTS_DIR' must be set.")
#                 screen_shot_path = os.path.join(results_dir, item.name + '.png')
#                 driver_fixture = item.funcargs['request']
#                 driver_fixture.cls.driver.save_screenshot(screen_shot_path)
#                 extra.append(pytest_html.extras.image(screen_shot_path))
#         report.extra = extra

# for allure report generation
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            is_frontend_test = True if 'init_driver' in item.fixturenames else False
            if is_frontend_test:
                results_dir = os.environ.get("RESULTS_DIR")
                if not results_dir:
                    raise Exception("Environment variable 'RESULTS_DIR' must be set.")
                screen_shot_path = os.path.join(results_dir, item.name + '.png')
                driver_fixture = item.funcargs['request']
                driver_fixture.cls.driver.save_screenshot(screen_shot_path)
                allure.attach(driver_fixture.cls.driver.get_screenshot_as_png(),
                              name='screenshot',
                              attachment_type=allure.attachment_type.PNG)
