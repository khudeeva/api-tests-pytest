import requests
import pytest

def test_patch_post():
    new_name ={
        "name" : "Ksenia the QA"
    }
    response = requests.patch("https://jsonplaceholder.typicode.com/users/1", json = new_name)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == new_name["name"]
    assert "email" in data
    assert "address" in data
    assert "phone" in data
    assert "website" in data
    assert "company" in data

