from src.order_api import OrderAPI

def test_create_order(random_order):
    response = OrderAPI.create_order(random_order)
    assert response.status_code == 201
    assert "track" in response.json()


def test_create_order_without_color():
    response = OrderAPI.create_order({})
    assert response.status_code == 201
    assert "track" in response.json()