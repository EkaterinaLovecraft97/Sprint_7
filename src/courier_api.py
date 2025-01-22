import requests
from src.urls import COURIER_URL
from src.utils import generate_random_string

class CourierAPI:
    @staticmethod
    def create_courier(login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return requests.post(COURIER_URL, json=payload)

    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f"{COURIER_URL}/{courier_id}")

    @staticmethod
    def login_courier(login, password):
        payload = {
            "login": login,
            "password": password
        }
        return requests.post(f"{COURIER_URL}/login", json=payload)
