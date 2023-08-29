# 439. Напишите функцию file_read, которая принимает имя файла, и печатает его содержимое. 
#      Учитывайте, что содержимое файла может быть как на русском языке, так и на английском.

def file_read(file_name: str) -> None:
    file = open(file_name, encoding='utf-8')
    print(file.read())

# 440. Напишите функцию file_n_lines, которая печатает первые n-строка файла. Функция file_n_lines принимает на вход название файла и количество строк для прочтения.
#      Не забывайте избавляться от символа переноса строки К примеру, если бы имелся файл hello.txt со следующим содержимым:
#      h
#      he
#      hel
#      hell
#      hello
#      То вызов file_n_lines(hello.txt, 3) должен распечатать следующее:
#      h
#      he
#      hel
#      Ваша задача написать только определение функции file_n_lines.

def file_n_lines(file_name: str, n: int) -> None:
    file = open(file_name, encoding='utf-8')
    [print(file.readline().strip()) for _ in range(n)]

# 441. Напишите функцию create_file_with_numbers, которая принимает на вход одно целое положительное число - n.
#      Функция должна создать файл с название "range_<number>.txt" и наполнить его целыми числами от 1 до n включительно, причем каждое число записывается  в отдельной строке.
#      Пример: функция create_file_with_numbers(5) должна создать файл range_5.txt с содержимым
#      1
#      2
#      3
#      4
#      5

def create_file_with_numbers(n: int) -> None:
    file = open(f'range_{n}.txt', 'a')
    [file.write(f'{i}\n') for i in range(1, n + 1)]

# 442. Напишите функцию longest_word_in_file, которая принимает имя файла и внутри его содержимого находит самое длинное слово и возвращает его в качестве ответа. 
#      В случае,  если есть несколько слов с максимальной длиной, нужно вернуть слово, которое встречается последнее в тексте. При этом слова в тексте отделяются друг от друга пробелами, 
#      любые другие знаки пунктуации необходимо исключить. И также учитывайте, что слова в тестах будут как на русском языке, так и на английском.
#      Если бы содержимое файла было таким:
#      He was running, but it was like running through deep water. There were trees all around him, 
#      trees which tried to stop him. They reached out with their branches. 
#      And it was behind him. It was coming nearer. 
#      то ответом было бы слово branches.
#      Все возможные знаки пунктуации можно получить из модуля string
#      from string import punctuation

from string import punctuation

def longest_word_in_file(file_name):
    longest_word = ''
    file = open(file_name, 'r', encoding='utf-8')
    for word in file.read().split():
        word = word.strip(punctuation)
        if len(word) >= len(longest_word):
            longest_word = word
    return longest_word

# 443. В этой задаче вам необходимо скачать файл numbers.txt, в котором записаны натуральные числа. Ваша задача найти:
#      - количество трехзначных чисел;
#      - сумму двухзначных чисел
#      В качестве ответа укажите найденные два числа через запятую без других знаков и пробелов. Сперва количество, потом сумма

file = open('numbers.txt')
count = sum = 0
for i in file:
    if 99 < int(i) <= 999:
        count += 1
    elif 9 < int(i) <= 99:
        sum += int(i)
print(f'{count},{sum}') 

# 444. Напишите функцию find_lines_len_more_6, которая принимает имя файла и находит количество строк, превышающее 6 символов. 
#      Не забывайте исключать знак переноса на новую строку, стоящий в конце строки. Функция find_lines_len_more_6 должна возвращать найденное количество строк.
#      Ваша задача написать только определение функции find_lines_len_more_6.

def find_lines_len_more_6(file_name:str) -> int:
    with open(file_name, 'r', encoding='utf-8') as f:
        return sum(len(line) > 6 for line in f.read().splitlines())

# 445. В вашем распоряжении имеется следующий файл lorem.txt. Ваша задача скачать его и найти сколько уникальных слов используется в этом тексте, при этом регистр букв не нужно учитывать. 
#      Это значит, что слова Lorem и loRem являются эквивалентными.
#      Например, если перед вами был бы такой текст:
#      Привет как дела
#      привет хорошо
#      то здесь четыре уникальных слова.
#      Между словами в файле стоят только пробелы и переносы строк, других разделителей нет. В качестве ответа укажите количество уникальных слов.

