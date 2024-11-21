import os
import shutil
from fastapi import Depends, APIRouter, Form, File, UploadFile, HTTPException
from fastapi.responses import FileResponse

from .schemas import ImageProcessingOptions
from .users import current_active_user
from .db import User
from .utils import process_image

file_router = APIRouter()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@file_router.post("/upload/")
async def upload_file(
        file: UploadFile = File(...),
        resize: str = Form(None),
        convert_to: str = Form(None),
        grayscale: bool = Form(None),
        flip: str = Form(None),
        user: User = Depends(current_active_user)
):
    options = ImageProcessingOptions(
        resize=resize,
        convert_to=convert_to,
        grayscale=grayscale,
        flip=flip
    )
    print(options)
    # создание новой папки для хранения
    user_folder = f"{UPLOAD_DIR}/{user.id}"
    os.makedirs(user_folder, exist_ok=True)
    # указание папки хранения
    file_location = os.path.join(user_folder, file.filename)
    # открыть файл
    with open(file_location, 'wb') as buffers:
        shutil.copyfileobj(file.file, buffers)
    # функция обработки изображений
    processed_file_location = process_image(file_location, options)
    return {'filename': os.path.basename(processed_file_location), 'location': processed_file_location}


@file_router.get("/download/{filename}", response_class=FileResponse)
async def download_file(
        filename: str,
        user: User = Depends(current_active_user)
):
    user_folder = f"{UPLOAD_DIR}/{user.id}"
    # указание папки хранения
    file_location = os.path.join(user_folder, filename)
    if not os.path.exists(file_location):
        raise HTTPException(status_code=404, detail='File not found')
    # путь загрузки
    return FileResponse(file_location)
