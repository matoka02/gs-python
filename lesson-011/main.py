# установка FastAPI
# pip install "fastapi[standard]"
# установка локального сервера
# pip install "uvicorn[standard]"

from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

# переход в текущую директорию
# cd lesson-011/
# запуск сервера
# uvicorn main:app --reload
## python3 -m uvicorn main:app --reload
# остановка сервера
# Ctrl+C
# # запуск сервера на другом порте, если основной занят
# uvicorn main:app --reload --port 8001
# переход в браузере на страницу документации
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

## 1. в браузере перейти по адресу, подставив id
# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

## 2. в браузере перейти по адресу, подставив в id только число
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

## 3. предопределенные значения
# class ModelName(str, Enum):
#     alexnet = 'alexnet'
#     resnet = 'resnet'
#     lenet = 'lenet'
#
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
#
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#
#     return {"model_name": model_name, "message": "Have some residuals"}


## 4.1 параметры запроса
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]

## 4.2 параметры запроса
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}

## 4.3 параметры запроса
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

## 4.4 параметры запроса
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item