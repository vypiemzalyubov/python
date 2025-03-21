# Перепишите рекурсивную функцию speller так, чтобы она выводила буквы слова в обратном порядке (каждую букву на новой строке)

def speller(word):
    if len(word) > 0:
        speller(word[1:])
        print(word[0])

# Определите функцию print_from, которая принимает одно натуральное число n и распечатывает на экране убывающую последовательность целых чисел от n до 1 включительно.
# Каждое число необходимо выводить на отдельной строке. Ваша задача только написать определение функции print_from

def print_from(n):
    if n < 1:
        return
    print(n)
    print_from(n - 1)

# Определите функцию print_to, которая принимает одно натуральное число n и распечатывает на экране последовательность целых чисел от 1 до n включительно.
# Каждое число необходимо выводить на отдельной строке. Ваша задача только написать определение функции print_to

def print_to(n):
    if n > 0:
        print_to(n - 1)
        print(n)

# Напишите рекурсивную функцию summa, которая будет суммировать все числа от 1 до N. Число N поступает внутрь функции в качестве аргумента

def summa(n):
    if n == 0:
        return 0
    return n + summa(n - 1)

# Напишите рекурсивную функцию find_min, которая найдет наименьшее число в списке.
# Для этого функция принимает в качестве аргумента список для поиска наименьшего значения

def find_min(lst):
    if len(lst) == 0:
        return
    elif len(lst) == 1:
        return lst[0]
    return lst[0] if lst[0] < find_min(lst[1:]) else find_min(lst[1:])

# Напишите функцию sum_recursive, которая принимает на вход одномерный список из целых чисел и возвращает сумму элементов переданного списка.
# Не забывайте, что реализовать это нужно при помощи рекурсии. Ваша задача только написать определение функции sum_recursive

def sum_recursive(lst):
    if len(lst) == 0:
        return
    elif len(lst) == 1:
        return lst[0]
    return lst[0] + sum_recursive(lst[1:])

# Напишите функцию sum_digits, которая находит сумму всех цифр переданного натурального числа n.
# Ваша задача только написать определение функции sum_digits

