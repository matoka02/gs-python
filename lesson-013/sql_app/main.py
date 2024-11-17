from fastapi import FastAPI
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {'message': 'Hello world'}

# перейти в директорию lesson-013
# cd lesson-013
# запуск сервера
# uvicorn sql_app.main:app --reload
