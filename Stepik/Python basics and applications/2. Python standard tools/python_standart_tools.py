# Вашей программе будет доступна функция foo, которая может бросать исключения.
# Вам необходимо написать код, который запускает эту функцию, затем ловит исключения ArithmeticError, AssertionError, ZeroDivisionError и выводит имя пойманного исключения.
# 
# Пример решения, которое вы должны отправить на проверку.
# try:
#     foo()
# except Exception:
#     print("Exception")
# except BaseException:
#     print("BaseException")

try:
    foo()
except ZeroDivisionError:
    print("ZeroDivisionError")    
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")

# Вам дано описание наследования классов исключений в следующем формате.
# <имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
# Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.
# 
# Или эквивалентно записи:
# class Error1(Error2, Error3 ... ErrorK):
#     pass
# 
# Антон написал код, который выглядит следующим образом.
# try:
#    foo()
# except <имя 1>:
#    print("<имя 1>")
# except <имя 2>:
#    print("<имя 2>")
# ...
# 
# Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить, так как ранее в коде будет пойман их предок. 
# Но Антон не помнит какие исключения наследуются от каких. Помогите ему выйти из неловкого положения и напишите программу, 
# которая будет определять обработку каких исключений можно удалить из кода.
# 
# Важное примечание:
# В отличие от предыдущей задачи, типы исключений не созданы. Создавать классы исключений также не требуется
# Мы просим вас промоделировать этот процесс, и понять какие из исключений можно и не ловить, потому что мы уже ранее где-то поймали их предка.
# 
# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов исключений.
# В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. 
# Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), 
# что класс не наследуется явно от одного класса более одного раза.
# В следующей строке содержится число m - количество обрабатываемых исключений.
# Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
# Гарантируется, что никакое исключение не обрабатывается дважды.
# 
# Формат выходных данных
# Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода, не изменив при этом поведение программы. 
# Имена следует выводить в том же порядке, в котором они идут во входных данных.
# 
# Пример теста 1
# Рассмотрим код
# try:
#    foo()
# except ZeroDivision :
#    print("ZeroDivision")
# except OSError:
#    print("OSError")
# except ArithmeticError:
#    print("ArithmeticError")
# except FileNotFoundError:
#    print("FileNotFoundError")
# 
# 
# ...
# По условию этого теста, Костя посмотрел на этот код, и сказал Антону, что исключение FileNotFoundError можно не ловить, ведь мы уже ловим OSError - предок FileNotFoundError

exceptions = {}
throwed_exceptions = []

def found_path(exceptions, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in exceptions:
        return []
    for node in exceptions[start]:
        if node not in path:
            newpath = found_path(exceptions, node, end, path)
            if newpath: return newpath
    return []

n = int(input())
for _ in range(n):
    inpt = input().split()
    child = inpt[0]
    parents = inpt[2:]
    exceptions[child] = parents

m = int(input())
for _ in range(m):
    throwing = input()
    for throwed_exception in throwed_exceptions:
        if len(found_path(exceptions, throwing, throwed_exception)) > 1:
            print(throwing)
            break
    throwed_exceptions.append(throwing)

# Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения положительных целых чисел. Также реализуйте новое исключение NonPositiveError.
# В классе PositiveList переопределите метод append(self, x) таким образом, чтобы при попытке добавить неположительное целое число бросалось исключение NonPositiveError и число не добавлялось, 
# а при попытке добавить положительное целое число, число добавлялось бы как в стандартный list.
# В данной задаче гарантируется, что в качестве аргумента x метода append всегда будет передаваться целое число.
# Примечание: Положительными считаются числа, строго большие нуля.

class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x > 0:
            super().append(x)
        else:
            raise NonPositiveError
        
# В первой строке дано три числа, соответствующие некоторой дате date - год, месяц и день. Во второй строке дано одно число days - число дней.
# Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.
# Примечание:
# Для решения этой задачи используйте стандартный модуль datetime.
# Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta﻿ для прибавления дней к дате.

from datetime import date, timedelta

date = date(*list(map(int, input().split())))
days = timedelta(days = int(input()))
res = date + days
print(res.year, res.month, res.day)

# Алиса владеет интересной информацией, которую хочет заполучить Боб.
# Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
# У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.
# Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями, но он не смог понять какой из паролей ему нужен. Помогите ему решить эту проблему.
# Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
# Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.
# Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать, какой из паролей служит ключом для расшифровки файла с интересной информацией.
# Ответом для данной задачи служит расшифрованная интересная информация Алисы.
# 
# Файл с информацией: encrypted.bin 
# Файл с паролями: passwords.txt

import simplecrypt

with open('passwords.txt', 'r') as file_p:
    passwords = file_p.read()

with open('encrypted.bin', 'rb') as file_e:
    encrypted = file_e.read()

for password in passwords.split():
    try:
        print(simplecrypt.decrypt(password, encrypted).decode('utf-8'))
    except simplecrypt.DecryptionException:
        print(password, 'Incorrect')