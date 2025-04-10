from utils.api_client import get_post, get_comments
import pytest

# проверка первого поста
def test_get_single_post():
    response = get_post(1)

    assert response.status_code == 200

    data = response.json()
    assert "userId" in data
    assert "title" in data
    assert "body" in data

# параметризация(проверка нескольких постов)
@pytest.mark.parametrize("post_id", [1, 2, 5, 10, 50])
def test_get_post_success(post_id):
    response = get_post(post_id)

    assert response.status_code == 200 # проверка что статус 200
    data = response.json()
    assert isinstance(data, dict) # данные - словарь
    assert "userId" in data # есть нужные ключи
    assert "title" in data
    assert "body" in data

# негативный тест - несуществующий пост
def test_get_post_not_found():
    response = get_post(9999)

    assert response.status_code == 404

# проверка структуры - поля, типы и их наличие
def test_post_fields_structure():
    response = get_post(1)

    data = response.json()

    assert isinstance(data["userId"], int)
    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)

# проверка комментариев к посту
def test_get_comments_single_post():
    response = get_comments(1)

    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert "name" in data[0]
    assert "email" in data[0]
    assert "body" in data[0]

# проверка количества комментариев
def test_number_of_comments_for_post_1():
    response = get_comments(1)

    data = response.json()
    assert len(data) == 5

# параметризация количества комментариев
@pytest.mark.parametrize("post_id, expected_count", [
   (1, 5),
   (2, 5), 
   (3, 5), 
   (100, 5),
   (101, 0)
])
def test_comments_count(post_id, expected_count):
    response = get_comments(post_id)

    data = response.json()
    assert len(data) == expected_count

# проверка содержимого всех комментариев
def test_comment_fields_and_email():
    response = get_comments(1)
    data = response.json()
    for comment in data:
        assert "name" in comment
        assert "email" in comment
        assert "body" in comment
        assert "@" in comment["email"]

# проверка содержимого всех комментариев с параметризацией
@pytest.mark.parametrize("post_id", [1, 2, 3, 100])
def test_all_comments_have_valid_fields(post_id):
    response = get_comments(post_id)
    data = response.json()
    
    for comment in data:
        assert "name" in comment
        assert "email" in comment
        assert "body" in comment
        assert "@" in comment["email"]

# автотест на успешный запрос по ID
def test_get_post_success():
    response = get_post(1)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert isinstance(data["userId"], int)
    assert "userId" in data
    assert "title" in data
    assert "body" in data

# автотест с параметризацией
@pytest.mark.parametrize("post_id", [1, 10, 50, 100])
def test_get_posts_parametrize_auto(post_id):
    response = get_post(post_id)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["userId"], int)
    assert "title" in data
    assert "body" in data

# автотест негативный запрос(несуществующий пост)
def test_get_post_no_existing():
    response  = get_post(1900)
    assert response.status_code == 404

def test_get_post_7():
    response = get_post(7)
    assert response.status_code == 200
    data=response.json()
    assert data["id"] == 7
    assert data["userId"] == 1
    assert "body" in data
    assert "title" in data

def test_get_nonexistent_post():
    response = get_post(9999)
    assert response.status_code == 404
    assert response.json() == {} # тело пустое

@pytest.mark.parametrize("post_id", [3, 7, 9])
def test_get_post_by_id(post_id):
    response= get_post(post_id)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "title" in data
    assert data["title"].strip() !=""
    
