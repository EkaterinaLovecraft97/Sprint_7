import requests
import allure
from src.urls import Urls
from src.helpers import validate_orders_structure


class TestOrdersListGet:

    @allure.title('Получение списка заказов')
    @allure.description(
        'Проверяем успешное получение списка заказов. '
        'Убеждаемся, что в теле ответа содержится массив заказов, и каждый заказ содержит поле "id". '
        'Код ответа должен быть 200.'
    )
    def test_orders_list_get_success(self):
        response = requests.get(Urls.URL_orders_create, timeout=500)
        assert response.status_code == 200, (
            f"Ожидался код ответа 200, но получен {response.status_code}. "
            f"Тело ответа: {response.text}"
        )
        response_json = response.json()
        assert 'orders' in response_json, (
            "В теле ответа отсутствует ключ 'orders'. "
            f"Тело ответа: {response.text}"
        )
        orders = response_json['orders']
        assert isinstance(orders, list), (
            f"Ожидалось, что 'orders' будет списком, но получено: {type(orders).__name__}. "
            f"Тело ответа: {response.text}"
        )
        validate_orders_structure(orders)
