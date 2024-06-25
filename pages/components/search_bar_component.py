from playwright.sync_api import Page

class SearchBarComponent:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_bar_lt = page.locator('div.input-group #mainSearchbar')


    # Actions
    def search(self, text_to_search: str):
        self.search_bar_lt.fill(text_to_search)
        self.search_bar_lt.press('Enter')

    # Results
    def result_search_bar_text(self):
        return self.search_bar_lt

    def result_search_page(self):
        return self.page


