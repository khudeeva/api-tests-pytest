import requests
import pytest

def test_put_post():
    full_data = {
        "id": 1,
        "name": "Ksenia Full Update",
        "username": "ksenia123",
        "email": "ksenia@example.com",
        "address": {
            "street": "Main",
            "suite": "Apt. 1",
            "city": "Moscow",
            "zipcode": "12345",
            "geo": {
                "lat": "55.7558",
                "lng": "37.6173"
            }
        },
        "phone": "123-456-7890",
        "website": "kseniaqa.dev",
        "company": {
            "name": "QA Team",
            "catchPhrase": "Testing everything!",
            "bs": "quality-as-a-service"
        }
    }

    response = requests.put("https://jsonplaceholder.typicode.com/users/1", json = full_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Ksenia Full Update"
    assert data["id"]== 1
    assert "company" in data and "name" in data["company"]