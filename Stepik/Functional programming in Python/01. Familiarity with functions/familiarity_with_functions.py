# В вашем распоряжении имеются две функции: say_hello и choose_profession
# Ваша задача вызвать сперва say_hello и передать значение Артем, а затем вызвать choose_profession со значением Разработчик

def say_hello(name):
    print(f"Привет, {name}!")

say_hello("Артем")

def choose_profession(profession):
    print(f'Я хочу стать {profession}ом')

choose_profession("Разработчик")

# Программист Сергей любит копипастить чужие программы. Но что-то пошло не так, и Сергей не может понять, почему его программа не запускается.
# В ней явно есть ошибки в определении функции
# Найдите и исправьте все ошибки в коде программы

def welcome_to_course(course_name):
    print("Приветствую")
    print(f'Добро пожаловать на курс "{course_name}"')


welcome_to_course('Функции в Python')

# Напишите функцию repeat_n_times, которая будет печатать на экран фразу «Я стану программистом» n раз.
# Само значение n определенно как параметр функции и поступает при вызове
# Ваша задача только написать определение функции repeat_n_times

def repeat_n_times(n):
    print(*["Я стану программистом" for _ in range(n)], sep="\n")

# Напишите функцию repeat_phrase_n_times, которая имеет два параметра: phrase и n.
# Функция repeat_phrase_n_times должна вывести n раз текст, который был передан в параметр phrase
# Ваша задача только написать определение функции repeat_phrase_n_times

def repeat_phrase_n_times(phrase, n):
    print(f"{phrase}\n" * n)