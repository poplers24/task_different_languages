import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose driver: chrome  or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en, ...")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {"intl.accept_languages": user_language})
        print("\nstart chrome browser for test..")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        driver = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsegeError("--browser_name should be chrome or firefox")
    yield driver
    time.sleep(15)
    print("\nquit browser..")
    driver.quit()

