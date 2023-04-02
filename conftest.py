import configparser
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as GeckoService


config = configparser.ConfigParser()
config.read('config.ini')


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name (e.g. chrome, firefox)")


@pytest.fixture(scope='function')
def driver(request):
    if config.get('Google', 'browser') == 'chrome':
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif config.get('Google', 'browser') == 'firefox':
        service = GeckoService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    elif config.get('Google', 'browser') == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        raise ValueError(f'Unsupported browser: {config.get("Google", "browser")}')

    driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)

    return driver
