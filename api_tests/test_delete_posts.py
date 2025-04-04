from utils.api_client import delete_post
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
    # assert response.text == "{}"
