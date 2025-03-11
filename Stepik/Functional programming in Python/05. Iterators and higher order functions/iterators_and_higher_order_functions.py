# Программе на вход поступают слова, разделенные пробелом. Ваша задача - проверить, во всех ли словах есть английская буква A вне зависимости от регистра.
# В качестве ответа программа должна вывести True или False.

print(all(['a' in word.lower() for word in input().split()]))

# На вход программе поступает список из целых чисел. Ваша задача - вывести True, если элементы в списке отсортированы строго по убыванию.
# В противном случае выведите False.

lst = list(map(int, input().split()))
print(all([lst[i] > lst[i+1] for i in range(len(lst)-1)]))

# Кто не помнит со школьных уроков английского эту запоминашку для написания английских слов, таких, как например, bought?
# Вашей программе на вход будут поступать слова, разделенные пробелом. Программа должна вывести True , если встретилось хотя бы одно слово, заканчивающееся на ought.
# В противном случае нужно вывести False. Регистр букв не имеет значения, значит, интересующиеся нас слова могут заканчиваться как на ought, так и, например, на OUGHT.

print(any([word.endswith('ought') for word in input().lower().split()]))

# Напишите функцию increase_3, которая принимает список целых чисел.
# Функция  increase_3 должна увеличить каждый элемент входного списка втрое, сформировать из этих значений кортеж и вернуть в качестве результата.

def increase_3(lst):
    return tuple(i * 3 for i in lst)

# Напишите функцию convert_to, которая имеет следующие параметры:
#  — values - список однотипных элементов. Элементы могут быть типа float, int, str
#  — type_to - необязательный параметр, по умолчанию принимает тип int
# Функция  convert_to должна конвертировать все элементы списка values в тип type_to и возвращать новый список в качестве результата.
# Используйте функцию map для конвертирования элементов

def convert_to(values, type_to=int):
    return list(map(type_to, values))

# Напишите функцию get_letters, которая принимает строку и формирует из нее список кортежей.
# Каждый элемент кортежа будет состоять из двух значений: берется соответствующая буква сперва в верхнем регистре, а затем в нижнем (см. примеры ниже)

def get_letters(s):
    return list(map(lambda x: (x.upper(), x.lower()), s))

# Перед вами имеется список словарей persons. Изучите внимательно все элементы списка, у них имеется одинаковый набор ключей.
# Ваша задача на основании списка persons отобрать информацию о номерах телефона и сложить их в отдельный список phones.
# Номера в списке phones должны располагаться в том же порядке, в котором расположены их владельцы в списке persons.
# В качестве ответа выведите переменную phones. Используйте функцию map

persons = [
    {
        'birthday': '1983-10-25',
        'job': 'Field seismologist',
        'name': 'Andrew Hernandez',
        'phone': '680-436-8521x3468'
    },
    {
        'birthday': '1993-10-03',
        'job': 'Pathologist',
        'name': 'Paul Harmon',
        'phone': '602.518.4130'
    },
    {
        'birthday': '2002-06-11',
        'job': 'Designer, multimedia',
        'name': 'Gregory Flores',
        'phone': '691-498-5303x079'
    },
    {
        'birthday': '2006-11-28',
        'job': 'Print production planner',
        'name': 'Jodi Garcia',
        'phone': '(471)195-7189'},
    {
        'birthday': '2019-12-05',
        'job': 'Warehouse manager',
        'name': 'Elizabeth Cannon',
        'phone': '001-098-434-5950x276'
    },
    {
        'birthday': '1984-06-12',
        'job': 'Visual merchandiser',
        'name': 'Troy Lucas',
        'phone': '+1-018-070-2288x18433'
    },
    {
        'birthday': '1993-09-14',
        'job': 'International aid/development worker',
        'name': 'Laurie Sandoval',
        'phone': '2930693269'
    },
    {
        'birthday': '1999-05-25',
        'job': 'Editor, film/video',
        'name': 'Jack Clark',
        'phone': '8643048473'
    },
    {
        'birthday': '1985-09-11',
        'job': 'Magazine journalist',
        'name': 'Kimberly Johnson',
        'phone': '+1-583-428-7663'
    },
    {
        'birthday': '1990-10-07',
        'job': 'Museum/gallery curator',
        'name': 'Austin Liu PhD',
        'phone': '714-879-5250'
    }
]

