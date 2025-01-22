import requests
from src.urls import ORDER_URL, ORDER_TRACK_URL

class OrderAPI:
    @staticmethod
    def create_order(payload):
        return requests.post(ORDER_URL, json=payload)

    @staticmethod
    def get_orders():
        return requests.get(ORDER_URL)

    @staticmethod
    def get_order_by_track(track_id):
        return requests.get(f"{ORDER_TRACK_URL}?t={track_id}")
