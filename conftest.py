import configparser
import pytest
import os
from datetime import datetime
import allure
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
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == 'firefox':
        service = GeckoService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    elif browser == 'firefox':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        raise Exception(f"{browser} is not supported")

    driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)

    return driver


def save_screenshot(driver, name):
    # Определяем путь к папке для скриншотов
    screenshot_dir = os.path.join(os.getcwd(), "screenshots")
    # Если папки не существует, то создаем ее
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    # Определяем имя файла скриншота на основе текущей даты и времени, названия тест-кейса и расширения файла
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_name = f"{name}_{now}.png"
    # Сохраняем скриншот
    driver.save_screenshot(os.path.join(screenshot_dir, screenshot_name))
    # Добавляем скриншот в отчет Allure
    allure.attach.file(os.path.join(screenshot_dir, screenshot_name), name="Screenshot", attachment_type=allure.attachment_type.PNG)


def expected_url(page):
    return f"{config.get('LOGIN_PAGE', 'url')}{config.get('URL_PART', 'app')}{config.get('PAGES', str(page))}"
