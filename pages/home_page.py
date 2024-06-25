from playwright.sync_api import Page
from data.contants import BASE_URL
from pages.components.search_bar_component import SearchBarComponent
from pages.components.login_component import LoginComponent

class HomePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_bar = SearchBarComponent(page)
        self.login = LoginComponent(page)

    # Navigation
    def load(self):
        self.page.goto(f"{BASE_URL}/tienda/home")

    # Actions
    def search_article(self, text_to_search: str):
        self.search_bar.search(text_to_search)
