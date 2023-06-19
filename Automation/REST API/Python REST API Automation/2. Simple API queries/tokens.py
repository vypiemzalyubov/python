# Токены
# 
# Иногда API-метод выполняет такую долгую задачу, что за один HTTP-запрос от него нельзя сразу получить готовый ответ. 
# Это может быть подсчет каких-то сложных вычислений или необходимость собрать информацию по разным источникам.
# В этом случае на первый запрос API начинает выполнения задачи, а на последующие ЛИБО говорит, что задача еще не готова, ЛИБО выдает результат. Сегодня я предлагаю протестировать такой метод.
# Сам API-метод находится по следующему URL: https://playground.learnqa.ru/ajax/api/longtime_job.
# Если мы вызываем его БЕЗ GET-параметра token, метод заводит новую задачу, а в ответ выдает нам JSON со следующими полями:
# * seconds - количество секунд, через сколько задача будет выполнена
# * token - тот самый токен, по которому можно получить результат выполнения нашей задачи
# Если же вызвать метод, УКАЗАВ GET-параметром token, то мы получим следующий JSON:
# * error - будет только в случае, если передать token, для которого не создавалась задача. В этом случае в ответе будет следующая надпись - No job linked to this token
# * status - если задача еще не готова, будет надпись Job is NOT ready, если же готова - будет надпись Job is ready
# * result - будет только в случае, если задача готова, это поле будет содержать результат
# Наша задача - написать скрипт, который делал бы следующее:
# 1) создавал задачу
# 2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
# 3) ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
# 4) делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result

import time
import json
import requests

print(f"Создаем новую задачу...")
response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
json_data1 = json.loads(response1.text)
token = json_data1.get("token")
seconds = json_data1.get("seconds")


print(f"Делаем запрос с token до того, как задача готова...")
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": {token}})
json_data2 = json.loads(response2.text)
status_before = json_data2.get("status")
print(f"Проверяем значение поля status в ответе до создания задачи...")
assert status_before == "Job is NOT ready", 'В поле "status" неверное значение, должно быть "Job is NOT ready"'
print(f"Значение поля status верное...")

print(f"Ждем {seconds} секунд, пока задача не будет готова...")
time.sleep(seconds)

print(f"Делаем запрос с token по истечению {seconds} секунд...")
response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": {token}})
json_data3 = json.loads(response3.text)
status_after = json_data3.get("status")
print(f"Проверяем значение поля status в ответе после создания задачи и наличие поля result...")
assert status_after == "Job is ready", 'В поле "status" неверное значение, должно быть "Job is ready"'
assert "result" in json_data3, 'В ответе отсутвует поле "result"'
print(f"Значение поля status верное, поле result присутствует")