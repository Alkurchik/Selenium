from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
from .locators import MainPageLocators
config = configparser.ConfigParser()
config.read('config.ini')


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = config.get('Google', 'url')

    def go_to_url(self):
        self.driver.get(self.url)

    def search(self, query):
        search_box = self.driver.find_element(*MainPageLocators.SEARCH_BOX)
        self.driver.find_element(*MainPageLocators.COOKIE_MSG).click()
        # search_box.send_keys(query)
        search_button = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        # search_button.click()

    def get_results(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(MainPageLocators.RESULTS))
        return self.driver.find_elements(*MainPageLocators.RESULTS)