def sum_digits(n):
    if n <= 0:
        return n
    return n % 10 + sum_digits(n // 10)

# Необходимо написать рекурсивную функцию double_fact, которая принимает на вход целое число и вычисляет значение двойного факториала по формуле.
# Ваша задача только написать определение функции double_fact

def double_fact(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return n * double_fact(n - 2)

# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где число, стоящее на n-ой позиции можно вычислить по формуле.
# Требуется найти N-е число Фибоначчи при помощи рекурсивной функции fibonacci. Функция должна принимать порядковый номер N и возвращать N-ое число Фибоначчи.
# Ваша задача только написать определение функции fibonacci

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Ваша задача - написать рекурсивную функцию tribonacci, которая принимает на вход целое число n - порядковый номер чисел Трибоначчи.
# Функция по параметру n должна вычислить и вернуть значение, стоящее на n-м месте в ряде чисел Трибоначчи.
# Ваша задача только написать определение функции tribonacci

def tribonacci(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

# Ваша задача - написать рекурсивную функцию get_combin, которая принимает на вход два целых числа
# и находит C(N,K) — число сочетаний из N элементов по K — с помощью рекуррентного соотношения.
# При этом гарантируется, что входные значения n и k будут удовлетворять следующим условиям:
# - n>0
# - 0<=k<=n
# Ваша задача только написать определение функции get_combin.
# В тестовых примерах в функцию get_combin сперва передается значение параметра n, затем k.

def get_combin(n, k):
    if k == n or k == 0:
        return 1
    elif 0 < k < n:
        return get_combin(n - 1, k) + get_combin(n - 1, k - 1)
    
# Ваша задача - написать рекурсивную функцию ackermann, которая принимает на вход два целых числа  m и n, и находит значение, определенное следующим образом.
# Найденное значение функция ackermann должна вернуть в качестве результата. Ваша задача только написать определение функции ackermann.
# В тестовых примерах в функцию сперва передается значение параметра m, затем n.

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))
    
# Перепишите реализацию функции is_member через рекурсию. Напоминаю, функция is_member  должна проверять, есть ли значение value в линейном списке lst.
# Функция is_member должна вернуть True, если значение value присутствует в списке lst, и False в противном случае.
# Гарантируется, что список lst не будет вложенным

def is_member(value, lst):
    if not lst:
        return False
    elif value == lst[0]:
        return True
    return is_member(value, lst[1:])

# Перед вами функция power, которая при помощи итерации возводит параметр a в степень n
# def power(a: int, n: int) -> int:
#     total = 1
#     for i in range(n):
#         total *= a
#     return total
# Перепишите реализацию функции power с итерации на рекурсию. Названии функции и параметры не должны меняться

def power(a, n):
    if n < 1:
        return 1
    return a * power(a, n - 1)

# Перед вами реализация функции gcd, которая находит наибольший общий делитель при помощи итерации
# def gcd(a: int, b: int) -> int:
#     while b:
#         a, b = b, a % b
#     return a
# Перепишите данную программу при помощи рекурсии

def gcd(a, b):
    if b != 0:
        a, b = b, a % b
        return gcd(a, b)
    return a

# Напишите рекурсивную функцию is_palindrome, которая при помощи рекурсии определяет, является ли переданное слово палиндромом.
# Во время проверок регистр букв не учитывайте. В тестовых данных используются только символы английского алфавита. Знаки пунктуации и пробелы отсутствуют.

def is_palindrome(s):
    s = s.lower()
    if len(s) < 2:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False

# Последовательность, в которой каждый следующий член можно найти, прибавив к предыдущему одно и то же число d, называется арифметической прогрессией.
# Рассмотрим вполне определенную арифметическую прогрессию: 1,8,15,22,29,36,....
# Здесь первый элемент последовательности равен 1, второй - 8 и т.д. Каждый следующий элемент получается путем прибавления семи к предыдущему
# Ваша задача написать рекурсивную функцию get_arith_progression, которая принимает число n и возвращает n-ое число указанной выше арифметической прогрессии.

def get_arith_progression(n):
    if n < 2:
        return n
    return get_arith_progression(n - 1) + 7

# В предыдущей задаче на арифметическую прогрессию мы имели дело с одной определенной последовательностью 1,8,15,22,29,36,....
# В ней первый элемент был равен 1, а разность прогрессии d была равна 7.
# Теперь ваша задача написать функцию get_arith_progression так, чтобы она могла находить n-ое число для произвольной арифметической последовательности.
# Для этого функция get_arith_progression должна иметь следующие обязательные параметры:
# - a1 - первый элемент последовательности
# - d - разность последовательности
# - n - порядковый номер элемента, который необходимо найти в арифметической прогрессии.
# Например, вызов get_arith_progression(4, 2, 3)  подразумевает, что нужно найти 3-й элемент в арифметической последовательности,
# которая начинается с 4-х и имеет разность прогрессии 2. Такая последовательность будет иметь следующие элементы 4,6,8,10,12,14,....
# Третьим элементом будет число 8. Ваша задача написать рекурсивную функцию get_arith_progression

def get_arith_progression(a1, d, n):
    if n == 1:
        return a1
    return get_arith_progression(a1, d, n - 1) + d

# Реализуйте рекурсивный алгоритм быстрого возведения в степень.
# Если нам требуется возвести некоторое число 𝑎 в степень 𝑛, где 𝑛 — положительное целое число, мы можем руководствоваться следующими принципами:
# - если 𝑛 четное, то мы можем представить результат 𝑎 в степени 𝑛 как a**n=a**n/2*a**n/2=a**(n/2)
# - если 𝑛 нечетное, то 𝑎 в степени 𝑛 можно найти как a**n=a**n−1*a
# При этом  𝑛−1 гарантированно станет четным числом и тогда на следующем этапе можно будет воспользоваться формулой выше для четных 𝑛.
# Базовым случаем для операции возведения в данной задаче будет являться нулевая степень числа. Любое число в нулевой степени равно 1.
# Напишите рекурсивную функцию quick_power, которая реализует алгоритм быстрого возведения в степень
# Для проверки правильности работы вашего алгоритма выведите в самом начале функции quick_power состояние параметров a и n  в следующем формате
# State: a=<value>, n=<value>

def quick_power(a, n):
    print(f'State: a={a}, n={n}')
    if n == 0:
        return 1
    elif n % 2 == 0:
        return quick_power(a, n // 2) ** 2
    return a * quick_power(a, n - 1)