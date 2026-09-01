import os

import allure
import pytest
from dotenv import load_dotenv
from playwright.sync_api import expect

from contract.car_models import CarModels

load_dotenv()


@allure.epic('Епік логін')
@allure.story('Сторі логін')
@allure.title('Перевірка логіна')
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.smoke
def test_login(api_setup):
    payload = {
        'email': os.getenv('USER_LOGIN'),
        'password': os.getenv('USER_PASSWORD')
    }
    with allure.step('Відправка пост запита'):
        resp_login = api_setup.post(
            url='https://qauto.forstudy.space/api/auth/signin',
            data=payload
        )

        allure.attach(
            resp_login.text(),
            name='Response login',
            attachment_type=allure.attachment_type.JSON
        )
    expect(resp_login).to_be_ok()
    with allure.step('Ми валідуємо респонс запита'):
        assert resp_login.status == 200
        assert resp_login.json().get('data').get('userId') == 328924


def test_get_car_by_id(create_delete_car):
    api, resp_create_car = create_delete_car
    resp_get_car_by_id = api.get(
        url=f'/api/cars/{resp_create_car.get("id")}',
    )
    expect(resp_get_car_by_id).to_be_ok()
    resp_json_by_id = resp_get_car_by_id.json().get('data')
    assert resp_json_by_id.get('id') == resp_create_car.get('id')


def test_get_cars_200(api):
    resp_get_cars = api.get(
        url='/api/cars'
    )
    expect(resp_get_cars).to_be_ok()


@allure.epic('назва таски епіка')
@allure.story('назва сторі')
@allure.link(url='https:jira-epic/1', name='назва таски епіка')
@allure.link(url='https:jira-story/1')
@allure.severity(allure.severity_level.CRITICAL)
class TestCar:
    @allure.description('''
    Пре конд створює машину
    
    Тест 
    гетає цю машину по айді і валідує чи вона відповідає дійсності
    
    Пост конд
    видаляє цю машину
    ''')
    @allure.feature('назва фічі_1')
    @allure.title('Перевірка створенної машини')
    @pytest.mark.smoke
    def test_get_car_by_id_v2(self, create_delete_car_v2):
        api, resp_create_car = create_delete_car_v2
        car = CarModels(api)
        resp_get_car_by_id = car.get_car_by_id(
            item_id=resp_create_car.get("id"),
        )
        resp_json_by_id = resp_get_car_by_id.json().get('data')
        assert resp_json_by_id.get('id') == resp_create_car.get('id')

    @allure.feature('назва фічі_2')
    @allure.title('Веріфакіця не інсуючого айді для get by id car')
    @pytest.mark.smoke
    def test_get_car_by_id_negative_v2(self, create_delete_car_v2):
        '''
        Ми перевіряємо не існуючий айді машини і очікуємо, що повернется 404 помилка
        '''
        car = CarModels(create_delete_car_v2[0])
        resp_get_car_by_id = car.get_car_by_id(
            item_id='123123123123',
            status_code=404
        )
        resp_json_by_id = resp_get_car_by_id.json().get('data')

    @allure.title('Перевірка створення машини')
    @pytest.mark.smoke
    def test_create_cars_200(self, api):
        payload_create_car = {
            "carBrandId": 1,
            "carModelId": 1,
            "mileage": 122
        }
        resp_create_cars = api.post(
            url='/api/cars',
            data=payload_create_car
        )
        expect(resp_create_cars).to_be_ok()
        resp_data = resp_create_cars.json().get('data')
        assert resp_data.get('id') is not None
        assert resp_data.get('carBrandId') == payload_create_car.get('carBrandId')
        assert resp_data.get('carModelId') == payload_create_car.get('carModelId')
        assert resp_data.get('mileage') == payload_create_car.get('mileage')
