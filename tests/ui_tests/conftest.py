import os
import logging
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, expect

from models.LoginPage import LoginPage

load_dotenv()

logger = logging.getLogger('UI_LOGGER')


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "http_credentials":{
            "username": os.getenv('BASIC_AUTH_USER'),
            "password": os.getenv('BASIC_AUTH_PASS')
        },
        "base_url": os.getenv('BASIC_URL'),
    }

@pytest.fixture()
def auth_ui(page: Page) -> Page:
    email_str = os.getenv("USER_LOGIN")
    password_str = os.getenv("USER_PASSWORD")
    login_page = LoginPage(page)
    login_page.go_to()
    login_page.login_in_to_account(email_str, password_str)
    expect(login_page.notify_locator).to_have_text('You have been successfully logged in')
    yield page