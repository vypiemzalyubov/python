# 1. На вход программе подаются два целых числа a и b. Напишите программу, которая выводит:
#    - сумму чисел a и b;
#    - разность чисел a и b;
#    - произведение чисел a и b;
#    - частное чисел a и b;
#    - целую часть от деления числа a на b;
#    - остаток от деления числа a на b;
#    - корень квадратный из суммы их 10-х степеней.
#
#    Формат входных данных
#    На вход программе подаются два целых числа a и b (b не равно 0), каждое на отдельной строке.
#    Формат выходных данных
#    Программа должна вывести результаты математических операций в соответствии с условием задачи.

a, b = int(input()), int(input())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print((a**10 + b**10) ** 0.5)

# 2. Напишите программу для вычисления и оценки индекса массы тела (ИМТ) человека. ИМТ показывает весит человек больше или меньше нормы для своего роста.
#    ИМТ человека рассчитывают по формуле: ИМТ = масса (кг) / рост(м) * рост(м), где масса измеряется в килограммах, а рост — в метрах.
#    Масса человека считается оптимальной, если его ИМТ находится между 18.5 и 25. Если ИМТ меньше 18.5, то считается, что человек весит ниже нормы.
#    Если значение ИМТ больше 25, то считается, что человек весит больше нормы.
#    Программа должна вывести "Оптимальная масса", если ИМТ находится между 18.5 и 25 (включительно). "Недостаточная масса", если ИМТ меньше 18.5
#    и "Избыточная масса", если значение ИМТ больше 25.
#
#    Формат входных данных
#    На вход программе подается два числа: масса и рост человека, каждое на отдельной строке.
#    Все входные числа являются вещественными, используйте для них тип данных float.
#    Формат выходных данных
#    Программа должна вывести текст в соответствии с условием задачи.

weight, height = float(input()), float(input())
imt = weight / (height**2)
if 18.5 <= imt <= 25:
    print("Оптимальная масса")
elif imt < 18.5:
    print("Недостаточная масса")
else:
    print("Избыточная масса")

# 3. Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ (в том числе пробел) стоит 60 копеек.
#    Ответ дайте в рублях и копейках в соответствии с примерами.
#
#    Формат входных данных
#    На вход программе подается строка текста.
#    Формат выходных данных
#    Программа должна вывести стоимость строки.

s = input()
cost = len(s) * 60
rouble = cost // 100
penny = cost % 100
print(f"{rouble} р. {penny} коп.")

# 4. Дана строка, состоящая из слов, разделенных пробелами. Напишите программу, которая подсчитывает количество слов в этой строке.
#
#    Формат входных данных
#    На вход программе подается строка.
#    Формат выходных данных
#    Программа должна вывести количество слов в строке.
#    Примечание 1. Кроме слов в тексте могут присутствовать только пробелы (один или несколько).
#    Примечание 2. Решите задачу в одну строчку кода 😎.

print(len(input().split()))

# 5. Китайский гороскоп назначает животным годы в 12-летнем цикле. Один 12-летний цикл показан в таблице ниже. Таким образом, 2012 год будет очередным годом дракона.
#    Напишите программу, которая считывает год и отображает название связанного с ним животного. Ваша программа должна корректно работать с любым годом, не только теми, что перечислены в таблице.
#
#    Формат входных данных
#    На вход программе подается одно целое число – год.
#    Формат выходных данных
#    Программа должна вывести текст – название животного.

match int(input()) % 12:
    case 8:
        print("Дракон")
    case 9:
        print("Змея")
    case 10:
        print("Лошадь")
    case 11:
        print("Овца")
    case 0:
        print("Обезьяна")
    case 1:
        print("Петух")
    case 2:
        print("Собака")
    case 3:
        print("Свинья")
    case 4:
        print("Крыса")
    case 5:
        print("Бык")
    case 6:
        print("Тигр")
    case 7:
        print("Заяц")

# 6. Дано пятизначное или шестизначное натуральное число. Напишите программу, которая изменит порядок его последних пяти цифр на обратный.
#
#    Формат входных данных
#    На вход программе подается одно натуральное пятизначное или шестизначное число.
#    Формат выходных данных
#    Программа должна вывести число, которое получится в результате разворота, указанного в условии задачи. Число нужно выводить без незначащих нулей.

if len(x := input()) == 5:
    print(x[::-1].lstrip("0"))
else:
    print((x[0] + x[:0:-1]).lstrip("0"))

# 7. На вход программе подаётся натуральное число. Напишите программу, которая вставляет в заданное число запятые
#    в соответствии со стандартным американским соглашением о запятых в больших числах.
#
#    Формат входных данных
#    На вход программе подаётся натуральное число n,(0 < n < 10**100).
#    Формат выходных данных
#    Программа должна вывести число с запятыми в соответствии с условием задачи.

