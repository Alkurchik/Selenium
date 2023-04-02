from .pages.main_page import MainPage
import allure


@allure.feature('Search')
@allure.story('Test search results')
def test_search_results(driver):
    main_page = MainPage(driver)
    main_page.go_to_url()
    main_page.search('Selenium')

