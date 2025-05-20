import requests
import pytest

def test_delete_post():
    response = requests.delete("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code in [200, 204]
    assert response.text.strip() == "{}"