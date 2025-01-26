import requests
import pytest
import allure
from src.helpers import new_courier_login_password
from src.urls import Urls


@pytest.fixture(scope='function')
@allure.step("Создание шаблонного курьера")
def default_courier():
    body = new_courier_login_password()

    courier_response = requests.post(Urls.URL_courier_create, json=body)
    assert courier_response.status_code == 201, "Ошибка при создании курьера. Ожидался статус 201."

    login_body = body.copy()
    login_body.pop("firstName", None)
    login_response = requests.post(Urls.URL_courier_login, json=login_body)
    assert login_response.status_code == 200, "Ошибка авторизации курьера. Ожидался статус 200."

    id_courier = login_response.json().get("id")
    assert id_courier, "Не удалось получить ID созданного курьера."

    def teardown():
        delete_response = requests.delete(Urls.URL_courier_delete + str(id_courier))
        assert delete_response.status_code == 200, f"Не удалось удалить курьера с ID {id_courier}."

    pytest.fixture.teardown_call = teardown

    return courier_response



