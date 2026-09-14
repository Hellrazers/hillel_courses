#Автоматизація E2E UI-тесту створення автомобіля з ізоляцією
# тестових даних (API Teardown)
from playwright.sync_api import expect, Page

from models.CarPage import CarPage


#Опис (Description):

#Необхідно реалізувати ізольований автоматизований UI-тест
# для перевірки флоу створення нової сутності «Автомобіль» (Vehicle/Car)
# з гарантованим очищенням створених даних на рівні бекенду.


def test_add_car(auth_ui: Page, delete_car):
    page = auth_ui
    BRAND_NAME = "Ford"
    MODEL_NAME = "Focus"
    MILEAGE = '123'
    car: CarPage = CarPage(page)
    car.add_car_button.click()
    expect(car.modal_title).to_have_text('Add a car')
    car.fill_values(BRAND_NAME, MODEL_NAME, MILEAGE)
    with page.expect_response('**/api/cars') as response:
        car.modal_add_button.click()
        delete_car.append(response.value.json().get('data'))
    expect(car.notify_not_login_locator).to_have_text('Car added')
    resp_json = response.value.json().get('data')
    assert resp_json.get('brand') == BRAND_NAME
    assert resp_json.get('model') == MODEL_NAME
    assert resp_json.get('mileage') == int(MILEAGE)

#Car added