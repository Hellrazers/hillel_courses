import time

from playwright.sync_api import Page, expect


def test_iframe(page: Page) -> None:
    page.goto('https://seleniumbase.io/w3schools/iframes')
    iframe_text = page.frame_locator('iframe#iframeResult')
    text_h2 = iframe_text.locator('body[contenteditable="false"] h2')

    expect(text_h2).to_have_text('HTML Iframes (nested iframes)')
    expect(page.locator('#framesize')).to_have_text('Result Size: 945 x 1011')
    use_css = iframe_text.locator('body[contenteditable="false"] p')
    expect(use_css).to_have_text('Use CSS width & height to specify the iframe size:')


def dialog_accept(dialog):
    dialog.accept()
    print(dialog.message)

def test_popup(page: Page) -> None:

    page.goto('https://testpages.eviltester.com/pages/basics/alerts-javascript/')
    page.on("dialog", dialog_accept)
    page.locator("#alertexamples").click()


def test_popup_accept(page: Page) -> None:

    page.goto('https://testpages.eviltester.com/pages/basics/alerts-javascript/')
    page.on("dialog", lambda dialog: dialog.accept())
    page.locator("#confirmexample").click()
    expect(page.locator('#confirmreturn')).to_have_text('true')

def test_popup_dismiss(page: Page) -> None:

    page.goto('https://testpages.eviltester.com/pages/basics/alerts-javascript/')
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.locator("#confirmexample").click()
    expect(page.locator('#confirmreturn')).to_have_text('false')
    time.sleep(5)

def test_page_works(page: Page) -> None:
    page.goto('https://testpages.eviltester.com/pages/basics/alerts-javascript/')
    page1 = page.context.new_page()
    page1.goto('https://playwright.dev/python/docs/pages')
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.locator("#confirmexample").click()
    expect(page.locator('#confirmreturn')).to_have_text('false')
    time.sleep(5)