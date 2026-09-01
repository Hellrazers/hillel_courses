import os
import logging
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, expect

from models.LoginPage import LoginPage

load_dotenv()
@pytest.mark.parametrize("email, password, status",
                        [ ("asdasd@asd.", "asdasd@asd.", 'email_problem'),
                          ("asdasd@asd.com", "asdasd@asd.", 'wrong_email'),
                          (os.getenv("USER_LOGIN"), os.getenv("USER_PASSWORD"), 'succuss')
                          ])
def test_param_login(page: Page, email, password, status) -> None:
    email_str = email
    password_str = password
    page.goto("/")
    page.get_by_role("button", name="Sign In").click()
    element_email = page.get_by_label("Email")
    expect(element_email).to_be_editable()
    element_email.fill(email_str)

    page.get_by_label("Password").fill(password_str)
    if status != "email_problem":
        page.get_by_role("button", name="Login").click()

    if status == "email_problem":
        expect(page.locator('//div[@class="invalid-feedback"]/p')).to_have_text('Email is incorrect')
    elif status == "wrong_email":
        expect(page.locator('p[class="alert alert-danger"]')).to_have_text("Wrong email or password")
    elif status == 'succuss':
        (expect(page.locator('//div[@class="alert alert-success"]/p'))
         .to_have_text('You have been successfully logged in'))




@pytest.mark.parametrize("email, password, status",
                        [ ("asdasd@asd.", "asdasd@asd.", 'email_problem'),
                          ("asdasd@asd.com", "asdasd@asd.", 'wrong_email'),
                          (os.getenv("USER_LOGIN"), os.getenv("USER_PASSWORD"), 'succuss')
                          ])
def test_param_login_after_upd(page: Page, email, password, status) -> None:
    email_str = email
    password_str = password
    login_page = LoginPage(page)
    login_page.go_to()
    login_page.login_in_to_account(email_str, password_str, status)

    if status == "email_problem":
        expect(login_page.error_email_incr).to_have_text('Email is incorrect')
    elif status == "wrong_email":
        expect(login_page.error_wrong_email).to_have_text("Wrong email or password")
    elif status == 'succuss':
        (expect(login_page.notify_locator)
         .to_have_text('You have been successfully logged in'))


def test_auth_login(auth_ui):
    logger = logging.getLogger('TEST_BODY')
    logger.info('We validating that we logger success to account and check that notify is correct')
    expect(auth_ui.locator('//div[@class="alert alert-success"]/p')).to_have_text('You have been successfully logged in')