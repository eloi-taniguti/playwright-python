from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    dev navigate(self):
        self.goto("https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/")
        expect(page.locator('h1')).to_have_text("Login")
