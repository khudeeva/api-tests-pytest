from utils.api_restful import create_post, delete_post,get_post
import pytest

def test_create_post():
    post = {
        "name": "Cherry",
        "data": {
        "year": "1990",
        "color": "red"
        }
    }
    response = create_post(post)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data

def test_create_post_delete():
    data = {
        "name": "Training Device",
        "data": {
            "type": "API",
            "active": True
        }
    }
    response = create_post(data)
    assert response.status_code in [200, 201]
    data = response.json()
    object_id = data["id"]
    delete_response = delete_post(object_id)
    assert delete_response.status_code == 200

    get_response = get_post(object_id)
    assert get_response.status_code == 404


def test_post_get_delete():
    new_data = {
        "name": "QA Device",
        "data": {
            "type": "practice",
            "stable": True
        }
    }
    response = create_post(new_data)
    assert response.status_code in [200, 201]
    data = response.json()
    assert "id" in data
    assert "name" in data
    object_id = data["id"]
    get_response = get_post(object_id)
    assert get_response.status_code == 200
    delete_response = delete_post(object_id)
    assert delete_response.status_code == 200
    get_response_return = get_post(object_id)
    assert get_response_return.status_code == 404

@pytest.mark.parametrize("payload", [
    {"name": "Valid1", "data": {"info": "This text 1"}},
    {"name": "Valid2", "data": {"info": "This text 2"}},
    {"name": "Valid3"}  
])
def test_invalid_post(payload):
    response = create_post(payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data