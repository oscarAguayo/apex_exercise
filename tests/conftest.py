import pytest
from pages.home_page import HomePage
from pages.result_search_page import ResultSearchPage
from playwright.sync_api import Page

@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture
def result_search_page(page: Page) -> ResultSearchPage:
    return ResultSearchPage(page)
