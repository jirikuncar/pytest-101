"""Implement FX client code."""

import requests


class FX(requests.Session):

    def __init__(self, base_url="http://localhost:8000"):
        super().__init__()
        self.base_url = base_url

    def convert(self, value, source, target):
        response = self.get(f"{self.base_url}/{source}/{target}/{value}")
        return float(response.content)
