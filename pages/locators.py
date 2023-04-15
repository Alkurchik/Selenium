from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_BOX = (By.XPATH, '//*[@name="q"]')
    SEARCH_BUTTON = (By.NAME, 'btnK')
    RESULTS = (By.XPATH, '//div[@class="g"]')
    COOKIE_MSG = (By.XPATH, '//*[@id="L2AGLb"]/div')


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, '//*[@id="username"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]')


class GeneralControls:
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
