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

# автотест создание поста
def test_create_post_first():
    new_data_first = {
        "title": "Мой заголовок",
        "body": "Это содежимое поста",
        "userId": 1
    }
    response = create_post(new_data_first)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == new_data_first["title"]
    assert data["body"] == new_data_first["body"]
    assert data["userId"] == new_data_first["userId"]
# автотест с параметризацией создания постов
@pytest.mark.parametrize("new_data_parametrized", [
    {"title": "Заголовок 1", "body": "Содержимое 1 поста", "userId": 1},
    {"title": "Заголовок 2", "body": "Содержимое 2 поста", "userId": 2},
    {"title": "Заголовок 3", "body": "Содержимое 3 поста", "userId": 3}
])
def test_create_posts_parametrized_auto(new_data_parametrized):
    response = create_post(new_data_parametrized)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == new_data_parametrized["title"]
    assert data["body"] ==  new_data_parametrized["body"]
    assert data["userId"] == new_data_parametrized["userId"]

# негативный тест (пустой title, нет body, userId - строка, а не число)
def test_create_posts_invalid_date():
    invalid_data_post = {
        "title": "", "userId": "это строка"
    }
    response = create_post(invalid_data_post)
    data = response.json()
    assert response.status_code !=500
    assert "id" in data
    assert data["title"] == ""
    assert "body" not in data
    assert data["userId"] == invalid_data_post["userId"]
    assert isinstance(data["userId"], str)

# параметризация неагтивных тестов
@pytest.mark.parametrize("invalid_post", [
    {"title": "", "body": "Нет заголовка", "userId": 1},
    {"title": "Нет body", "userId": 2},
    {"title": "userId — строка", "body": "some text", "userId": "abc"},
    {"title": "Нет userId", "body": "но есть текст"},
])
def test_create_post_invalid_data_parametrized(invalid_post):
    response = create_post(invalid_post)
    data = response.json()
    assert response.status_code != 500
    assert "id" in data
    assert data.get("title") == invalid_post.get("title")
    assert data.get("body") == invalid_post.get("body")
    assert data.get("userId") == invalid_post.get("userId")

def test_create_post_api():
    new_post = {
        "title": "Автотест",
    "body": "Создано в рамках практики",
    "userId": 101
    }
    response = create_post(new_post)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == new_post["title"]
    assert data["body"] == new_post["body"]
    assert data["userId"] == new_post["userId"]

def test_create_post_invalid_data():
    invalid_post = {}
    response = create_post(invalid_post)
    assert response.status_code != 500
    data = response.json()
    assert "id" in data
    assert "title" not in data
    assert "body" not in data
    assert "userId" not in data  

@pytest.mark.parametrize("new_data_api",[
    {"title": "Пост 1", "body": "Описание 1", "userId": 10},
    {"title": "Пост 1", "body": "Описание 1", "userId": 20},
    {"title": "Пост 1", "body": "Описание 1", "userId": 30}
])
def test_create_post_parametrize_api(new_data_api):
    response = create_post(new_data_api)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == new_data_api["title"]
    assert data["body"] == new_data_api["body"]
    assert data["userId"] == new_data_api["userId"]
@pytest.mark.parametrize("invalid_all_data", [
    {"title": "", "body": "Нет title", "userId": 10},
    {"title": "Title есть", "body": "Нет userId", "userId": None},
    {"title": "Title есть", "body": "", "userId": 30}
])
def test_invalid_parametrize(invalid_all_data):
    response = create_post(invalid_all_data)
    assert response.status_code !=500
    data = response.json()
    assert "id" in data
    assert data["title"] == invalid_all_data["title"]
    assert data["body"] == invalid_all_data["body"]
    assert data["userId"] == invalid_all_data["userId"]

def test_create_post_practice():
    new_data_practice = {
    "title": "My post",
    "body": "Some text here",
    "userId": 1
}
    response=create_post(new_data_practice)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == new_data_practice["title"]
    assert data["body"] == new_data_practice["body"]
    assert data["userId"] == new_data_practice["userId"]

def test_create_post_practice2():
    new_data_practice2 = {
        "title": "Some title here",
        "body": "Some text here",
        "userId":1
    }
    response = create_post(new_data_practice2)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == new_data_practice2["title"]
    assert data["body"] == new_data_practice2["body"]
    assert data["userId"] == new_data_practice2["userId"]

@pytest.mark.parametrize("new_data_posts", [
    {"title": "My test 1", "body": "My text for test1", "userId": 1},
    {"title": "My test 2", "body": "My text for test2", "userId": 2},
    {"title": "My test 3", "body": "My text for test3", "userId": 3}
])
def test_create_post_parametrize_practice(new_data_posts):
    response = create_post(new_data_posts)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == new_data_posts["title"]
    assert data["body"] == new_data_posts["body"]
    assert data["userId"] == new_data_posts["userId"]

def test_create_post_missing_fields():
    data_missing = {
        "title": "This title for test"
    }
    response = create_post(data_missing)
    assert response.status_code != 500
    data = response.json()
    assert data["title"] == data_missing["title"]

@pytest.mark.parametrize("create_posts_data", [
{"title": "Title1", "body": "This text for title1", "userId": 1},
{"title": "Title2", "body": "This text for title2", "userId": 2},
{"title": "Title3", "body": "This text for title3", "userId": 3}
])
    
def test_create_posts_practice(create_posts_data):
    response = create_post(create_posts_data)
    assert response.status_code in [200, 201]
    data = response.json()
    assert "id" in data
    assert data["title"] == create_posts_data["title"]
    assert data["body"] == create_posts_data["body"]
    assert data["userId"] == create_posts_data["userId"]

@pytest.mark.parametrize("invalid_posts_data", [
{"title": "Title1", "body": "", "userId": 1},
{"title": "", "body": "This text for title2", "userId": 2},
{"title": "", "body": "", "userId": 3}
])
def test_negative_parametrize_posts(invalid_posts_data):
    response = create_post(invalid_posts_data)
    assert response.status_code !=500
    data = response.json()
    assert "title" not in data or data["title"] == invalid_posts_data["title"]
    assert "body" not in data or data["body"] == invalid_posts_data["body"]

