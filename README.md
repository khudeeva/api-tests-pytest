# API Tests with Pytest

Автоматизированные тесты API, написанные с использованием `pytest` и `requests`.

## Описание

Набор автотестов для проверки REST API:  
[https://jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com)

Покрыты все основные HTTP-методы:

- `GET` — получение данных
- `POST` — создание данных
- `PUT` — полное обновление
- `PATCH` — частичное обновление
- `DELETE` — удаление ресурса

## ⚙️ Технологии

- Python 3.10+
- Pytest
- Requests

## Как запускать тесты

- Все тесты:

```bash
pytest

- Тесты из одного файла:
pytest api_tests/test_get_posts.py

- Один конкретный тест:
pytest api_tests/test_get_posts.py::test_get_single_post
```

## Автор: @khudeeva
