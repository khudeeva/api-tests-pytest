import requests
import pytest

def test_get_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "userId" in data

def test_get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 10
    assert "email" in data[0]

def test_practice_get():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["userId"] == 1
    assert "title" in data
    print(data["title"])