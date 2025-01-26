import requests
import allure
import pytest
from src.data import Data, ResponseJSON
from src.urls import Urls
from src.helpers import generate_login, generate_password, generate_first_name


class TestCourierCreate:

    @allure.title("Проверка успешного создания курьера")
    @allure.description("Создание шаблонного курьера, проверка статуса ответа и тела ответа")
    def test_create_courier_success(self, default_courier):
        create_courier_response = default_courier
        assert create_courier_response.status_code == 201, "Некорректный код ответа при создании курьера"
        assert create_courier_response.json()["ok"] == True, "В теле ответа отсутствует 'ok': true"

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
    @allure.description('Тест проверяет невозможность создания курьера, если одно из обязательных полей пустое. Код ответа: 400.')
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': generate_password(), 'firstName': generate_first_name()},
        {'login': generate_login(), 'password': '', 'firstName': generate_first_name()}
    ])
    def test_create_courier_account_with_empty_required_fields(self, empty_credentials):
        response = requests.post(Urls.URL_courier_create, json=empty_credentials)
        assert response.status_code == 400, "Ожидался код ответа 400, но получен другой."
        assert response.json() == ResponseJSON.Response_400_create_account, "Сообщение об ошибке не совпадает с ожидаемым."
