from utils.api_client import update_post, patch_post
import pytest

def test_update_post_success():
    updated_post = {
        "title": "Updated title",
        "body": "This post was updated succeddfully",
        "userId": 1
    }
    response = update_post(1, updated_post)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == updated_post["title"]
    assert data["body"] == updated_post["body"]
    assert data["userId"] == updated_post["userId"]

def test_update_post_number_5():
    updated_post_number_5 ={
        "title": "Обновлённый пост",
        "body": "Содержимое изменено",
        "userId": 3
    }
    response = update_post(5, updated_post_number_5)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == updated_post_number_5["title"]
    assert data["body"] == updated_post_number_5["body"]
    assert data["userId"] == updated_post_number_5["userId"]

# параметризация - обновление постов
@pytest.mark.parametrize("post_id, update_data", [
    (1, {"title": "обновление 1", "body": "Новый текст 1", "userId": 10}),
    (2, {"title": "обновление 2", "body": "Новый текст 2", "userId": 20}),
    (3, {"title": "обновление 3", "body": "Новый текст 3", "userId": 30})
])
def test_update_post_parametrized(post_id, update_data):
    response = update_post(post_id, update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == update_data["title"]
    assert data["body"] == update_data["body"]
    assert data["userId"] == update_data["userId"]

# PATCH
def test_patch_post_title():
    updated_title = {
        "title": "Изменен только заголовок"
    }
    response = patch_post(1, updated_title)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == updated_title["title"]

# параметризация частичное обновление 
@pytest.mark.parametrize("post_id, patch_data", [
    (1, {"title": "Заголовок поста 1"}),
    (2, {"title": "Обновлен заголок поста 2"}),
    (3, {"title": "Новый title для 3 поста"})
])
def test_patch_title_posts(post_id, patch_data):
    response = patch_post(post_id, patch_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == patch_data["title"]
    assert "body" in data # проверяем, что другие поля остались без изменений
    assert "userId" in data

# негативное тестирование PATCH(пустая строка title)
def test_patch_post_empty_title():
    negative_patch = {
         "title": ""
    }
    response = patch_post(1, negative_patch)
    assert response.status_code != 500
    data = response.json()
    assert data["title"] == ""
    assert "body" in data
    assert "userId" in data