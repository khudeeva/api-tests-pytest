from utils.api_client import delete_post, get_post
import pytest
def test_delete_post_sucess():
    response = delete_post(1)
    assert response.status_code == 200
    # assert response.text == ""

# параметризация - удаляем несколько постов
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_delete_post_parametrized(post_id):
    response = delete_post(post_id)
    assert response.status_code == 200
    assert response.text == "{}"

# негативный тест - удаление несуществующего поста
def test_delete_post_non_exisiting_post():
    response = delete_post(9999)
    assert response.status_code !=500
    assert response.text == "{}"

def test_delete_post_api():
    response = delete_post(1)
    assert response.status_code == 200
    assert response.text == "{}"

def test_delete_practice():
    response = delete_post(1)
    assert response.status_code == 200
    assert response.text == "{}"

def test_delete_and_get_post():
    response = delete_post(5)
    assert response.status_code in [200, 204]
    assert response.text == "{}"
    response = get_post(5)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 5

