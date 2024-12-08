import re
import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage

@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    
def test_successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.login_as("demouser", "abc123")
    expect(page.locator('h2')).to_have_text("Invoice List")
    expect(page).to_have_url(re.compile(r".*/account"))

def test_invalid_username_login(page: Page):
    login_page = LoginPage(page)
    login_page.login_as("Demouser", "abc123")
    expect(page.get_by_text('Wrong username or password')).to_be_visible()

def test_invalid_username_and_password_login(page: Page):
    login_page = LoginPage(page)
    login_page.login_as("demouser_", "xyz")
    expect(page.get_by_text('Wrong username or password')).to_be_visible()

def test_invalid_password_login(page: Page):
    login_page = LoginPage(page)
    login_page.login_as("demouser", "nananana")
    expect(page.get_by_text('Wrong username or password')).to_be_visible()

#This test will fail because credentials are valid
def test_invalid_credentials_login(page: Page):
    login_page = LoginPage(page)
    login_page.login_as("demouser", "abc123")
    expect(page.get_by_text('Wrong username or password')).to_be_visible()
