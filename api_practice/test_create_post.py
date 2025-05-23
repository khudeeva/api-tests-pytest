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

def test_create_posts():
    new_info = {
        "name": "Ksenia QA",
        "username": "ksenia_test",
        "email": "ksenia@example.com"  
      } 
    response = requests.post("https://jsonplaceholder.typicode.com/users", json = new_info)
    assert response.status_code in [200, 201]
    data = response.json()
    assert "id" in data 
    assert data["name"] == "Ksenia QA"

def test_practice_create():
    update_info = {
        "title": "QA rocks",
        "body": "Автотест для создания поста",
        "userId": 99
        }

    
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json = update_info)
    assert response.status_code in [200, 201]
    data = response.json()
    assert "id" in data
    assert data["title"] == update_info["title"]
    assert data["userId"] == update_info["userId"]
    assert data["body"] == update_info["body"]