import time

import pytest
from playwright.sync_api import Page, expect

from models.LoginPage import LoginPage

@pytest.mark.smoke
def test_example(page: Page) -> None:
    EMAIL_STR, PASSWORD_STR = 'asdasd@asd.com', 'asdasd@asd.com'

    page.goto("/")
    login_page = LoginPage(page)
    expect(page.locator("section")).to_contain_text("With the help of the Hillel auto project, you will have the opportunity to get hands-on experience in manual testing.")
    page.get_by_role("button", name="About").click()
    expect(page.get_by_text("Keep track of your")).to_be_visible()
    login_page.login_in_to_account(EMAIL_STR, PASSWORD_STR)
    expect(page.locator('//p[@class="alert alert-danger"]')).to_have_text("Wrong email or password")

@pytest.mark.smoke
def test_example2(page: Page) -> None:
    page.goto("/")
    page.get_by_role("button", name="Sign In").click()
    element_email = page.get_by_label("Email")
    expect(element_email).to_be_editable()
    element_email.fill("asdasd@asd.com")
    element_email.dblclick(modifiers=['Shift'])
    page.keyboard.down('Delete')
    page.keyboard.up('Delete')

    time.sleep(5)
    page.get_by_label("Password").fill("asdasd@asd.com")


def test_drag_drop4(page: Page):
    page.goto("/")

    page_2 = page.context.new_page()
    page_2.goto('https://seleniumbase.io/other/drag_and_drop')
    # page.locator('div[id="div2"]').drag_to(page.locator('div[id="div1"]'))
    page_2.locator('div[id="div2"]').hover()
    page_2.mouse.down()
    page_2.locator('div[id="div1"]').hover()
    page_2.mouse.up()

    expect(page.locator("section")).to_contain_text("With the help of the Hillel auto project, you will have the opportunity to get hands-on experience in manual testing.")
    page.get_by_role("button", name="About").click()
    expect(page.get_by_text("Keep track of your")).to_be_visible()
    page.get_by_role("button", name="Sign In").click()
    page.get_by_label("Email").fill("asdasd@asd.com")
    page.get_by_label("Password").fill("asdasd@asd.com")
    page.get_by_role("button", name="Login").click()
    expect(page.locator('//p[@class="alert alert-danger"]')).to_have_text("Wrong email or password")

    page.goto('https://seleniumbase.io/other/drag_and_drop')
    # page.locator('div[id="div2"]').drag_to(page.locator('div[id="div1"]'))
    page.locator('div[id="div2"]').hover()
    page.mouse.down()
    page.locator('div[id="div1"]').hover()
    page.mouse.up()


def test_drag_drop3(page: Page):
    page.goto('https://seleniumbase.io/other/drag_and_drop')
    # page.locator('div[id="div2"]').drag_to(page.locator('div[id="div1"]'))
    page.locator('div[id="div2"]').hover()
    page.mouse.down()
    page.locator('div[id="div1"]').hover()
    page.mouse.up()
    time.sleep(5)

def test_checkbox(page: Page):
    page.goto("https://faculty.washington.edu/chudler/java/boxes.html")

    list_checkbox = page.locator('input[type="checkbox"]').all()

    for index, checkbox in enumerate(list_checkbox):
        if index % 2 == 0:
            checkbox.check()
    for index, checkbox in enumerate(list_checkbox):
        if index % 2 == 0:
            expect(checkbox).to_be_checked()
    for index, checkbox in enumerate(list_checkbox):
        if index % 2 == 0:
            checkbox.uncheck()
        if index % 2 != 0:
            checkbox.check()

    for index, checkbox in enumerate(list_checkbox):
        if index % 2 == 0:
            expect(checkbox).not_to_be_checked()
        if index % 2 != 0:
            expect(checkbox).to_be_checked()