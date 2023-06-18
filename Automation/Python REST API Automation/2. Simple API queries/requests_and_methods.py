# Запросы и методы
# 
# У нас есть вот такой URL: https://playground.learnqa.ru/ajax/api/compare_query_type. Запрашивать его можно четырьмя разными HTTP-методами: POST, GET, PUT, DELETE.
# При этом в запросе должен быть параметр method. Он должен содержать указание метода, с помощью которого вы делаете запрос. 
# Например, если вы делаете GET-запрос, параметр method должен равняться строке ‘GET’. Если POST-запросом - то параметр method должен равняться ‘POST’. И так далее.
# Надо написать скрипт, который делает следующее:
# 1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
# 2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
# 3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
# 4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method. 
# Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее. И так для всех типов запроса. 
# Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, но сервер отвечает так, словно все ок. 
# Или же наоборот, когда типы совпадают, но сервер считает, что это не так.
# Не забывайте, что для GET-запроса данные надо передавать через params=. А для всех остальных через data=. Итогом должны быть скрипт и ответы на все 4 вопроса.

import requests

# response_1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
# print(f"Ответ сервера, если не указывать параметр method в запросе: {response_1.text}, статус код {response_1.status_code}")

# response_2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
# print(f"Статус код ответа сервера на http-запрос типа HEAD, которого нет в списке доступных: {response_2.status_code}")

# payload_3 = {"method": "GET"}
# response_3 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload_3)
# print(f"Ответ сервера на GET запрос с правильным параметром method: {response_3.text}, статус код {response_3.status_code}")



get_request = ["GET", "POST", "PUT", "DELETE"]
for r in get_request:
    response_get = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": {r}})
    print(f"Ответ сервера: {response_get.text}\nСтатус код ответа: {response_get.status_code}")