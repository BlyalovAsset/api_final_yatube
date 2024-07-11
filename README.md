# API_FINAL_YATUBE

API_Final - законченная версия API для yatube.

## Описание проекта

API_Final - это API для платформы yatube, которая позволяет пользователям публиковать посты, комментировать их и подписываться на других пользователей. Этот проект предоставляет все необходимые конечные точки для работы с данными платформы.

## Стек технологий

- Python 3.7
- Django Rest Framework
- SQLite

## Как запустить проект

1. Клонировать репозиторий и перейти в него в командной строке:
    ```sh
    git clone git@github.com:BlyalovAsset/api_final_yatube.git
    cd api_final_yatube
    ```

2. Создать и активировать виртуальное окружение:
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. Установить зависимости из файла `requirements.txt`:
    ```sh
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

4. Выполнить миграции:
    ```sh
    python3 manage.py migrate
    ```

5. Запустить проект:
    ```sh
    python3 manage.py runserver
    ```
## Примеры запросов к API

1. Получить список всех постов (GET):
   ```sh
    http://127.0.0.1:8000/api/v1/posts/
    ```
   Пример ответа:
   ```sh
   {
    "count": 11,
    "next": "/api/v1/posts/?limit=1&offset=2",
    "previous": "/api/v1/posts/?limit=1",
    "results": [
        {
            "id": 2,
            "author": "regular_user",
            "text": "Пост зарегистрированного пользователя.",
            "pub_date": "2023-11-30T10:03:46.978297Z",
            "image": null,
            "group": null
        }
    ]
    }
   ```
2. Получить определенный пост (GET):
    ```sh
    [http://127.0.0.1:8000/api/v1/posts/](http://127.0.0.1:8000/api/v1/posts/1/)
    ```
    Пример ответа:
    ```sh
    {
            "id": 2,
            "author": "regular_user",
            "text": "Пост зарегистрированного пользователя.",
            "pub_date": "2023-11-30T10:03:46.978297Z",
            "image": null,
            "group": null
        }
    ```
3. Получить коментарии определенного поста (GET):
    ```sh
    http://127.0.0.1:8000/api/v1/posts/1/comments/
    ```
    Пример ответа:
    ```sh
    {
            "id": 2,
            "author": "regular_user",
            "text": "Пост зарегистрированного пользователя.",
            "pub_date": "2023-11-30T10:03:46.978297Z",
            "image": null,
            "group": null
   }
    ```
4. Оформление подписки:
   ```sh
    POST /api/v1/follow/ HTTP/1.1
Authorization: Bearer [token]
content-type: application/json

{
    "following": "root"
}
    ```
Пример ответа:
```sh
{
  "user": "testuser",
  "following": "root"
}
```
author: Asset Blyaov
