import requests
import allure
import pytest
from src.data import Data, ResponseJSON
from src.urls import Urls
from src.helpers import generate_login, generate_password, generate_first_name


@pytest.fixture
def delete_courier():
    courier_ids = []

    def _delete(courier_id):
        if courier_id:
            delete_response = requests.delete(f"{Urls.URL_courier_create}/{courier_id}")
            assert delete_response.status_code == 200, f"Не удалось удалить курьера с id {courier_id}."

    yield courier_ids.append

    for courier_id in courier_ids:
        _delete(courier_id)


class TestCourierCreate:

    @allure.title('Успешное создание курьера с корректными данными')
    @allure.description('Проверяем, что можно создать нового курьера с уникальными данными. Код ответа: 201.')
    def test_create_courier_account_success(self, delete_courier):
        courier_data = {
            'login': generate_login(),
            'password': generate_password(),
            'firstName': generate_first_name()
        }
        response = requests.post(Urls.URL_courier_create, json=courier_data)
        assert response.status_code == 201, "Ожидался код ответа 201, но получен другой."
        response_body = response.json()
        assert response_body == {'ok': True}, "Тело ответа не соответствует ожидаемому формату."

        login_payload = {'login': courier_data['login'], 'password': courier_data['password']}
        login_response = requests.post(Urls.URL_courier_login, json=login_payload)
        assert login_response.status_code == 200, "Не удалось авторизоваться созданным курьером."
        courier_id = login_response.json().get('id')
        assert courier_id is not None, "Идентификатор курьера не был возвращен при авторизации."
        delete_courier(courier_id)

    @allure.title('Ошибка при создании курьера с занятым логином')
    @allure.description('Проверяем, что нельзя зарегистрировать курьера с уже существующим логином. Код ответа: 409.')
    def test_create_courier_account_login_taken_conflict(self):
        payload = {
            'login': Data.valid_login,
            'password': generate_password(),
            'firstName': generate_first_name()
        }
        response = requests.post(Urls.URL_courier_create, json=payload)
        assert response.status_code == 409, "Ожидался код ответа 409, но получен другой."
        assert response.json() == ResponseJSON.Response_409_create_account, "Сообщение об ошибке не совпадает с ожидаемым."

    @allure.title('Ошибка при создании курьера с пустыми обязательными полями')
    @allure.description(
        'Тест проверяет невозможность создания курьера, если одно из обязательных полей пустое. Код ответа: 400.')
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': generate_password(), 'firstName': generate_first_name()},
        {'login': generate_login(), 'password': '', 'firstName': generate_first_name()}
    ])
    def test_create_courier_account_with_empty_required_fields(self, empty_credentials):
        response = requests.post(Urls.URL_courier_create, json=empty_credentials)
        assert response.status_code == 400, "Ожидался код ответа 400, но получен другой."
        assert response.json() == ResponseJSON.Response_400_create_account, "Сообщение об ошибке не совпадает с ожидаемым."
