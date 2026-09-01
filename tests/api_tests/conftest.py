import os
import logging
import pytest
from playwright.sync_api import Playwright, Request, APIRequestContext, expect

from contract.car_models import CarModels

# @pytest.fixture
# def fixture_first():
#     return 1

logger = logging.getLogger('api')
@pytest.fixture()
def api_setup(playwright: Playwright):
    api = playwright.request.new_context(
        base_url=os.getenv('BASIC_URL'),
    )
    yield api

    api.dispose()

@pytest.fixture()
def api(api_setup: APIRequestContext):
    payload = {
        'email': os.getenv('USER_LOGIN'),
        'password': os.getenv('USER_PASSWORD')
    }
    logger.info(f'Sending request to /api/auth/signin' )
    resp_login = api_setup.post(
        url='https://qauto.forstudy.space/api/auth/signin',
        data=payload
    )
    expect(resp_login).to_be_ok()


    yield api_setup


@pytest.fixture()
def create_delete_car(api: APIRequestContext):
    payload_create_car = {
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 122
    }
    logger.info(f'Sending request to /api/cars with payload: {payload_create_car}')
    resp_create_cars = api.post(
        url='/api/cars',
        data=payload_create_car
    )
    logger.info(f'Response:{resp_create_cars.json()} and status code: {resp_create_cars.status}')

    expect(resp_create_cars).to_be_ok()
    yield api, resp_create_cars.json().get('data')
    logger.info(f'Sending request to /api/cars/{resp_create_cars.json().get('data').get('id')}')
    resp_delete = api.delete(
        url=f'/api/cars/{resp_create_cars.json().get('data').get('id')}',
        data=payload_create_car
    )
    logger.info(f'Response:{resp_delete.json()} and status code: {resp_delete.status}')
    expect(resp_delete).to_be_ok()


@pytest.fixture()
def create_delete_car_v2(api: APIRequestContext):
    car = CarModels(api)
    payload_create_car = {
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 122
    }
    resp_create_cars = car.post_car(data=payload_create_car)

    yield api, resp_create_cars.json().get('data')
    resp_delete = car.delete_car_by_id(item_id=resp_create_cars.json().get('data').get('id'))
