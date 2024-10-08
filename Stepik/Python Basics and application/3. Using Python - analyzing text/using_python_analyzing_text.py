# Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
# За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.
#
# Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции строка s перейдет в строку "baba",
# после выполнения двух и операций – в строку "bbaa", и дальнейшие операции не будут изменять строку s.
#
# Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a. Если операций потребуется более 1000, выведите Impossible.
#
# Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a, или Impossible, если операций потребуется более 1000.

s, a, b = [input() for _ in range(3)]
count = 0
while a in s:
    if a in b:
        count = 'Impossible'
        break
    s = s.replace(a, b)
    count += 1
print(count)

# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
# Выведите одно число – количество вхождений строки t в строку s.
# 
# Пример:
# s = "abababa"
# t = "aba"
# 
# Вхождения строки t в строку s:
# abababa
# abababa
# abababa

s, t = [input() for _ in range(2)]
print(sum([1 for i in range(len(s)) if s[i:].startswith(t)]))

# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'((cat).*){2,}', line):
        print(line)

# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве слова.

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'\bcat\b', line):
        print(line)

# Вам дана последовательность строк.
# Выведите строки, содержащие две буквы "z", между которыми ровно три символа.

for line in __import__('sys').stdin:
    line = line.rstrip()
    if __import__('re').search(r'z.{3}z', line):
        print(line)

# Вам дана последовательность строк.
# Выведите строки, содержащие обратный слеш "\".

for line in __import__('sys').stdin:
    line = line.rstrip()
    if __import__('re').search(r'\\', line):
        print(line)

# Вам дана последовательность строк.
# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

for line in __import__('sys').stdin:
    line = line.rstrip()
    if __import__('re').search(r'\b(\w+)\1\b', line):
        print(line)

# Вам дана последовательность строк.
# В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.

for line in __import__('sys').stdin:
    line = line.rstrip()
    print(__import__('re').sub(r'human', 'computer', line))

# Вам дана последовательность строк.
# В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".

for line in __import__('sys').stdin:
    print(__import__('re').sub(r'\b[a]+\b', 'argh', line.rstrip(), 1, __import__('re').I))

# Вам дана последовательность строк.
# В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
# Буквой считается символ из группы \w.

for line in __import__('sys').stdin:
    print(__import__('re').sub(r'\b(\w)(\w)(\w*)\b', r'\2\1\3', line.rstrip()))

# Вам дана последовательность строк.
# В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
# Буквой считается символ из группы \w.

for line in __import__('sys').stdin:
    print(__import__('re').sub(r'(\w)\1+', r'\1', line.rstrip()))

# Рассмотрим два HTML-документа A и B.
# Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
# Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и из C в B можно перейти за один переход.
# 
# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
# 
# Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

a, b = [input() for _ in range(2)]
urls = []
pattern = r'<a.*href="(.*)">'

for url in __import__('re').findall(pattern, __import__('requests').get(a).text):
    urls.extend(__import__('re').findall(pattern, __import__('requests').get(url).text))

urls = list(map(lambda url: url.replace('stepic.org', 'stepik.org'), urls))
print('Yes' if b in urls else 'No')

# Вашей программе на вход подается ссылка на HTML файл.
# Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.
# 
# Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов, которая следует сразу после символов протокола, 
# если он есть, до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида <a href="../some_path/index.html">.
# 
# Сайты следует выводить в алфавитном порядке.

response = __import__('requests').get(input())
pattern = __import__('re').compile(r'<a.*?href=["|\'](.*?:\/\/)?(\w.*?)([/|:].*)?["|\'].*')

domains = [link[1] for link in pattern.findall(response.text)]
[print(domain) for domain in sorted(set(domains))]

# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.
# Одним из атрибутов преступления является его тип – Primary Type.
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
# 
# Файл с данными:
# Crimes.csv

with open("Crimes.csv") as f:
    reader = __import__("csv").reader(f)
    crimes = __import__("collections").Counter(list(zip(*list(reader)[1:]))[5])
    print(crimes.most_common(1)[0][0])

# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле name, которое содержит имя класса, 
# и поле parents, которое содержит список имен прямых предков.
# 
# Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
# 
# Эквивалент на Python:
# 
# class A:
#     pass
# 
# class B(A, C):
#     pass
# 
# class C(A):
#     pass
# 
# Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от одного класса более одного раза.
# Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате: <имя класса> : <количество потомков>
# Выводить классы следует в лексикографическом порядке.

def counter(value):
    for key in tmp_dict:
        if value in tmp_dict[key]:
            s.add(key)
            counter(key)
    return str(len(s) + 1)

tmp_dict = {alpha['name']: alpha['parents'] for alpha in __import__('json').loads(input())}
for key in sorted(tmp_dict):
    s = set()
    print(f"{key} : {counter(key)}")

# В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
# Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.
# Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
# Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
# 
# Пример запроса к интересному числу:
# http://numbersapi.com/31/math?json=true
# 
# Пример запроса к скучному числу:
# http://numbersapi.com/999/math?json=true

with open("dataset_24476_3.txt") as file:
    for number in file:
        number = number.strip()
        params = {"json": True}
        url = f"http://numbersapi.com/{number}/math"
        response = __import__("requests").get(url, params=params)
        if response.json()["found"]:
            print("Interesting")
        else:
            print("Boring")

# В этой задаче вам необходимо воспользоваться API сайта artsy.net
# API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.
# В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).
# 
# Вам даны идентификаторы художников в базе Artsy.
# Для каждого идентификатора получите информацию о имени художника и годе рождения.
# Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения, выведите их имена в лексикографическом порядке.

client_id = "******"
client_secret = "******"

response_artsy = __import__("requests").post("https://api.artsy.net/api/tokens/xapp_token",
                                             data={
                                                 "client_id": client_id,
                                                 "client_secret": client_secret
                                             })

response = __import__("json").loads(response_artsy.text)

token = response["token"]

artists = {}

with open("dataset_24476_4.txt") as file:
    for artist_id in file:
        artist_id = artist_id.strip()
        url = f"https://api.artsy.net/api/artists/{artist_id}"
        headers = {"X-Xapp-Token": token}
        r = __import__("requests").get(url, headers=headers)
        artists[r.json()["sortable_name"]] = int(r.json()["birthday"])

for k, v in sorted(artists.items(), key=lambda x: (x[1], x[0])):
    print(k)

# Вам дано описание пирамиды из кубиков в формате XML.
# Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
# Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.
# 
# Пример:
# <cube color="blue">
#   <cube color="red">
#     <cube color="green">
#     </cube>
#   </cube>
#   <cube color="red">
#   </cube>
# </cube>
#  
# Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 
# 1. Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.
# Ценность цвета равна сумме ценностей всех кубиков этого цвета.
# Выведите через пробел три числа: ценности красного, зеленого и синего цветов.

import xml.etree.ElementTree as ET

tree = ET.fromstring(input())
ans = {"red": 0, "green": 0, "blue": 0}

def dfs(cube, res, depth):
    res[cube.attrib["color"]] += depth
    for i in cube.findall("cube"):
        dfs(i, res, depth + 1)

dfs(tree, ans, 1)
print(ans["red"], ans["green"], ans["blue"])