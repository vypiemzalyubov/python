# 262. Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14×10 в соответствии с образцом:
#
#      **********
#      *        *
#      *        *
#      *        *
#      *        *
#      *        *
#      *        *
#      *        *
#      *        *
#      *        *
#      *        *
#      *        *
#      *        *
#      **********

def draw_box():
    print('*' * 10)
    for i in range(12):
        print('*' + ' ' * 8 + '*')
    print('*' * 10)    


draw_box()

# 263. Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными 10 в соответствии с образцом:
#
#      *
#      **
#      ***
#      ****
#      *****
#      ******
#      *******
#      ********
#      *********
#      **********

def draw_triangle():
    for i in range(11):
        print('*' * i)


draw_triangle()

# 264. Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
#
#      fill – символ заполнитель;
#      base – величина основания равнобедренного треугольника;
#      а затем выводит его.
#
#      Гарантируется, что основание треугольника – нечетное число.

def draw_triangle(fill, base):
    for i in range(base):
        print(fill * min(i + 1, base - i))

fill = input()
base = int(input())

draw_triangle(fill, base)

# 265. Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
#
#      name – имя человека;
#      surname – фамилия человека;
#      patronymic – отчество человека;
#      а затем выводит на печать ФИО человека.
#
#      Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.

def print_fio(name, surname, patronymic):
    print(f"{surname[0]}{name[0]}{patronymic[0]}".upper())

name, surname, patronymic = input(), input(), input()

print_fio(name, surname, patronymic)

# 266. Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.

def print_digit_sum(num):
    print(sum(int(i) for i in str(num)))

n = int(input())

print_digit_sum(n)

# 267. Напишите функцию convert_to_miles(km), которая принимает в качестве аргумента расстояние в километрах и возвращает расстояние в милях. 
#      Формула для преобразования: мили = километры * 0.6214.

def convert_to_miles(km):
    return km * 0.6214

num = int(input())

print(convert_to_miles(num))

# 268. Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце.
#      Гарантируется, что передаваемый аргумент находится в диапазоне от 1 до 12.
#      Считайте, что год является невисокосным.

def get_days(month):
    if month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

num = int(input())

print(get_days(num))

# 269. Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую список всех делителей данного числа.

def get_factors(num):
    res = []
    for i in range(1, num + 1):
        if num % i == 0:
            res.append(i)
    return res        
            
n = int(input())

print(get_factors(n))

# 270. Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую количество делителей данного числа.
#      Используйте уже реализованную функцию get_factors(num) из предыдущей задачи.

def get_factors(num):
    return [i for i in range(1, n + 1) if n % i == 0]

def number_of_factors(num):
    return len(get_factors(num))

n = int(input())

print(number_of_factors(n))

# 271. Напомним, что строковый метод find('a') возвращает местоположение первого вхождения символа a в строке. 
#      Проблема заключается в том, что данный метод не находит местоположение всех символов а.
#      Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: строку target и символ symbol и возвращает список, 
#      содержащий все местоположения этого символа в строке.
#      Если указанный символ не встречается в строке, то следует вернуть пустой список.

def find_all(target, symbol):
    res = [i for i in range(len(target)) if target[i] == symbol]
    return res

s = input()
char = input()

print(find_all(s, char))

# 272. Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два отсортированных по возрастанию списка, состоящих из целых чисел, 
#      и объединяет их в один отсортированный список.
#      Списки list1 и list2 могут иметь разную длину.

def merge(list1, list2):
    for i in list2:
        list1.append(i)
    return sorted(list1)

numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))

# 273. На вход программе подается число n, а затем n строк, содержащих целые числа в порядке возрастания. Из данных строк формируются списки чисел. 
#      Напишите программу, которая объединяет указанные списки в один отсортированный список с помощью функции quick_merge(), а затем выводит его.

n = int(input())

def quick_merge(n):
    return sorted([int(i) for i in range(n) for i in input().split()])

print(*quick_merge(n))

# 274. Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов три натуральных числа, 
#      и возвращает значение True если существует невырожденный треугольник со сторонами side1, side2, side3 и False в противном случае.

def is_valid_triangle(side1, side2, side3):
    if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        return True
    else:
        return False

a, b, c = int(input()), int(input()), int(input())

print(is_valid_triangle(a, b, c))

# 275. Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True если число является простым и False в противном случае.

def is_prime(num):
    return len([i for i in range(1, num + 1) if num % i == 0]) == 2

n = int(input())

print(is_prime(n))

# 276. Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое число большее числа num.

def is_prime(num):
    return len([i for i in range(1, num+1) if num % i == 0]) == 2

def get_next_prime(num):
    j = num + 1
    while is_prime(j) == False:
        j += 1
    return j
        
n = int(input())

print(get_next_prime(n))

# 277. Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является надежным и False в противном случае.
#      Пароль является надежным если:
#      его длина не менее 8 символов; 
#      он содержит как минимум одну заглавную букву (верхний регистр); 
#      он содержит как минимум одну строчную букву (нижний регистр);
#      он содержит хотя бы одну цифру.

def is_password_good(password):
    if len(password) < 8:
        return False
    if password.lower() == password:
        return False
    if password.upper() == password:
        return False
    if password.isalpha():
        return False

    return True
    
txt = input()

print(is_password_good(txt))

# 278. Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2 и возвращает значение True если слова имеют одинаковую длину 
#      и отличаются ровно в 1 символе и False в противном случае.

def is_one_away(word1, word2):
    if len(word1) == len(word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                count += 1
        if len(word1) - count == 1:
            return True
    return False

txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))

# 279. Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True если указанный текст является палиндромом 
#      и False в противном случае.
#      При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы, а также символы , . ! ? -.

