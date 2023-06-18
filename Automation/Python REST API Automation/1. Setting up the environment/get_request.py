# GET-запрос
# 
# В проекте создать скрипт, который отправляет GET-запрос по адресу: https://playground.learnqa.ru/api/get_text.
# Затем с помощью функции print вывести содержимое текста в ответе на запрос.

import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)