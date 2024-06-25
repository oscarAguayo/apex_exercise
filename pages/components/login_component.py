from playwright.sync_api import Page

class LoginComponent:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.login = page.locator('//span[@class="a-header__topLink"]')

    # Results
    def result_login_text(self):
        return self.login.text_content()