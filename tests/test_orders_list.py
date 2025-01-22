import requests
import allure
import pytest
from src.urls import Urls


class TestOrdersListGet:

    @allure.title('Получение списка заказов')
    @allure.description(
        'Проверяем успешное получение списка заказов. '
        'Убеждаемся, что в теле ответа содержится массив заказов, и каждый заказ содержит поле "id". '
        'Код ответа должен быть 200.'
    )
    def test_orders_list_get_success(self):
        response = requests.get(Urls.URL_orders_create, timeout=500)

        # Проверка кода ответа
        assert response.status_code == 200, (
            f"Ожидался код ответа 200, но получен {response.status_code}. "
            f"Тело ответа: {response.text}"
        )

        # Проверка структуры ответа
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

        # Проверка, что каждый заказ содержит поле 'id'
        for order in orders:
            assert 'id' in order, (
                f"Один из заказов не содержит ключа 'id'. "
                f"Неправильный заказ: {order}"
            )
