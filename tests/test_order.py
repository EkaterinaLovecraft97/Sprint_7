import requests
import allure
import pytest
import json
from src.data import OrderData
from src.urls import Urls


class TestOrderCreate:

    @allure.title('Создание заказа с различными параметрами цвета самоката')
    @allure.description(
        'Проверяем, что система позволяет указать один цвет самоката, выбрать сразу оба или не указывать цвет вовсе. '
        'Тест выполняется с разными наборами данных: только серый, только черный, оба цвета или без цвета. '
        'Проверяются код ответа и наличие трека в теле ответа.'
    )
    @pytest.mark.parametrize('order_data', [
        OrderData.order_data_single_color_1,
        OrderData.order_data_single_color_2,
        OrderData.order_data_multi_color,
        OrderData.order_data_no_colors
    ])
    def test_order_create_with_color_parameters(self, order_data):
        order_payload = json.dumps(order_data)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            Urls.URL_orders_create,
            data=order_payload,
            headers=headers,
            timeout=5
        )

        # Проверка кода ответа
        assert response.status_code == 201, (
            f"Ожидался код ответа 201, но получен {response.status_code}. "
            f"Тело ответа: {response.text}"
        )
        # Проверка наличия трека в ответе
        assert 'track' in response.text, (
            "Поле 'track' отсутствует в теле ответа. "
            f"Тело ответа: {response.text}"
        )
