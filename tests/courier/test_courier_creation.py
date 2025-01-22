from src.courier_api import CourierAPI

def test_create_courier(random_courier):
    response = CourierAPI.create_courier(**random_courier)
    assert response.status_code == 201
    assert response.json().get("ok") is True


def test_create_duplicate_courier(random_courier):
    CourierAPI.create_courier(**random_courier)
    response = CourierAPI.create_courier(**random_courier)
    assert response.status_code == 409