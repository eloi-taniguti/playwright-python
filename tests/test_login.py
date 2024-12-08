import re
import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage

invalid_credentials = [
    {
        'username': 'Demouser',
        'password': 'abc123'
    },
    {
        'username': 'demouser_',
        'password': 'xyz'
    },
    {
        'username': 'demouser',
        'password': 'nanana'
    },
    {
        'username': 'demouser',
        'password': 'abc123'
    }
]

@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    
def test_TC001_successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.login_as("demouser", "abc123")
    expect(page.locator('h2')).to_have_text("Invoice List")
    expect(page).to_have_url(re.compile(r".*/account"))

#This test will fail because last credentials are valid
def test_TC002_invalid_credentials_login(page: Page):
    login_page = LoginPage(page)
    for user in invalid_credentials:
        login_page.login_as(user['username'], user['password'])
    expect(page.get_by_text('Wrong username or password')).to_be_visible()
