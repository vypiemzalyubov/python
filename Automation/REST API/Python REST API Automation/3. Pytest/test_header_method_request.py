# Тест запроса на метод header
# 
# Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_header.
# Этот метод возвращает headers с каким-то значением. Необходимо с помощью функции print() понять что за headers и с каким значением, и зафиксировать это поведение с помощью assert.

import requests

def test_check_cookie():
    response = requests.get("https://playground.learnqa.ru/api/homework_header")
    header = response.headers
    assert response.status_code == 200, "Wrong response status code"
    assert header["x-secret-homework-header"] == "Some secret value", "Wrong header in answer"