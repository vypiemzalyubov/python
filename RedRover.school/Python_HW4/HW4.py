# # 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа): 
# #      периметр квадрата, площадь квадрата и диагональ квадрата.

def square(x):
    return ('Периметр квадрата:', x * 4, "Площадь квадрата:", x * x, "Диагональ квадрата:", x * x + x * x)

x = int(input('Введите сторону квадрата: '))
print(square(x))

# # 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно 
# #      в формате аргумент: значение. Например:
# # 	 name: John
# # 	 last_name: Smith
# # 	 age: 35 
# # 	 position: web developer

def file(x):
    dict = {input('Введите аргумент: '):input('Введите значение: ') for _ in range(x)}
    for key, value in dict.items():
        print(key, ':', value)

x = int(input('Введите количество аргументов: '))
file(x)

# # 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только 
# #      положительные числа

my_list = [20, -3, 15, 2, -1, -21]
res_list = list(filter(lambda x: x > 0, my_list))
print(f'Список содержащий положительные числа: {res_list}')

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке

import functools

my_list = [20, -3, 15, 2, -1, -21]
res = functools.reduce(lambda x, y: x * y, my_list)
print(f'Результат перемножения значений в списке my_list: {res}')

# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра

import time

def time_of_func(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print('Время выполнения функции square:', time.perf_counter_ns() - start_time)
        return res
    return wrapped

@time_of_func
def square(x):
    return ('Периметр квадрата:', x * 4, "Площадь квадрата:", x * x, "Диагональ квадрата:", x * x + x * x)

print(square(5))


# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления. 
#      Примените эти функции в качестве методов в другом файле.

import my_calc as my

print(f'Сумма чисел 3 и 7: {my.summation(3, 7)}')
print(f'Разность чисел 40 и 10: {my.subtraction(40, 10)}')
print(f'Умножение 11 на 9: {my.multiplication(11, 9)}')
print(f'Деление 100 на 20: {my.division(100, 20)}')