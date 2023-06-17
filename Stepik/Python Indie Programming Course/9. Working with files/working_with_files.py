# 777. Ваша задача выполнить сериализацию словаря из данного задания и сохранить полученную json-строку в переменную json_data. 
#      В качестве ответа ваша программа должна вывести на экран значение переменной json_data.

import json

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 
     'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

json_data = json.dumps(d)
print(json_data)

# 778. К вам в руки попал файлик manager_sales формата json, в котором содержится информация одного автосалона о продажах менеджеров. 
#      В файле указано для каждого менеджера список проданных им автомобилей, а также проставлена цена продажи каждого автомобиля.
#      Ваша задача скачать файлик и самостоятельно найти самого успешного менеджера по итоговой сумме продаж. 
#      В качестве ответа нужно через пробел указать сперва его имя, затем фамилию и после общую сумму его продаж.

import json

max_sum = 0
max_f_name = ''
max_l_name = ''

with open('manager_sales.json') as file:
    data = json.load(file)

    for elem in data:
        f_name = elem["manager"]["first_name"]
        l_name = elem["manager"]["last_name"]
        total = 0
        for car in elem["cars"]:
            total += car["price"]
        if total > max_sum:
            max_sum = total
            max_f_name = f_name
            max_l_name = l_name

print(f'{max_f_name} {max_l_name} {max_sum}')

# 779. В json-файле group_people содержится информация о нескольких групп людей, при этом у каждой группы есть свой идентификатор. 
#      Ваша задача скачать файлик и самостоятельно найти идентификатор группы, в которой находится самое большое количество женщин, рожденных после 1977 года. 
#      В качестве ответа необходимо указать через пробел идентификатор найденной группы и сколько в ней было женщин, рожденных после 1977 года.

import json

max_count = 0
max_group = 0

with open('group_people.json') as file:
    data = json.load(file)

    for elem in data:
        id = elem["id_group"]
        count = 0
        for people in elem["people"]:
            if people["gender"] == 'Female' and people["year"] > 1977:
                count += 1
            if count > max_count:
                max_count = count
                max_group = id

print(f'{max_group} {max_count}')

# 780. Перед вами имеется программа, которая десериализует JSON строку к питоновскому значению.
#      Сама JSON строка оформлена неправильно, поэтому в программе возникает ошибка json.decoder.JSONDecodeError.
#      Ваша задача найти и исправить ошибки в оформлении  JSON строки. Остальную часть программы не нужно менять.

import json

json_string = '''
{
    "customers": [
        {
            "userid": 123456,
            "username": "Allie Hsu",
            "phone": [
                "000-001-0002",
                "000-002-0002"
            ],
            "is_vip": true
        },
        {
            "userid": 223678,
            "username": "Donald Duck",
            "phone": null,
            "is_vip": false
        }
    ]
}
'''

data = json.loads(json_string)
print(data['customers'][0]['username'])