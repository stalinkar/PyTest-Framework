# tests/api/test_api_example.py
import requests


def test_get_example(config):
    base_url = config["api"]["base_url"]
    response = requests.get(f"{base_url}/posts/1")
    assert response.status_code == 200
