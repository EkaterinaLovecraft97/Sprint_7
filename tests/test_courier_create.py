import requests
import allure
import pytest
from src.data import Data
from src.urls import Urls
from src.helpers import generate_login, generate_password, generate_first_name


class TestCourierCreate:

    @allure.title('Успешное создание курьера с корректными данными')
    @allure.description('Проверяем, что можно создать нового курьера с уникальными данными. Код ответа: 201.')
    def test_create_courier_account_success(self):
        payload = {
            'login': generate_login(),
            'password': generate_password(),
            'firstName': generate_first_name()
        }
        response = requests.post(Urls.URL_courier_create, data=payload)
        assert response.status_code == 201, "Ожидался код ответа 201, но получен другой."
        assert response.json() == {'ok': True}, "Тело ответа не соответствует ожидаемому формату."

    @allure.title('Ошибка при создании курьера с занятым логином')
    @allure.description('Проверяем, что нельзя зарегистрировать курьера с уже существующим логином. Код ответа: 409.')
    def test_create_courier_account_login_taken_conflict(self):
        payload = {
            'login': Data.valid_login,
            'password': generate_password(),
            'firstName': generate_first_name()
        }
        response = requests.post(Urls.URL_courier_create, data=payload)
        assert response.status_code == 409, "Ожидался код ответа 409, но получен другой."
        assert response.json() == {
            'code': 409,
            'message': 'Этот логин уже используется. Попробуйте другой.'
        }, "Сообщение об ошибке не совпадает с ожидаемым."

    @allure.title('Ошибка при создании курьера с пустыми обязательными полями')
    @allure.description('Тест проверяет невозможность создания курьера, если одно из обязательных полей пустое. Код ответа: 400.')
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': generate_password(), 'firstName': generate_first_name()},
        {'login': generate_login(), 'password': '', 'firstName': generate_first_name()}
    ])
    def test_create_courier_account_with_empty_required_fields(self, empty_credentials):
        response = requests.post(Urls.URL_courier_create, data=empty_credentials)
        assert response.status_code == 400, "Ожидался код ответа 400, но получен другой."
        assert response.json() == {
            'code': 400,
            'message': 'Недостаточно данных для создания учетной записи'
        }, "Сообщение об ошибке не совпадает с ожидаемым."
