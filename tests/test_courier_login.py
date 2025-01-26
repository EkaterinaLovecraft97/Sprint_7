import requests
import allure
import pytest
from src.data import Data, ResponseJSON
from src.urls import Urls
from src.helpers import generate_login, generate_password


class TestCourierLogin:

    @allure.title('Успешная аутентификация курьера с корректными данными')
    @allure.description('Проверяем, что курьер может успешно войти в систему, используя валидные данные. Код ответа: 200.')
    def test_courier_login_success(self):
        response = requests.post(Urls.URL_courier_login, data=Data.valid_courier_data)
        assert response.status_code == 200, "Ожидался код ответа 200, но получен другой."
        assert 'id' in response.text, "Тело ответа не содержит поле 'id', необходимое для успешной аутентификации."

    @allure.title('Ошибка аутентификации с неверными данными')
    @allure.description('Проверяем невозможность входа в систему при использовании несуществующего логина или неправильного пароля. Код ответа: 404.')
    @pytest.mark.parametrize('nonexistent_credentials', [
        {'login': generate_login(), 'password': generate_password()},
        Data.courier_data_with_wrong_password
    ])
    def test_courier_login_nonexistent_data_not_found(self, nonexistent_credentials):
        response = requests.post(Urls.URL_courier_login, data=nonexistent_credentials)
        assert response.status_code == 404, "Ожидался код ответа 404, но получен другой."
        assert response.json() == ResponseJSON.Response_404_account, "Сообщение об ошибке в ответе не совпадает с ожидаемым."

    @allure.title('Ошибка аутентификации с пустым логином или паролем')
    @allure.description('Проверяем, что при отсутствии логина или пароля система возвращает ошибку. Код ответа: 400.')
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': generate_password()},
        {'login': Data.valid_login, 'password': ''}
    ])
    def test_courier_login_empty_credentials_bad_request(self, empty_credentials):
        response = requests.post(Urls.URL_courier_login, data=empty_credentials)
        assert response.status_code == 400, "Ожидался код ответа 400, но получен другой."
        assert response.json() == ResponseJSON.Response_400_login, "Сообщение об ошибке в ответе не совпадает с ожидаемым."
