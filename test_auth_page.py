import pytest
from .pages.main_page import MainPage

link = "http://dev.dentes.app"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()
        page.go_to_login_page()
