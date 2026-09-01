import pytest
import pytest_asyncio
from playwright.async_api import Page, expect, async_playwright

@pytest_asyncio.fixture()
async def async_page() -> Page:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        yield page, browser
        await browser.close()

    # page.locator('div[id="div2"]').drag_to(page.locator('div[id="div1"]'))



@pytest.mark.asyncio
async def test_example(async_page: Page) -> None:
    page, browser = async_page
    await page.goto("https://guest:welcome2qauto@qauto.forstudy.space")
    page_2 = await browser.new_page()
    await page_2.goto('https://seleniumbase.io/other/drag_and_drop')
    await page_2.locator('div[id="div2"]').hover()
    await page_2.locator('div[id="div2"]').hover()
    await page_2.mouse.down()
    await page_2.locator('div[id="div1"]').hover()
    await page_2.mouse.up()
    await expect(page.locator("section")).to_contain_text("With the help of the Hillel auto project, you will have the opportunity to get hands-on experience in manual testing.")
    await page.get_by_role("button", name="About").click()
    await expect(page.get_by_text("Keep track of your")).to_be_visible()
    await page.get_by_role("button", name="Sign In").click()
    await page.get_by_label("Email").fill("asdasd@asd.com")
    await page.get_by_label("Password").fill("asdasd@asd.com")
    await page.get_by_role("button", name="Login").click()
    await expect(page.locator('//p[@class="alert alert-danger"]')).to_have_text("Wrong email or password")
