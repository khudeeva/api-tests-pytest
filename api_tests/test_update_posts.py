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

# автотест с обновлением данных PUT
def test_update_post_success():
    updated_post = {
        "title": "Измененный заголовок",
        "body": "Изменено содержимое",
        "userId": 1
    }
    response = update_post(1, updated_post)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1 #убемся, что обновили нужный пост
    assert data["title"] == updated_post["title"]
    assert data["body"] == updated_post["body"]
    assert data["userId"]== updated_post["userId"]

# автотест с частичным обновлением данных PATCH
def test_patch_post_title():
    new_title_patch = {"title": "Обновим только title"}
    response = patch_post(1, new_title_patch)
    assert response.status_code == 200
    data=response.json()
    assert data["id"] == 1
    assert data["title"] == new_title_patch["title"]
    assert "body" in data
    assert "userId" in data

# параметризация patch
@pytest.mark.parametrize("post_id, patch_data", [
    (1, {"title": "Обновлённый title поста 1"}),
    (2, {"title": "Заголовок для поста 2"}),
    (3, {"title": "Изменение только title (пост 3)"}),
])
def test_patch_title_posts(post_id, patch_data):
    response = patch_post(post_id, patch_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == patch_data["title"]
    assert data["id"] == post_id
    assert "body" in data
    assert "userId" in data

# параметризация негативных тестов для patch
@pytest.mark.parametrize("post_id, patch_data_invalid", [
    (1, {"title": ""}), #пустой заголовк
    (2, {"title": None}),#отсутствует значение
    (3, {"title": 123})#неверный тип данных
])
def test_patch_post_invalid(post_id, patch_data_invalid):
    response = patch_post(post_id, patch_data_invalid)
    assert response.status_code != 500
    data = response.json()
    assert data["id"] == post_id
    assert data["title"] == patch_data_invalid["title"]
    assert "body" in data
    assert "userId" in data

def test_update_post_api():
   updated_post = {
    "title": "Обновлённый заголовок",
    "body": "Полное обновление поста",
    "userId": 1
    }
   response = update_post(1,updated_post)
   assert response.status_code == 200
   data=response.json()
   assert data["id"] == 1
   assert data["title"] == updated_post["title"]
   assert data["body"] == updated_post["body"]
   assert data["userId"] == updated_post["userId"]

def test_patch_post_api():
    partial_data = {
        "title": "Частичное обновление заголовка"   
        }
    response = patch_post(1,partial_data)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == partial_data["title"]
    assert "body" in data
    assert "userId" in data

def test_put_post_practice():
        new_data_practice = {
            "title": "My new title here",
            "body": "This text here",
            "userId": 1
        }
        response = update_post(1, new_data_practice)
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        assert data["title"] == new_data_practice["title"]
        assert data["body"] == new_data_practice["body"]
        assert data["userId"] == new_data_practice["userId"]
def test_patch_post_practice():
    new_title_practice = {
        "title": "My only title here"
    }
    response = patch_post(1, new_title_practice)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1 
    assert data["title"] == new_title_practice["title"]
    assert "body" in data
    assert "userId" in data

def test_patch_post_title_exam():
    new_title_exam = {
        "title": "My new title in test exam"
    }
    response = patch_post(1, new_title_exam)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == new_title_exam["title"]
    assert "body" in data
    assert "userId" in data