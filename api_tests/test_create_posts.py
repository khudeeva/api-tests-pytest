from utils.api_client import create_post
import pytest

# тест на успешное создание поста
def test_create_post_success():
    new_post = {
        "title": "Pytest is awesome",
        "body": "Testing API with PyTest is fun!",
        "userId": 1
    }
    response = create_post(new_post)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == new_post["title"]
    assert data["body"] == new_post["body"]
    assert data["userId"] == new_post["userId"]

# параметризация (создание нескольких разных постов)
@pytest.mark.parametrize("new_post", [
    {"title": "First post", "body": "This my first post", "userId": 1},
    {"title": "Second post", "body": "This my second post", "userId": 2},
    {"title": "Thirds post", "body": "This my thirds post", "userId": 3},
])
def test_create_post_parametrize(new_post):
    response = create_post(new_post)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == new_post["title"]
    assert data["body"] == new_post["body"]
    assert data["userId"] == new_post["userId"]

# негативный тест - данные title отсутствуют
def test_create_post_without_title():
    invalid_post = {
        "body": "Post without title",
        "userId": 1
    }
# для реального API ожидаем 400, но тут ответ будет 201
    response = create_post(invalid_post)
    assert response.status_code != 500 #хотя бы не ошибка сервера
    data = response.json()
    assert "id" in data
    assert data["body"] == invalid_post["body"]
    assert data["userId"] == invalid_post["userId"]

# проверяем неверный тип userId
def test_create_post_with_invalid_userid():
    post = {
        "title" : "Invalid userId",
        "body": "userId should be number",
        "userId": "admin" #строка вместо числа
    }
    response = create_post(post)
    assert response.status_code !=500

# негативный тест - пустой body
def test_create_post_empty_body():
    empty_body = {
        "title": "Post container empty body",
        "body": "",
        "userId": 1
    }
    response = create_post(empty_body)
    assert response.status_code != 500 # assert response.status_code in [201, 400]
# убедимся, что тело принято таким, как отправлено
    data = response.json()
    assert data["body"] == ""

# параметризованный негативный тест на создание поста
@pytest.mark.parametrize("new_post", [
    {"body": "Missing title", "userId": 1},
    {"title": "Empty body", "body": "", "userId": 1},
    {"title": "Invalid userId", "body": "some text", "userId": "admin"},
    {"title": "", "body": "No title text", "userId": 2}
])
def test_create_post_invalid_cases(new_post):
    response = create_post(new_post)
    assert response.status_code !=500
