import allure
from ..pages.login_page import LoginPage
from ..conftest import save_screenshot, expected_url
import configparser
config = configparser.ConfigParser()
config.read('config.ini')


@allure.feature('Login')
@allure.story('Test Login - Success path')
def test_login_page(driver):
    main_page = LoginPage(driver)
    main_page.authorization()
    save_screenshot(driver, "login page")
    assert driver.current_url == expected_url('dashboard'), f"Unexpected url"