phones = list(map(lambda x: x['phone'], persons))
print(phones)

# Перед вами имеется список кортежей names. Каждый кортеж состоит из двух элементов: имени и фамилии.
# Ваша задача на основании списка names создать новый список new_names, где каждый кортеж должен замениться на строку конкатенации имени и фамилии,
# между которыми стоит пробел . Вот пример на других данных:
# names = [('Monica', 'Waters'), ('Juan', 'Lee'), ('Donna', 'Walker')]
# new_names = ['Monica Waters', 'Juan Lee', 'Donna Walker']
# Для преобразования используйте функцию map. В качестве ответа выведите переменную new_names

names = [('Gerald', 'Tucker'), ('Tricia', 'Johnson'), ('Robert', 'Mendez'),
         ('Shawn', 'Gutierrez'), ('Gary', 'Ross'), ('Melanie', 'Warren'),
         ('Drew', 'May'), ('Jennifer', 'Carroll'), ('Ann', 'Lynn'), ('Ralph', 'Vazquez'),
         ('Brittany', 'Erickson'), ('Mark', 'Montoya'), ('Randall', 'Hicks'),
         ('Tyler', 'Miller'), ('Bryan', 'Brown'), ('Joshua', 'Sawyer'),
         ('Sarah', 'Phillips'), ('Donna', 'Davenport'), ('Rebekah', 'Johnson'),
         ('Andrew', 'Reynolds'), ('April', 'Turner'), ('Amanda', 'Ryan'), ('Jennifer', 'Poole'),
         ('Jonathan', 'Lane'), ('Laura', 'Stone'), ('Sara', 'Brown'), ('Alexander', 'Johnson'),
         ('Emily', 'Phillips'), ('Tyler', 'Smith'), ('Victor', 'Kelly'), ('Audrey', 'Thomas'),
         ('Melissa', 'Green'), ('Bethany', 'Holt'), ('Christopher', 'Kerr'), ('Gabrielle', 'Black'),
         ('Jennifer', 'Wade'), ('Douglas', 'Horton'), ('Steven', 'Welch'),
         ('Terri', 'Thompson'), ('Cassandra', 'Nelson'), ('Andrew', 'Jones'),
         ('James', 'Schultz'), ('Richard', 'Castillo'), ('Shaun', 'Logan'),
         ('Danielle', 'Lane'), ('Mark', 'Anderson'), ('Charles', 'Shaw'),
         ('Derrick', 'Grant'), ('Tracy', 'Pierce'), ('Robert', 'Washington')]

new_names = list(map(lambda x: f'{x[0]} {x[1]}', names))
print(new_names)

# В базовом курсе по python есть задача RGB , в которой необходимо по трем целым числам получить цвет в формате RGB.
# Сейчас вам предстоит выполнить обратное преобразование. Ваша задача создать функцию from_hex_to_rgb, которая принимает на вход строку
# - закодированный код цвета в формате RGB и возвращает кортеж из трех значений (оттенок_красного, оттенок_зеленого, оттенок_синего). Вот посмотрите примеры:
# from_hex_to_rgb(#000000) => (0, 0, 0)
# from_hex_to_rgb(#FFFFFF) => (255, 255, 255)
# from_hex_to_rgb(#FF0000) => (255,0, 0)
# from_hex_to_rgb(#00FF00) => (0,255, 0)
# from_hex_to_rgb(#0000FF) => (0,0,255)
# from_hex_to_rgb(#FFFFFF) => (255,255,255)
# from_hex_to_rgb(#87CEEB) => (135,206,235)
# from_hex_to_rgb(#87CEFA) => (135,206,250)
# from_hex_to_rgb(#191970) => (25,25,112)
# Как только функция будет готова, ее необходимо использовать внутри функции convert_to_rgb, которая принимает список строк,
# содержащих информацию о цветах в формате RGB. Функция convert_to_rgb должна расшифровать каждый цвет и вернуть список кортежей.

