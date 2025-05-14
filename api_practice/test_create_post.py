import requests
import pytest 

def test_create_post():
    new_data = {
        "title": "New title",
        "body": "This text of first post",
        "userId": 1
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json = new_data)
  
    assert response.status_code in [200, 201]
    data = response.json()
    assert "id" in data
    assert data["title"] == new_data["title"]
    assert data["body"] == new_data["body"]
    assert data["userId"] == new_data["userId"]