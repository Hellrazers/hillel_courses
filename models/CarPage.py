from playwright.sync_api import Page

from models.BasePage import BasePage


class CarPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.add_car_button = page.locator('//button[@class="btn btn-primary"]')
        self.modal_title = page.locator('.modal-title')
        self.modal_brand_selector = page.locator('#addCarBrand')
        self.modal_model_selector = page.locator('#addCarModel')
        self.modal_mileage_input = page.locator('#addCarMileage')
        self.modal_add_button = page.locator('//div[@class="modal-content"]//button[@class="btn btn-primary"]')


    def fill_values(self, brand_name: str, model_name: str, mileage: str | int):

        self.modal_brand_selector.select_option(brand_name)
        self.modal_model_selector.select_option(model_name)
        self.modal_mileage_input.fill(mileage)
        return self