with open('lorem.txt', 'r', encoding='utf-8') as f:
    print(len(set(f.read().lower().split())))

# 446. В вашем распоряжении имеется файл lorem_new.txt. Ваша задача посчитать сколько раз встретилось каждое слово в этом тексте. 
#      Для этого создайте словарь words, где ключом будет слово, а значением - количество раз появления этого слова в тексте. 
#      Регистр букв в словах учитывать не нужно, поэтому слова Hello и hEllO являются эквивалентными. Значения ключа в словаре words записывайте в верхнем регистре.
#      Например, если перед вами был бы такой текст:
#      Привет как дела
#      привет хорошо
#      то словарь words выглядел бы так:
#      {'ПРИВЕТ': 2, 'КАК': 1, 'ДЕЛА': 1, 'ХОРОШО': 1}
#      Между словами в файле стоят только пробелы и переносы строк, других разделителей нет. 
#      Ваша задача только создать переменную-словарь words и подсчитать в нем количество повторений слов. Выводить ничего не нужно.

with open('lorem_new.txt', 'r', encoding='utf-8') as f:
    words = {}
    for word in f.read().upper().split():
        words[word] = words.get(word, 0) + 1

# 447. В этой задаче вам необходимо обработать файл с названием words.txt, содержащий множество неуникальных слов. 
#      Ваша задача найти в нем все слова, заканчивающиеся на строку ЕЯ, и вывести их на экран. При этом нужно:
#      - исключить дубли
#      - привести все буквы к верхнему регистру
#      - расположить слова в выводе в порядке двойной сортировки: сперва отсортировать по возрастанию длины слова, а при одинаковых значениях длины расположить по алфавиту.
#      Значит, если бы перед вам был файл с содержимым:
#      панацея
#      газосварщик
#      ФЕЯ
#      затея
#      лапочка
#      Гея
#      панацея
#      богая
#      ливрея
#      ШЕЯ
#      я
#      Камыш
#      то ответ должен быть таким:
#      ГЕЯ
#      ФЕЯ
#      ШЕЯ
#      ЗАТЕЯ
#      ЛИВРЕЯ
#      ПАНАЦЕЯ
#      Не забывайте про кодировку)

with open('words.txt', 'r', encoding='utf-8') as f:
    s = set()
    for word in f.read().upper().split():
        if word.endswith('ЕЯ'):
            s.add(word)
    [print(i) for i in sorted(s, key=lambda x: (len(x), x))]

# 448. Ваша задача выполнить сериализацию словаря из данного задания и сохранить полученную json-строку в переменную json_data. 
#      В качестве ответа ваша программа должна вывести на экран значение переменной json_data.

import json

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 
     'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

json_data = json.dumps(d)
print(json_data)

# 449. К вам в руки попал файлик manager_sales формата json, в котором содержится информация одного автосалона о продажах менеджеров. 
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

# 450. В json-файле group_people содержится информация о нескольких групп людей, при этом у каждой группы есть свой идентификатор. 
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

# 451. В этой задаче вам необходимо раскодировать текст, находящийся в текстовом файле Abracadabra__1_. Ключ для декодирования располагается в json-файле Alphabet. 
#      В качестве ответа нужно просто отправить получившийся текст. И обратите внимание, что раскодировать нужно только лишь буквы, 
#      все остальные символы (цифры, знаки пунктуации и т.д.) необходимо выводить как есть.

import json

with open('Abracadabra__1_.txt') as file_txt:
    text = file_txt.read()

with open('Alphabet.json') as file:
    alphabet = json.load(file)

for char in text:
    print(alphabet.get(char, char), end='')

# 452. Переменная people содержит строку в формате JSON, в которой вы можете получить личные данные 100 человек.
#      Каждого человека представляет предмет (словарь) с ключами:
#      - имя
#      - страна
#      - возраст
#      Распечатайте информацию о каждом человеке в соответствии с примером ниже. 
#      ...
#      Melissa Crawford, Lebanon, 17
#      Paul Herrera, Kiribati, 17
#      Justin Galvan, Namibia, 19
#      Mary Estes, Montenegro, 19
#      Larry Bray, Brunei Darussalam, 21
#      ...
#      <Имя>, <Страна>, <Возраст>
#      Распечатку необходимо отсортировать по возрасту, а при равенстве возраста необходимо расположить в алфавитном порядке.

