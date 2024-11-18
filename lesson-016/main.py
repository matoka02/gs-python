# установка jwt
# pip install PyJWT
# установка python-multipart
# pip install python-multipart
# установка для шифрования и/или подписи контента
# pip install "python-jose[cryptografy]"
# установка для хеширования пароля
# pip install "passlib[bcrypt]"

# генерация SECRET_KEY в терминале
# openssl rand -hex 32

# перейти в директорию lesson-016
# cd lesson-016
# запуск сервера
# uvicorn auth:app --reload