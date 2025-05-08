from utils.api_client import create_post, get_post, patch_post, delete_post
import pytest

def test_full_checked_api():
    new_post = {
        "title": "Ksenia Post",
        "body": "This is a body",
        "userId": 25
    }

    # POST
    response = create_post(new_post)
    assert response.status_code in [200, 201]
    data = response.json()
    assert "id" in data
    post_id = data["id"]

    # GET
    get_response = get_post(post_id)
    get_data = get_response.json()
    # assert "title" in get_data
    # assert get_data["title"] == new_post["title"]


    # PATCH
    patch_data = {"title": "Updated Title"}
    patch_response = patch_post(post_id, patch_data)
    assert patch_response.status_code == 200
    patched_data = patch_response.json()
    assert patched_data["title"] == "Updated Title"

    # DELETE
    delete_response = delete_post(post_id)
    assert delete_response.status_code == 200

    # GET after delete 
    get_deleted = get_post(post_id)
    assert get_deleted.status_code in [200, 404] 


