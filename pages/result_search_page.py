from playwright.sync_api import Page
from pages.components.search_bar_component import SearchBarComponent
from typing import List

class ResultSearchPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_bar = SearchBarComponent(page)
        self.empty_result = page.get_by_text('Lo sentimos, no encontramos nada para')
        self.grid_result = page.locator('div.o-listing__products')
        self.filter_options = page.locator('//aside//button[@class="a-title__filter"]//label')

    # Actions
    def search_article(self, text_to_search):
        self.search_bar.search(text_to_search)

    def get_filter_options(self) -> List[str]:
        self.filter_options.all_text_contents()

    # Results
    def result_search_empty(self):
        return self.empty_result

    def result_search_with_articles(self):
        return self.grid_result

    def result_get_filter_options(self):
        return self.filter_options.all_text_contents()

    def result_check_value_in_filter_options(self, value: str):
        filter_options = self.result_get_filter_options()
        if value in filter_options:
            return True
        return False