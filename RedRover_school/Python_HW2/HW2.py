# Задание 2.1
# Напишите программу, которая проверяет здоровье персонажа в игре. 
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.

print(True if int(input('Health: ')) > 0 else False)

# Задание 2.2
# Напишите программу, которая проверяет является ли введенное число четным. Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”

number = int(input('Enter a number: '))
if number % 2 == 0:
    print('Четное')
else:
    print('Нечетное')    

# Задание 2.3
# Напишите программу, которая проверяет является ли год високосным. Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600). 
# Однако, если год делится без остатка на 400, он также считается високосным (1200, 2000)

year = int(input('Enter an year: '))
if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
    print(f'{year} год является високосным')
else:
    print(f'{year} год является невисокосным')    

# Задание 2.4
# Напишите программу, которая печатает введенный текст заданное количество раз, построчно. Текст и количество повторений нужно ввести с помощью input()

text = input('Enter a text: ')
number = int(input('Enter the number of repetitions: '))
for _ in range(number):
    print(text)

# Задание 2.5.
# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str), производит заданное арифметическое действие и печатает результат в формате: 
# {num1} {operator) {num2) = {result}

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
operator = input('Enter a operator: ')    
if operator == '+':
    result = num1 + num2
    print(f'{num1} {operator} {num2} = {result}')
elif operator == '-':
    result = num1 - num2
    print(f'{num1} {operator} {num2} = {result}')
elif operator == '*':
    result = num1 * num2
    print(f'{num1} {operator} {num2} = {result}')
elif operator == '/':
    try:
        result = num1 / num2
        print(f'{num1} {operator} {num2} = {result}')
    except ZeroDivisionError:
        print('You can\'t divide by zero')