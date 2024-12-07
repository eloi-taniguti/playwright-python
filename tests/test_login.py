import time
import re
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page):
        page.goto("https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/")
        expect(page.locator('h1')).to_have_text("Login")
    
def test_successful_login(page: Page):
    page.fill('input[name="username"]', "demouser")
    page.fill('input[name="password"]', "abc123")
    time.sleep(5)
    page.get_by_role("button", name="Login").click()
    expect(page.locator('h2')).to_have_text("Invoice List")
    time.sleep(5)
    expect(page).to_have_url(re.compile(r".*/account"))

def test_invalid_username_login(page: Page):
    page.fill('input[name="username"]', "Demouser")
    page.fill('input[name="password"]', "abc123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text('Wrong username or password')).to_be_visible()

def test_invalid_username_and_password_login(page: Page):
    page.fill('input[name="username"]', "demouser_")
    page.fill('input[name="password"]', "xyz")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text('Wrong username or password')).to_be_visible()

def test_invalid_password_login(page: Page):
    page.fill('input[name="username"]', "demouser")
    page.fill('input[name="password"]', "nananana")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text('Wrong username or password')).to_be_visible()

#This test will fail because credentials are valid
def test_invalid_credentials_login(page: Page):
    page.fill('input[name="username"]', "demouser")
    page.fill('input[name="password"]', "abc123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text('Wrong username or password')).to_be_visible()
