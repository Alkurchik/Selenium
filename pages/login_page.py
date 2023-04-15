from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
from .locators import MainPageLocators, LoginPageLocators, GeneralControls
config = configparser.ConfigParser()
config.read('config.ini')


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = config.get('LOGIN_PAGE', 'url')

    def authorization(self):
        self.driver.get(f'{self.url}/login')
        self.driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(config.get('CREDENTIALS', 'admin_email'))
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(config.get('CREDENTIALS', 'admin_password'))
        self.driver.find_element(*GeneralControls.SUBMIT_BUTTON).click()

    def get_results(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(MainPageLocators.RESULTS))
        return self.driver.find_elements(*MainPageLocators.RESULTS)
