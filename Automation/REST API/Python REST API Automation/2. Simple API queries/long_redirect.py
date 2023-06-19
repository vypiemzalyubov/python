# Длинный редирект
# 
# Необходимо написать скрипт, который создает GET-запрос на метод: https://playground.learnqa.ru/api/long_redirect
# С помощью конструкции response.history необходимо узнать, сколько редиректов происходит от изначальной точки назначения до итоговой. И какой URL итоговый.

import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
length_response = len(response.history)
final_url = response.history[-1].url

print(f"Количество редиректов: {length_response}\nИтоговый URL: {final_url}")