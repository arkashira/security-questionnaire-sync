import json
from typing import Any, Dict
import requests


class ApiClient:
    """Very thin wrapper around a remote JSON endpoint."""

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def get(self, path: str) -> Dict[str, Any]:
        resp = requests.get(f"{self.base_url}{path}")
        resp.raise_for_status()
        return resp.json()

    def post(self, path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        resp = requests.post(f"{self.base_url}{path}", json=payload)
        resp.raise_for_status()
        return resp.json()