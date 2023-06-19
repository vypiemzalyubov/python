import requests
import json

payload = {'name': 'User'}
response = requests.get('https://playground.learnqa.ru/api/hello', params=payload)
print(response.cookies)