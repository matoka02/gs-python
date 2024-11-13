import requests

# В терминале:
# 1) создать виртуальную среду командой
# python3 -m venv venv
# 2) в корне проекта появилась папка venv, активировать командой
# source venv/bin/activate
# 3) для windows - другая команда
# windows_activate = ".\venv\Scripts\activate"
# linux_macos_activate = "source venv/bin/activate"
# 4) в строке перед местоположением проекта появилось имя среды
# (.venv) PS D:\tessa\gs-python>
# 5) установка библиотеки командой
# pip install requests

# site = "https://jsonplaceholder.typicode.com"
# response = requests.get(url=site)
# print(response)
# print('------------')
# print(response.text)
# print('------------')

### GET
site = "https://jsonplaceholder.typicode.com/posts"
response_get = requests.get(url=site + "/8")
# print(response_get.text)
# print('------------')
print(response_get.json())
print('------------')
# print('title: ', response_get.json()['title'])
# print('------------')
# print(response_get.headers)
# print('------------')
# for header, value in response_get.headers.items():
#     print(f"Header: {header} --> Value: {value}")
# print('------------')

### POST
# body = {
#     'userId': 12,
#     'title': 'test',
#     'body': 'test'
# }
# headers = {
#     'Content-Type': 'application/json; charset=utf-8'
# }
# response_post = requests.post(url=site, json=body, headers=headers)
# print(response_post.status_code)
# print(response_post.reason)
# print(response_post.text)
# print('------------')


### PUT - полная перезапись обьекта
# data = {
#     'title': 'test_put'
# }
# response_put = requests.put(url=site + "/8", data=data)
# print(response_put.status_code)
# print(response_put.reason)
# print(response_put.text)
# print('------------')


### PATCH - перезапись только указанного поля
# data = {
#     'title': 'test_put'
# }
# response_patch = requests.patch(url=site + "/8", data=data)
# print(response_patch.status_code)
# print(response_patch.reason)
# print(response_patch.text)
#
# print('------------')


### DELETE
# response_delete = requests.delete(url=site + "/8")
# print(response_delete.status_code)
# print(response_delete.reason)
# print(response_delete.text)