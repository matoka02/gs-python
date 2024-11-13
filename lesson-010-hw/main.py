import requests
import json
site = "https://jsonplaceholder.typicode.com"

# task 1
response = requests.get(url=site)
# print(response.text)
print('------------')

# task 2
params = {
    'username': 'Bret'
}
response_get = requests.get(url=site + "/users", params=params)
print(response_get.json())
print('------------')

# task 3
body = {
    'name': 'Leonard G. McCoy',
    'username': 'Tessa',
    'email': 'qwerty@example.com',
    'address': {
        'street': 'Kulas Light',
        'suite': 'Apt. 556',
        'city': 'Gwenborough',
        'zipcode': '92998-3874',
        'geo': {
            'lat': '-37.3159',
            'lng': '81.1496'
        }
    },
    'phone': '1-770-736-8031 x56442',
    'website': 'hildegard.org',
    'company': {
        'name': 'Romaguera-Crona',
        'catchPhrase': 'Multi-layered client-server neural-net',
        'bs': 'harness real-time e-markets'
    }
}
headers = {
    'Content-Type': 'application/json; charset=utf-8'
}
response_post = requests.post(url=site + "/users", json=body, headers=headers)
print(response_post.status_code)
print(response_post.reason)
# print(response_post.text)
print('------------')

# task 4
response_all = requests.get(url=site + "/users")
print(response_all.headers)
print(response_all.history)
print(response_all.status_code)
print('------------')

# task 5
# try:
#     response = requests.get('https://example.com')
#     response.raise_for_status()
#     print(response.text)
# except requests.exceptions.RequestException as e:
#     print('Error:', e)

# task 6
response_get = requests.get(url=site + "/users/2")
content = response_get.json()
print(content)
filename = 'user_content.json'
with open(filename, 'w', encoding='utf-8') as file:
    json.dump(content, file, ensure_ascii=False, indent=4)

print(f"Content saved to {filename}")
