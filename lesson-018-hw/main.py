# установка интерфейса базы данных
# pip install asyncpg

# в корневой директории отключить окружение (использовать луче PowerShell, GitBash не принимает такие команды)
# deactivate
# перейти в директорию lesson-018-hw
# cd lesson-018-hw
# установка свежего окружения в директории
# python.exe -m venv venv
# активировать среду
# windows_activate = ".\venv\Scripts\activate"
# linux_macos_activate = "source venv/bin/activate"
# список установленных пакетов
# pip list
# установить пакеты согласно требований
# pip install -r requirements.txt

# запуск сервера
# uvicorn app.app:app --reload
# запуск сервера (v2)
# python main.py

# для проверки работы см. инструкции
# https://fastapi-users.github.io/fastapi-users/latest/usage/flow/

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.app:app", host="localhost", log_level="info")