print("{:,}".format(int(input())))

# 8. n человек, пронумерованных числами от 1 до n, стоят в кругу. Они начинают считаться, каждый k-й по счету человек выбывает из круга,
#    после чего счет продолжается со следующего за ним человека. Напишите программу, определяющую номер человека, который останется в кругу последним.
#
#    Формат входных данных
#    На вход программе подаются два числа n и k, записанные на отдельных строках.
#    Формат выходных данных
#    Программа должна вывести одно число – номер человека, который останется в кругу последним.

n, k = int(input()), int(input())
res = 0
for i in range(1, n + 1):
    res = (res + k) % i
print(res + 1)

# 9. Дан набор точек на координатной плоскости. Необходимо подсчитать и вывести количество точек, лежащих в каждой координатной четверти.
#
#    Формат входных данных
#    В первой строке записано количество точек. Каждая следующая строка состоит из двух целых чисел — координат точки
#    (сначала абсцисса – x, затем ордината – y), разделенных символом пробела.
#    Формат выходных данных
#    Программа должна вывести количество точек, лежащих в каждой координатной четверти, как в примерах.
#    Примечание. Учтите, что точки, лежащие на осях координат, не принято относить к какой-либо координатной четверти.

result = {"1": 0, "2": 0, "3": 0, "4": 0}
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        continue
    elif x > 0 and y > 0:
        result["1"] += 1
    elif x < 0 and y > 0:
        result["2"] += 1
    elif x < 0 and y < 0:
        result["3"] += 1
    else:
        result["4"] += 1
print(f"""Первая четверть: {result["1"]}
Вторая четверть: {result["2"]}
Третья четверть: {result["3"]}
Четвертая четверть: {result["4"]}""")

# 10. На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел.
#     Напишите программу подсчета количества чисел, которые больше предшествующего им в этом списке числа.
#
#     Формат входных данных
#     На вход программе подается строка текста из разделенных пробелами натуральных чисел.
#     Формат выходных данных
#     Программа должна вывести одно число – количество элементов списка, больших предыдущего.
#     Примечание. Разберём первый тест. У нас формируется список [1, 2, 3, 4, 5], в нём 2>1, 3>2,  4>3, 5>4.
#     То есть получается 4 таких случая, где текущее число больше предыдущего. Поэтому ответ 4.

lst = list(map(int, input().split()))
count = 0
for i in range(len(lst)):
    if i != 0 and lst[i] > lst[i - 1]:
        count += 1
print(count)

# 11. На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел.
#     Напишите программу, которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.).
#     Если в списке нечетное количество элементов, то последний остается на своем месте.
#
#     Формат входных данных
#     На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.
#     Формат выходных данных
#     Программа должна вывести измененный список, разделяя его элементы одним пробелом.

lst = list(map(int, input().split()))
for i in range(1, len(lst), 2):
    lst[i], lst[i - 1] = lst[i - 1], lst[i]
print(*lst)

# 12. На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел.
#     Напишите программу циклического сдвига элементов списка направо, когда последний элемент становится первым,
#     а остальные сдвигаются на одну позицию вперед, в сторону увеличения индексов.
#
#     Формат входных данных
#     На вход программе подается строка текста из разделенных пробелами натуральных чисел.
#
#     Формат выходных данных
#     Программа должна вывести элементы измененного списка с циклическим сдвигом, разделяя его элементы одним пробелом.

lst = list(map(int, input().split()))
print(lst[-1], *lst[:-1])

# 13. На вход программе подается строка текста, содержащая натуральные числа, расположенные по неубыванию. Из строки формируется список чисел.
#     Напишите программу для подсчета количества разных элементов в списке.
#
#     Формат входных данных
#     На вход программе подается строка текста, содержащая натуральные числа, разделенные символом пробела, расположенные по неубыванию.
#
#     Формат выходных данных
#     Программа должна вывести одно число – количество различных элементов списка.

print(len(set(map(int, input().split()))))

# 14. Напишите программу для определения, является ли число произведением двух чисел из данного набора. Программа должна выводить результат в виде ответа «ДА» или «НЕТ».
#
#     Формат входных данных
#     В первой строке подаётся число n(0 < n < 1000) – количество чисел в наборе. В последующих n строках вводятся целые числа, составляющие набор (могут повторяться).
#     Затем следует целое число, которое является или не является произведением двух каких-то чисел из набора.
#
#     Формат выходных данных
#     Программа должна вывести «ДА» или «НЕТ» в соответствии с условием задачи.
#
#     Примечание 1. Само на себя число из набора умножиться не может. Другими словами, два множителя должны иметь разные индексы в наборе.
#     Примечание 2. Для решения задачи используйте вложенные циклы.

