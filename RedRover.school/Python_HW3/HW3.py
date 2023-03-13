# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3

my_list = ['a', 'b', [1, 2, 3], 'd']
print(*my_list[-2])

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'

list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
summa = 0
stroka = []
for i in list_1:
    if isinstance(i, int):
        summa += i
    if isinstance(i, str) and 'a' in i:
        stroka.append(i)    
print(f'Сумма всех чисел: {summa}', *stroka, sep='\n')

# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж

list2 = ['cat', 'dog', 'horse', 'cow']
print(type(tuple(list2)))

# 3.4. Напишите программу, которая определяет, какая семья больше. 
#       1) Программа имеет два input() - например, family_1, family_2. 
#       2) Членов семьи нужно перечислить через запятую. 
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

family_1 = input('Введите family1: ').split(',')
family_2 = input('Введите family2: ').split(',')
if len(family_1) > len(family_2):
    print(*family_1)
elif len(family_2) > len(family_1):
    print(*family_2)
else:
    print('Equal')

# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме. 
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение

film = {'title': 'Shutter Island', 'director': 'Martin Scorsese', 'year': 2010, 'budget':1000000, 'main_actor':'Di Caprio', 'slogan':'Some places never let you go'}
print(f'{film.keys()}\n{film.values()}\n{film.items()}')

# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(f'Сумма всех значений в словаре: {sum(my_dictionary.values())}')

# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]

list3 = [1, 2, 3, 4, 5, 3, 2, 1]
temp_list = []
[temp_list.append(i) for i in list3 if i not in temp_list]
list3 = temp_list
print(list3)        

# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'} 
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

print(f'Значения, которые встречаются в обоих множествах: {set1.intersection(set2)}')

print('Значения, которые не встречаются в обоих множествах: ', set1.symmetric_difference(set2))

if set1.issubset(set2) == True:
    print('Множества являются подмножествами друг друга')
else:
    print('Множества не являются подмножествами друг друга')    