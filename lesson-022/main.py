# 1. в PowerShell в корневой директории ветки deploy выполнить подключение по SSH (использован сервер VPS.ua)
# ssh user@IP
# 2. вводим пароль (ранее получен по эл.почте)
# 3. список папок на просмотр
# ls
# 4. создать папку и перейти в нее
# mkdir home
# cd home
# 5. обновление пакетов
# apt update

# 6. установка Docker на Ubuntu сервера (см. https://docs.docker.com/engine/install/ubuntu/)
# # Add Docker's official GPG key:
# sudo apt-get update
# sudo apt-get install ca-certificates curl
# sudo install -m 0755 -d /etc/apt/keyrings
# sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
# sudo chmod a+r /etc/apt/keyrings/docker.asc
#
# # Add the repository to Apt sources:
# echo \
#   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
#   $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
#   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
# sudo apt-get update

# 7. установка обновлений (см. https://docs.docker.com/engine/install/ubuntu/)
# sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
# 8. проверка версии
# docker --version

# 9. установка SSH-ключа для гитхаба (см. https://docs.github.com/ru/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux)
# ssh-keygen -t ed25519 -C "your_email@example.com"
# eval "$(ssh-agent -s)"
# ssh-add ~/.ssh/id_ed25519
# cat ~/.ssh/id_ed25519.pub

# 10. полученный SSH-ключ сохраняем в учетке гитхаба (см. https://github.com/settings/keys)
# 11. в репозитории теперь копирую нужную ветку по SSH-ключу
# git clone git@github.com:matoka02/fastapi.git
# 12. проверка наличия папки репозитория, заходим в него
# ls
# cd fastapi
# ls
# 13. в одно директории с Dockerfile в терминале
# docker compose up
# 14. в браузере перейти
# http://IP:8080
# 15. в Postmane можно тестировать тоже
# 16. остановка сервера и удаление контейнеров
# Ctrl+C
# docker compose down --volumes
# 17. запуск контейнеров
# docker compose up -d


import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.app:app", host="0.0.0.0", log_level="info", reload=True)