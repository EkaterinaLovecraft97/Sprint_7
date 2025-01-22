import random
import string

def generate_random_string(length):
    """Генерирует случайную строку заданной длины."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def validate_response(response, expected_status_code):
    """Проверяет, что код ответа соответствует ожидаемому."""
    assert response.status_code == expected_status_code, f"Expected {expected_status_code}, got {response.status_code}"
    return response.json()