def from_hex_to_rgb(color: str) -> tuple[int, int, int]:
    color = color[1:3], color[3:5], color[5:7]
    return tuple(map(lambda x: int(x, 16), color))


def convert_to_rgb(values: list[str]) -> list[tuple[int, int, int]]:
    return [from_hex_to_rgb(value) for value in values]

# Имеются три списка из 50 элементов: list_x, list_y и list_w.
# Ваша задача — произвести научные расчеты для соответствующих значений этих списков. Нужно подставить в формулу x**2−x∗y∗w+w**4
# поочередно первые значения из списков list_x, list_y и list_w, потом вторые, затем третьи и т.д.
# Значения из списка list_x должны подставляться в переменную x, из списка list_y - в переменную y и из списка list_w - в переменную w.
# Всего должно получиться 50 вычисленных значений. Их необходимо сложить в список и вывести на экран.

list_x = [25, 48, 23, 13, -18, -10, -3, 16, 2, -12, 20, -14, 14, 45, 41, 6, 11, 15, 22,
          -14, -11, 41, 15, 48, 47, 41, -8, 1, 4, 1, 40, 27, -11, -2, -14, -15, 35, 4,
          49, 4, 5, 13, 50, 35, -3, 3, 30, -11, 7, 12]

list_y = [-9, 17, 41, 47, -5, -10, -5, 13, 31, -11, 37, 9, 46, 27, -1, 36, 32, 23, -12,
          38, 8, 9, 17, 16, 29, -4, 4, 2, 1, 46, 6, 49, -16, 21, -19, -10, 15, -13, 20,
          13, -18, 21, -17, 21, 10, 5, 38, -1, 18, 22]

list_w = [9, -26, 3, 21, 48, -14, 43, -4, -16, 16, 41, 43, -27, -9, 10, -10, 4, -2, 1,
          7, 30, -29, 11, 17, 31, 31, -26, 38, 38, -17, 35, 17, 35, 10, -25, 42, -30,
          -10, -20, 20, 15, 0, 29, -30, -21, -13, -27, -21, -18, -26]

print(list(map(lambda x, y, w: pow(x, 2) - x * y * w + pow(w, 4), list_x, list_y, list_w)))

# Напишите функцию filter_numbers, которая принимает список целых чисел и возвращает новый список,
# который состоит только из четных чисел входного списка или из тех, которые по модулю больше 100.

def filter_numbers(lst):
    return list(filter(lambda x: x % 2 == 0 or abs(x) > 100, lst))

# Напишите функцию filter_words, которая принимает список строк и возвращает новый список,
# который состоит из строк, длина которых четыре символа, или начинающихся на заглавную букву S.

def filter_words(lst):
    return list(filter(lambda x: len(x) == 4 or x.startswith('S'), lst))

# Перед вами имеется реализация функции get_values. Ваша задача — избавиться от циклов for при помощи map и filter.
# Для этого перепишите функцию get_values, но так, чтобы она не меняла свою изначальную функциональность

