from playwright.async_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.notify_locator = page.locator('//div[@class="alert alert-success"]/p')
        self.notify_not_login_locator = page.locator('//div[@class="alert-list"]')

    def go_to(self, url):
        self.page.goto(url)
