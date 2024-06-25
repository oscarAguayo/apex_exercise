import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.result_search_page import ResultSearchPage

def test_search_a_common_article(home_page: HomePage, result_search_page: ResultSearchPage) -> None:
    """
    Test Case: TC01 Search a common article
    Acceptance criteria: Get products related to the search
    """
    # Test Data
    text_to_search = 'laptop'
    # Test Actions
    home_page.load()
    expect(home_page.search_bar.search_bar_lt).to_be_visible()
    home_page.search_article(text_to_search)
    expect(result_search_page.search_bar.result_search_bar_text()).to_have_value(text_to_search)
    expect(result_search_page.result_search_with_articles()).to_be_visible()

def test_search_with_no_articles_founded(home_page: HomePage, result_search_page: ResultSearchPage) -> None:
    """
    Test Case: TC02 Search with no articles founded
    Acceptance criteria: Be notified if there are no articles
    """
    # Test Data
    text_to_search = 'asdfghjklñ'
    # Test Actions
    home_page.load()
    expect(home_page.search_bar.search_bar_lt).to_be_visible()
    home_page.search_article(text_to_search)
    expect(result_search_page.search_bar.result_search_bar_text()).to_have_value(text_to_search)
    expect(result_search_page.result_search_empty().first).to_be_visible()

def test_filter_articles_by_brand_size_and_price(home_page: HomePage, result_search_page: ResultSearchPage) -> None:
    """
    Test Case: TC04 Filter articles by brand, size and range of price
    Acceptance criteria: Filter has the texts: "Marcas", "Tamaño", "Precios"
    """
    # Test Data
    text_to_search = 'Smart TV'
    # Test Actions
    home_page.load()
    expect(home_page.search_bar.search_bar_lt).to_be_visible()
    home_page.search_article(text_to_search)
    expect(result_search_page.search_bar.result_search_bar_text()).to_have_value(text_to_search)
    expect(result_search_page.result_search_with_articles()).to_be_visible()
    assert result_search_page.result_check_value_in_filter_options("Marcas")
    assert result_search_page.result_check_value_in_filter_options("Tamaño")
    assert result_search_page.result_check_value_in_filter_options("Precios")

@pytest.mark.skip(reason=" I don't have the capability to know when the promotion notification will be trigger")
def test_receive_promotion_notification(home_page: HomePage):
    """
    Test Case: TC05 Receive a promotion notification for a product or an  event
    Acceptance criteria: Receive a promotion notification
    """
    pass

@pytest.mark.xfail()
def test_is_user_logged(home_page: HomePage):
    """
    Test Case: 06 Be logged as a consumer
    Acceptance criteria: No "Iniciar sesión" text visible
    """
    home_page.load()
    assert home_page.login.result_login_text() != "Iniciar sesión"