def is_palindrome(text):
     text1 = [i.lower() for i in text if i.isalnum()] 
     return text1 == text1[::-1]

txt = input()

print(is_palindrome(txt))

# 280. BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.
#      Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
#      число a – должно быть палиндромом;
#      число b – должно быть простым;
#      число c – должно быть четным.
#      Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password
#      и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.

def is_valid_password(password):
    password = password.split(':')
    a, b, c = password[0], int(password[1]), int(password[2])
    if len(password) != 3 or a != a[::-1] or c % 2 != 0:
        return False
    for i in range(2, b):
        if b % i == 0:
            return False
    return True   
    
psw = input()

print(is_valid_password(psw))

# 281. Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text, состоящую из символов ( и ) 
#      и возвращает значение True если поступившая на вход строка является правильной скобочной последовательностью и False в противном случае.
#      Правильной скобочной последовательностью называется строка, состоящая только из символов ( и ), где каждой открывающей скобке найдется парная закрывающая скобка.

def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
    return len(text) == 0

txt = input()

print(is_correct_bracket(txt))

# 282. Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».

def convert_to_python_case(text):
    for c in text:
        if c.isupper():
            text = text.replace(c, '_' + c.lower())
    return text[1:]

txt = input()

print(convert_to_python_case(txt))

# 283. Напишите функцию get_middle_point(x1, y1, x2, y2), которая принимает в качестве аргументов координаты концов отрезка (x1;y1) и (x2;y2)
#      и возвращает координаты точки являющейся серединой данного отрезка.

def get_middle_point(x1, y1, x2, y2):
    return (x_1 + x_2) / 2, (y_1 + y_2) / 2

x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)

# 284. Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности 
#      и возвращает два значения: длину окружности и площадь круга, ограниченного данной окружностью.

import math

def get_circle(radius):
    return 2 * math.pi * radius, math.pi * radius ** 2

r = float(input())

length, square = get_circle(r)
print(length, square)

# 285. Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа a, b, c – коэффициенты квадратного уравнения 
#      ax**2 + bx + c = 0 и возвращает его корни в порядке возрастания.

def solve(a, b, c):
    d = (b ** 2) - 4 * a * c
    x1 = ((-1 * b) - d ** 0.5) / (2 * a)
    x2 = ((-1 * b) + d ** 0.5) / (2 * a)
    
    return min(x1,x2), max(x1,x2)    

a, b, c = int(input()), int(input()), int(input())

x1, x2 = solve(a, b, c)
print(x1, x2)

# 286. Напишите функцию draw_triangle(), которая выводит звездный равнобедренный треугольник с основанием и высотой равными 15 и 8 соответственно

def draw_triangle():
    for i in range(8):
        print(' ' * (8 - 1 - i) + '*' * (1 + i * 2)) 

draw_triangle()

# 287. Интернет магазин осуществляет экспресс доставку для своих товаров по цене 1000 рублей за первый товар и 120 рублей за каждый последующий товар. 
#      Напишите функцию get_shipping_cost(quantity), которая принимает в качестве аргумента натуральное число quantity – количество товаров в заказе и возвращает стоимость доставки.

def get_shipping_cost(quantity):
    if quantity == 1:
        return 1000
    else:
        return ((quantity -1) * 120) + 1000

n = int(input())

print(get_shipping_cost(n))

# 288. Напишите функцию compute_binom(n, k), которая принимает в качестве аргументов два натуральных числа n и k и возвращает значение биномиального коэффициента

from math import factorial as f

def compute_binom(n, k):
    return f(n) // (f(k) * f(n-k))

n = int(input())
k = int(input())

print(compute_binom(n, k))

# 289. Напишите функцию number_to_words(num), которая принимает в качестве аргумента натуральное число num и возвращает его словесное описание на русском языке.
#      Считайте, что число 1 ≤ num ≤ 99

def number_to_words(num):
    dict = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто','']
    if num <= 20:
        return dict[num - 1]
    else:
        return dict[num // 10 - 1 + 18] + ' ' + dict[num % 10 - 1]


n = int(input())

print(number_to_words(n))

# 290. Напишите функцию get_month(language, number), которая принимает на вход два аргумента 
#      language – язык ru или en и number – номер месяца (от 1 до 12) и возвращает название месяца на русском или английском языке.

def get_month(language, number):
    en = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july',
          8: 'august', 9: 'september', 10: 'october', 11: 'november', 12: 'december'}    
    ru = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль',
          8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}
    if language == 'en':
        return en[number]
    else:
        return ru[number]

lan = input()
num = int(input())

print(get_month(lan, num))

# 291. Магическая дата – это дата, когда день, умноженный на месяц, равен числу образованному последними двумя цифрами года.
#      Напишите функцию, is_magic(date) которая принимает в качестве аргумента строковое представление корректой даты
#      и возвращает значение True если дата является магической и False в противном случае.

def is_magic(date):
     return int(date[0:2]) * int(date[3:5]) == int(date[8:10])

date = input()

print(is_magic(date))

# 292. Панграмма – это фраза, содержащая в себе все буквы алфавита. Обычно панграммы используют для презентации шрифтов, чтобы можно было в одной фразе рассмотреть все глифы.
#      Напишите функцию, is_pangram(text) которая принимает в качестве аргумента строку текста на английском языке и возвращает значение True если текст является панграммой
#      и False в противном случае. Гарантируется, что введенная строка содержит только буквы английского алфавита.

def is_pangram(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text = text.replace(' ', '')
    text = text.lower()
    for i in alphabet:
        if i not in text:
            return False
    return True    

text = input()

print(is_pangram(text))