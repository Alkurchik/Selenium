from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


class BasePage:

    browser: RemoteWebDriver

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        return self.browser.get(self.url)

    def go_to_login_page(self):
        # link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        # link.click()
        pass
