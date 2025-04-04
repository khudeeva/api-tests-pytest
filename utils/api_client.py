import requests
# базовый адрес API
BASE_URL = "https://jsonplaceholder.typicode.com"

# GET
# возвращает ответ от сервера, когда делаем запрос к /posts/1, /posts/2 и т.д.
def get_post(post_id):
    return requests.get(f"{BASE_URL}/posts/{post_id}")

#проверка комментариев к посту
def get_comments(post_id):
    return requests.get(f"{BASE_URL}/posts/{post_id}/comments")

#POST
def create_post(data):
    return requests.post(f"{BASE_URL}/posts", json=data)