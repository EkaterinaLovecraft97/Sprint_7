import pytest
from src.utils import generate_random_string

@pytest.fixture
def random_courier():
    """Фикстура для генерации случайного курьера."""
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }

@pytest.fixture
def random_order():
    """Фикстура для генерации случайного заказа."""
    return {
        "color": ["BLACK", "GREY"]
    }