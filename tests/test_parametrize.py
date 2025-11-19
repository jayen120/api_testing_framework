import pytest
import requests

@pytest.mark.parametrize("endpoint", [
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/comments",
    "https://jsonplaceholder.typicode.com/albums"
])
def test_api_endpoints(endpoint):
    response = requests.get(endpoint)
    assert response.status_code == 200