lst = [int(input()) for _ in range(int(input()))]
x = int(input())
flag = False
for i in range(len(lst)):
    for j in range(len(lst)):
        if i == j:
            continue
        if lst[i] * lst[j] == x:
            flag = True
            break
print("ДА") if flag else print("НЕТ")

# 15. Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов". Для этого они решили сыграть в камень, ножницы и бумагу.
#     Помогите ребятам бросить честный жребий и определить, кто будет делать очередной модуль нового курса.
#
#     Формат входных данных
#     На вход программе подаются две строки текста, содержащие слова "камень", "ножницы" или "бумага". На первой строке записан выбор Тимура, на второй – выбор Руслана.
#
#     Формат выходных данных
#     Программа должна вывести результат жеребьёвки, то есть кто победит: Тимур, Руслан или же они сыграют вничью.
#
#     Примечание. Правила игры стандартные: камень побеждает ножницы, но проигрывает бумаге, а ножницы побеждают бумагу.

match input(), input():
    case "камень", "бумага":
        print("Руслан")
    case "бумага", "камень":
        print("Тимур")
    case "ножницы", "камень":
        print("Руслан")
    case "камень", "ножницы":
        print("Тимур")
    case "бумага", "ножницы":
        print("Руслан")
    case "ножницы", "бумага":
        print("Тимур")
    case _:
        print("ничья")

# 16. Проиграв 10 раз Тимуру, Руслан понял, что так дело дальше не пойдет, и решил усложнить игру. Теперь Тимур и Руслан играют в игру Камень, ножницы, бумага, ящерица, Спок.
#     Помогите ребятам вновь бросить честный жребий и определить, кто будет делать следующий модуль в новом курсе.
#
#     Формат входных данных
#     На вход программе подаются две строки текста, содержащие по одному слову из перечня "камень", "ножницы", "бумага", "ящерица" или "Спок".
#     На первой строке записан выбор Тимура, на второй – выбор Руслана.
#
#     Формат выходных данных
#     Программа должна вывести результат жеребьёвки: кто победил - Тимур или Руслан, или они сыграли вничью.
#
#     Примечание. Правила игры стандартные: ножницы режут бумагу. Бумага заворачивает камень. Камень давит ящерицу, а ящерица травит Спока,
#     в то время как Спок ломает ножницы, которые, в свою очередь, отрезают голову ящерице, которая ест бумагу, на которой улики против Спока.
#     Спок испаряет камень, а камень, разумеется, затупляет ножницы.

tim, rus = input(), input()

choices = ["камень", "ящерица", "Спок", "ножницы", "бумага"]
result = ["ничья", "Руслан", "Тимур", "Руслан", "Тимур"]

print(result[choices.index(tim) - choices.index(rus)])

# 17. Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" соответствует выпадению Орла, а буква "Р" - выпадению Решки.
#     Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
#
#     Формат входных данных
#     На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
#
#     Формат выходных данных
#     Программа должна вывести наибольшее количество подряд выпавших Решек.
#
#     Примечание. Если выпавших Решек нет, то необходимо вывести число 0.

s = input().split("О")
print(len(max(s)))

# 18. Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника".
#     Помогите владельцу фирмы отыскать все зараженные холодильники. Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр,
#     и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен
#     и нужно вывести номер холодильника, нумерация начинается с единицы.
#
#     Формат входных данных
#     В первой строке подаётся число n – количество холодильников. В последующих n строках вводятся строки, содержащие латинские строчные буквы и цифры,
#     в каждой строке от 5 до 100 символов.
#
#     Формат выходных данных
#     Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.

lst = [input() for _ in range(int(input()))]
for k, v in enumerate(lst, start=1):
    if __import__("re").search(r"a.*n.*t.*o.*n", v):
        print(k, end=" ")

# 19. Необходимо написать программу, реализующую алгоритм написания этой песни. Алгоритм выводит в конце предложения следующую в алфавитном порядке букву,
#     если она встречается в строке текста, а очередную строку отображает уже без этой буквы.
#
#     Формат входных данных
#     На вход программе подается одно слово, записанное строчными русскими буквами без буквы "ё".
#
#     Формат выходных данных
#     Программа должна вывести в соответствии с указанным алгоритмом строки, количество которых равно количеству разных букв в строке,
#     которая получается путем конкатенации введенного слова и строки "запретил букву".
#
#     Примечание 1. Текст исходной песни в первом тесте.
#     Примечание 2. Поем и решаем, друзья, поем и решаем 😂.

word = f"{input()} запретил букву"
for i in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
    if i in word:
        print(" ".join(word.split()), i)
        word = word.replace(i, "")