def get_values(nums: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(list(map(lambda x: x * 3, list(filter(lambda x: x % 3 == 0, nums)))))

# Напишите функцию filter_tuples, которая принимает кортеж кортежей из трех числовых значений.
# Функция filter_tuples должна вернуть новый кортеж, который состоит только из тех элементов входного кортежа, произведение значений которых равно 60

def filter_tuples(tpl):
    return tuple(filter(lambda x: __import__('math').prod(x) == 60, tpl))

# Перед вами список словарей foods, который хранит в себе информацию о меню ресторана.
# Проанализируйте ключи и значения, хранящиеся в словарях списка foods, они вам потребуются для задания.
# Ваша задача — найти все имена блюд, которые являются салатами в списке foods.
# Из имен салатов необходимо составить список, элементы которого должны следовать в том же порядке, как и в списке foods.
# В качестве ответа выведите на экран найденный список. Используйте функции map и filter.

foods = [
    {'name': "Стейк Рибай", 'type_food': "Основное", 'price': 75.95},
    {'name': "Ассорти из гигантских креветок", 'type_food': "Закуска", 'price': 2029.95},
    {'name': "Оливье", 'type_food': "Салат", 'price': 329.95},
    {'name': "Жареный канадский бекон", 'type_food': "Закуска", 'price': 239.95},
    {'name': "Крабовый пирог", 'type_food': "Закуска", 'price': 532.95},
    {'name': "Цезарь", 'type_food': "Салат", 'price': 14.95},
    {'name': "Пирог из лобстера", 'type_food': "Закуска", 'price': 230.95},
    {'name': "Огурчики", 'type_food': "Закуска", 'price': 123.95},
    {'name': "Мимоза", 'type_food': "Салат", 'price': 223.95},
    {'name': "Овощной", 'type_food': "Салат", 'price': 310.95},
    {'name': "Картошка фри", 'type_food': "Гарнир", 'price': 234.95},
    {'name': "Спаржа", 'type_food': "Гарнир", 'price': 455.95},
    {'name': "Стейк Техасский", 'type_food': "Основное", 'price': 1631.95},
    {'name': "Грибы", 'type_food': "Гарнир", 'price': 234.95},
    {'name': "Лосось на гриле", 'type_food': "Основное", 'price': 936.95},
    {'name': "Крабовый", 'type_food': "Салат", 'price': 563.95}
]

print(list(map(lambda x: x['name'], filter(lambda x: x['type_food'] == 'Салат', foods))))

# Перед вами вновь список словарей foods. Ваша задача — найти суммарную стоимость всех основных блюд, которые имеются в списке foods.
# В качестве ответа выведите найденную сумму, округленную до двух знаков после запятой

foods = [
    {'name': "Стейк Рибай", 'type_food': "Основное", 'price': 75.95},
    {'name': "Ассорти из гигантских креветок", 'type_food': "Закуска", 'price': 2029.95},
    {'name': "Оливье", 'type_food': "Салат", 'price': 329.95},
    {'name': "Жареный канадский бекон", 'type_food': "Закуска", 'price': 239.95},
    {'name': "Крабовый пирог", 'type_food': "Закуска", 'price': 532.95},
    {'name': "Цезарь", 'type_food': "Салат", 'price': 14.95},
    {'name': "Пирог из лобстера", 'type_food': "Закуска", 'price': 230.95},
    {'name': "Огурчики", 'type_food': "Закуска", 'price': 123.95},
    {'name': "Мимоза", 'type_food': "Салат", 'price': 223.95},
    {'name': "Овощной", 'type_food': "Салат", 'price': 310.95},
    {'name': "Картошка фри", 'type_food': "Гарнир", 'price': 234.95},
    {'name': "Спаржа", 'type_food': "Гарнир", 'price': 455.95},
    {'name': "Стейк Техасский", 'type_food': "Основное", 'price': 1631.95},
    {'name': "Грибы", 'type_food': "Гарнир", 'price': 234.95},
    {'name': "Лосось на гриле", 'type_food': "Основное", 'price': 936.95},
    {'name': "Крабовый", 'type_food': "Салат", 'price': 563.95}
]

print(sum(list(map(lambda x: x['price'], filter(lambda x: x['type_food'] == 'Основное', foods)))))