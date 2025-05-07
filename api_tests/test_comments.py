from utils.api_client import get_comments
import pytest

@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_comments(post_id):
    response = get_comments(post_id)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for comment  in data:
        assert "name" in comment
        assert "email" in comment
        assert "body" in comment
        assert "@" in comment["email"]

def test_amount_comments():
    response = get_comments(1)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for comment in data:
        assert len(data) == 5
        assert "name" in comment
        assert "email" in comment
        assert "body" in comment
        assert "@" in comment["email"]