import json

people = '[{"name": "Haley Whitney", "country": "British Indian Ocean Territory (Chagos Archipelago)", "age": 54}, {"name": "Matthew King", "country": "Colombia", "age": 34}, {"name": "Sean Sullivan", "country": "Mayotte", "age": 40}, {"name": "Christian Crawford", "country": "Russian Federation", "age": 29}, {"name": "Sarah Contreras", "country": "Honduras", "age": 82}, {"name": "Danielle Williams", "country": "Togo", "age": 91}, {"name": "Jonathan Wilson", "country": "Tunisia", "age": 49}, {"name": "Patricia Wilkerson", "country": "Georgia", "age": 22}, {"name": "Zachary Scott", "country": "Brunei Darussalam", "age": 55}, {"name": "Elizabeth Sanchez", "country": "Nauru", "age": 23}, {"name": "Christina Fernandez", "country": "Burundi", "age": 71}, {"name": "Allen Norton", "country": "Montserrat", "age": 79}, {"name": "Scott Arroyo", "country": "Montenegro", "age": 72}, {"name": "Brooke Boyd", "country": "Latvia", "age": 74}, {"name": "Jerry Morrow", "country": "San Marino", "age": 23}, {"name": "Danielle Bradshaw", "country": "Vietnam", "age": 64}, {"name": "Jerry Thompson", "country": "Belgium", "age": 30}, {"name": "Mark Jordan", "country": "Comoros", "age": 89}, {"name": "Joseph Berger", "country": "Cook Islands", "age": 94}, {"name": "Gina Brooks", "country": "Samoa", "age": 51}, {"name": "Walter Duran", "country": "Chad", "age": 67}, {"name": "John Martinez", "country": "Wallis and Futuna", "age": 65}, {"name": "Johnny Glover", "country": "Eritrea", "age": 72}, {"name": "Lindsay Moore", "country": "Liberia", "age": 53}, {"name": "Kimberly Burton", "country": "Nicaragua", "age": 92}, {"name": "Jacqueline Ballard", "country": "Nigeria", "age": 78}, {"name": "Charles Thompson", "country": "Saudi Arabia", "age": 50}, {"name": "Suzanne Roberts", "country": "Serbia", "age": 43}, {"name": "David Decker", "country": "South Africa", "age": 71}, {"name": "Christopher Perez", "country": "Cayman Islands", "age": 49}, {"name": "Debra Hall", "country": "Greece", "age": 13}, {"name": "John King", "country": "Bahamas", "age": 40}, {"name": "Justin Galvan", "country": "Namibia", "age": 19}, {"name": "Jacqueline Berger", "country": "Yemen", "age": 59}, {"name": "Shawn Robinson", "country": "Saint Pierre and Miquelon", "age": 32}, {"name": "Kristen Garcia", "country": "Portugal", "age": 48}, {"name": "Christopher Barry", "country": "French Polynesia", "age": 23}, {"name": "Alejandra Cook", "country": "Egypt", "age": 16}, {"name": "Jill Harrell", "country": "Comoros", "age": 49}, {"name": "Sara Zimmerman", "country": "Brazil", "age": 26}, {"name": "Mrs. Charlene Flores", "country": "New Caledonia", "age": 75}, {"name": "Melissa Crawford", "country": "Lebanon", "age": 17}, {"name": "Larry Wong", "country": "New Caledonia", "age": 6}, {"name": "Brenda Acosta", "country": "Grenada", "age": 48}, {"name": "Latoya Terry", "country": "Saint Martin", "age": 41}, {"name": "Seth Luna", "country": "Sao Tome and Principe", "age": 59}, {"name": "Micheal Adams", "country": "Barbados", "age": 53}, {"name": "Susan Carroll", "country": "Somalia", "age": 64}, {"name": "Douglas Morris", "country": "Thailand", "age": 24}, {"name": "Dennis Wagner", "country": "Zimbabwe", "age": 66}, {"name": "Kristin Johnson", "country": "Niue", "age": 71}, {"name": "Steven Krause", "country": "Turkmenistan", "age": 84}, {"name": "Jared Smith", "country": "Colombia", "age": 46}, {"name": "Lauren Anderson", "country": "Christmas Island", "age": 46}, {"name": "Joshua Spencer", "country": "Russian Federation", "age": 38}, {"name": "Maria Edwards", "country": "Hungary", "age": 78}, {"name": "Anne Lee", "country": "United States of America", "age": 10}, {"name": "James Mckenzie", "country": "Uganda", "age": 43}, {"name": "Joshua Gallegos", "country": "United States Minor Outlying Islands", "age": 27}, {"name": "Paul Herrera", "country": "Kiribati", "age": 17}, {"name": "Veronica White", "country": "Gabon", "age": 88}, {"name": "Michael Hall", "country": "China", "age": 43}, {"name": "Sabrina Thompson", "country": "Chad", "age": 27}, {"name": "Jennifer Archer", "country": "Korea", "age": 45}, {"name": "Christina Simmons", "country": "Israel", "age": 80}, {"name": "Travis White", "country": "Central African Republic", "age": 31}, {"name": "Dennis Hernandez", "country": "Slovenia", "age": 66}, {"name": "Matthew Richards", "country": "Svalbard & Jan Mayen Islands", "age": 34}, {"name": "Stephen Curry", "country": "Finland", "age": 92}, {"name": "Margaret Williamson", "country": "Hong Kong", "age": 86}, {"name": "Mary Estes", "country": "Montenegro", "age": 19}, {"name": "Alex Scott", "country": "Christmas Island", "age": 67}, {"name": "John Andrews", "country": "Bahamas", "age": 68}, {"name": "Jonathan Willis", "country": "Saint Martin", "age": 23}, {"name": "Olivia Campos", "country": "Armenia", "age": 72}, {"name": "Diana Davis", "country": "Azerbaijan", "age": 54}, {"name": "Jack Cummings", "country": "Martinique", "age": 94}, {"name": "Kaitlyn Mcdonald", "country": "Austria", "age": 12}, {"name": "Maria Blake", "country": "Pitcairn Islands", "age": 91}, {"name": "Kelly Thomas", "country": "Ethiopia", "age": 74}, {"name": "John Terrell Jr.", "country": "India", "age": 50}, {"name": "Lindsay Wood", "country": "United Arab Emirates", "age": 72}, {"name": "Matthew Gilbert", "country": "Madagascar", "age": 86}, {"name": "Tanner Johnson", "country": "Congo", "age": 11}, {"name": "Michael Garcia", "country": "Liberia", "age": 45}, {"name": "Nicole Johnson", "country": "Barbados", "age": 54}, {"name": "William Lee", "country": "Lithuania", "age": 59}, {"name": "Jeffrey Coffey", "country": "Faroe Islands", "age": 88}, {"name": "Sandra Freeman", "country": "Philippines", "age": 35}, {"name": "Latoya Maxwell", "country": "Sweden", "age": 12}, {"name": "Darius Blevins", "country": "Thailand", "age": 29}, {"name": "Teresa Newman", "country": "Jersey", "age": 6}, {"name": "Larry Bray", "country": "Brunei Darussalam", "age": 21}, {"name": "Adam Roberson", "country": "Jordan", "age": 71}, {"name": "Michael Gomez", "country": "Tajikistan", "age": 37}, {"name": "Abigail Mccarthy", "country": "Kiribati", "age": 85}, {"name": "Tom Morris", "country": "Cayman Islands", "age": 27}, {"name": "Kevin Wagner", "country": "Suriname", "age": 55}, {"name": "Peggy Bryant", "country": "Korea", "age": 36}, {"name": "Erik Mclaughlin", "country": "Austria", "age": 24}]'

data = json.loads(people)
data = sorted(data, key=lambda k: (k["age"], k["name"]))

[print(f"{i['name']}, {i['country']}, {i['age']}") for i in data]


# 453. Перед вами имеется программа, которая десериализует JSON строку к питоновскому значению.
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