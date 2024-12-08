from playwright.sync_api import Page, Locator, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_title: Locator = page.locator('h1')
        self.username_input: Locator = page.locator('input[name="username"]')
        self.password_input: Locator = page.locator('input[name="password"]')
        self.login_button: Locator = page.get_by_role("button", name="Login")

    def navigate(self):
        self.page.goto("https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/")
        expect(self.login_title).to_have_text("Login")

    def login_as(self, username: str, psw: str):
        self.username_input.fill(username)
        self.password_input.fill(psw)
        self.login_button.click()
