# в корневой директории отключить окружение (использовать луче PowerShell, GitBash не принимает такие команды)
# deactivate
# перейти в директорию lesson-020
# cd lesson-020
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

# запись переменных среды в переменные окружения
# для GitBash
# export ENVIRONMENT=testing
# для PowerShell
# $env:ENVIRONMENT='testing'
# запуск тестов, находящихся в tests
# pytest tests -v -s -p no:warning

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.app:app", host="localhost", log_level="info", reload=True)