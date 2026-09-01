import allure
from playwright.sync_api import APIRequestContext

from contract.preparing import logger_api


class CarModels:

    def __init__(self, api: APIRequestContext):
        self.api = api
        self.path = '/api/cars'

    @allure.step('Гет всіх машин')
    @logger_api
    def get_all_cars(self, status_code: int = 200, **kwargs):
        resp = self.api.get(url=self.path, **kwargs)
        assert resp.status == status_code
        return resp

    @logger_api
    def get_car_by_id(self, item_id, status_code: int = 200, **kwargs):
        with allure.step(f'гет машини по айді: {item_id}'):
            resp = self.api.get(url=f'{self.path}/{item_id}', **kwargs)
            assert resp.status == status_code
            return resp

    @allure.step('Створення машини')
    @logger_api
    def post_car(self, status_code: int = 201, **kwargs):
        resp = self.api.post(url=f'{self.path}', **kwargs)
        assert resp.status == status_code
        return resp

    @logger_api
    def delete_car_by_id(self, item_id, status_code: int = 200, **kwargs):
        with allure.step(f'видалення машини по айді: {item_id}'):
            resp = self.api.delete(url=f'{self.path}/{item_id}', **kwargs)
            assert resp.status == status_code
            return resp
