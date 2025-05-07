import requests

BASE_URL = "https://api.restful-api.dev/objects"

def create_post(data):
    return requests.post(BASE_URL, json=data)

def get_post(object_id):
    return requests.get(f"{BASE_URL}/{object_id}")

def update_post(object_id, data):
    return requests.put(f"{BASE_URL}/{object_id}", json=data)

def patch_post(object_id, data):
    return requests.patch(f"{BASE_URL}/{object_id}", json=data)

def delete_post(object_id):
    return requests.delete(f"{BASE_URL}/{object_id}")
