import requests
import json

from .errors import FalseResult

BASE_URL = "https://fortniteapi.io/"


class SyncRequest:
    def __init__(self):
        self.headers = {}

    def add_header(self, key, val):
        self.headers[key] = val

    def remove_header(self, key):
        return self.headers.pop(key)

    def get(self, endpoint: str, params: dict = None):
        response = requests.get(BASE_URL + endpoint, params=params, headers=self.headers)
        try:
            data = response.json()
        except json.JSONDecodeError:
            data = {'error': response.text}
        if response.status_code == 200:
            if data.get('result') is False:
                raise FalseResult(data.get('code', 'Unknown Error'))
            return data
