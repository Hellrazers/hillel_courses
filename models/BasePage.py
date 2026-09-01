from playwright.async_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.notify_locator = page.locator('//div[@class="alert alert-success"]/p')

    def go_to(self, url):
        self.page.goto(url)
