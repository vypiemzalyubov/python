# 90. На летних каникулах Тимур и ученики онлайн-школы BEEGEEK решили отдохнуть. В результате n учеников школы поехали отдыхать на море, 
#     m учеников съездили в деревню, а k учеников сходили в горы. Оказалось, что и в деревне, и на море были x учеников, а в деревне и в горах — y учеников. 
#     Побывать и в горах, и на море не удалось никому. Напишите программу для определения количества учеников в школе, если никто не смог посетить все три места сразу, а 
#     z учеников писали ДВИ по математике для поступления в МГУ, и никуда не ездили.
# 
#     Формат входных данных
#     На вход программе подаются числа n,m,k,x,y,z, каждое на отдельной строке.
# 
#     Формат выходных данных
#     Программа должна вывести одно число в соответствии с условием задачи.
# 
#     Примечание. n – все ученики, которые поехали на море, m – все ученики, которые съездили в деревню, и k – все ученики, которые сходили в горы.

n, m, k, x, y, z = [int(input()) for _ in range(6)]
print(n + m - x + k - y + z)

# 91. Ученики 10 класса онлайн-школы BEEGEEK получили задание прочесть на летних каникулах три книги:
#     - "Что такое математика?";
#     - "Математическая составляющая";
#     - "100 гениальных идей по математике".
#     Оказалось, что n учеников прочитали первую книгу, m учеников — вторую, k учеников — третью. 
#     Также известно, что x учеников прочли первую или вторую, или обе эти книги, y учеников — вторую или третью, или обе, z учеников — первую и третью, 
#     или хотя бы одну из этих двух книг. Полностью выполнили задание только t учеников. Всего в 10 классе учится a учеников. 
#     Напишите программу, которая выводит сколько учеников:
#     - прочитали только одну книгу;
#     - прочитали две книги;
#     - не прочитали ни одной из рекомендованных книг.
# 
#     Формат входных данных
#     На вход программе подаются числа n,m,k,x,y,z,t,a, каждое на отдельной строке.
# 
#     Формат выходных данных
#     Программа должна вывести три числа в соответствии с условием задачи, каждое на отдельной строке.

n, m, k, x, y, z, t, a = (int(input()) for i in range(8))
r1 = n + m - x - t
r2 = m + k - y - t
r3 = k + n - z - t
r = (n - r1 - r3 - t) + (m - r1 - r2 - t) + (k - r2 - r3 - t)
print(r, r1 + r2 + r3, a - r - r1 - r2 - r3 -t, sep='\n')

# 92. Дополните приведенный код так, чтобы он вывел сумму минимального и максимального элементов множества numbers.

numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
print(min(numbers) + max(numbers))

# 93. Дополните приведенный код, чтобы он вывел среднее арифметическое элементов множества numbers.

numbers = {20, 6, 8, 18, 18, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 12, 8, 8, 10, 4, 2, 2, 2, 16, 20}
average = sum(numbers) / len(numbers)
print(average)

# 94. Дополните приведенный код, чтобы он вывел сумму квадратов элементов множества numbers.

numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
print(sum({i ** 2 for i in numbers}))

# 95. Дополните приведенный код, чтобы он вывел элементы множества fruits, каждый на отдельной строке, отсортированные по убыванию (в обратном лексикографическом порядке).
#     Примечание. Выводите каждый элемент множества на отдельной строке.

fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
print(*sorted({i for i in fruits}, reverse=True), sep='\n')

# 96. На вход программе подается строка текста. Напишите программу, которая определяет количество различных символов в строке.
# 
#     Формат входных данных
#     На вход программе подается строка текста.
# 
#     Формат выходных данных
#     Программа должна вывести количество различных символов в строке.
# 
#     Примечание. Задачу можно решить в одну строчку кода.

print(len(set(input())))

# 97. На вход программе подается строка, состоящая из цифр. Необходимо определить, верно ли, что в ее записи ни одна из цифр не повторяется?
# 
#     Формат входных данных
#     На вход программе подается строка, состоящая из цифр
# 
#     Формат выходных данных
#     Программа должна вывести YES если ни одна из цифр в строке не повторяется и NO в противном случае.

print('YES') if len(s := input()) == len(set(s)) else print('NO')

# 98. На вход программе подаются две строки, состоящие из цифр. Необходимо определить, верно ли, что в записи этих двух строк используются все десять цифр?
# 
#     Формат входных данных
#     На вход подаются две строки, состоящие из цифр.
# 
#     Формат выходных данных
#     Программа должна вывести YES, если в записи этих двух строк используются все десять цифр, и NO в противном случае.

s1, s2 = list(map(int, set(input()))), list(map(int, set(input())))
flag = True

for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    if i not in s1 and i not in s2:
        flag = False
        
print('YES') if flag else print('NO') 

# 99. На вход программе подаются две строки, состоящие из цифр. Необходимо определить, верно ли, что для записи этих строк были использованы одинаковые наборы цифр?
# 
#     Формат входных данных
#     На вход подаются две строки, состоящие из цифр.
# 
#     Формат выходных данных
#     Программа должна вывести YES, если для записи этих строк были использованы одинаковые наборы цифр и NO, в противном случае.

print('YES' if set(input()) == set(input()) else 'NO')

# 100. На вход программе подается строка, состоящая из трех слов. Верно ли, что для записи всех трех слов был использован один и тот же набор букв?
# 
#      Формат входных данных
#      На вход программе подается строка, состоящая из трех слов.
# 
#      Формат выходных данных
#      Программа должна вывести YES, если для записи всех трех слов был использован один и тот же набор букв и NO в противном случае.

s = input().split()
print('YES' if set(s[0]) == set(s[1]) == set(s[2]) else 'NO')

# 101. Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.
# 
#      Формат входных данных
#      На вход программе в первой строке подается число n – общее количество слов. Далее идут n строк с словами.
# 
#      Формат выходных данных
#      Программа должна вывести на отдельной строке количество уникальных символов для каждого слова.

print(*[len(set(input().lower())) for _ in range(int(input()))], sep='\n')

# 102. Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.
# 
#      Формат входных данных
#      На вход программе в первой строке подается число n – общее количество слов. Далее идут n строк со словами.
# 
#      Формат выходных данных
#      Программа должна вывести одно число – общее количество уникальных символов во всех словах без учета регистра.

tmp = [input().lower() for i in range(int(input()))]
x = []
for i in range(len(tmp)-1):
    x += tmp[i] + tmp[i+1]
print(len(set(x)))

# 103. Напишите программу для определения общего количества различных слов в строке текста.
# 
#      Формат входных данных
#      На вход программе подается строка текста.
# 
#      Формат выходных данных
#      Программа должна вывести одно число – общее количество различных слов в строке без учета регистра.
# 
#      Примечание 1. Словом считается последовательность непробельных символов, идущих подряд, слова разделены одним или большим числом пробелов.
#      Примечание 2. Знаками препинания .,;:-?! пренебрегаем.

print(len(set(__import__('re').sub(r'[.,;:-?-!]', '', input().lower()).split())))

# 104. На вход программе подается строка текста, содержащая числа. Для каждого числа выведите слово YES (в отдельной строке), 
#      если это число ранее встречалось в последовательности или NO, если не встречалось.
# 
#      Формат входных данных
#      На вход программе подается строка текста, содержащая числа, разделенные символом пробела.
# 
#      Формат выходных данных
#      Программа должна вывести текст в соответствии с условием задачи.
# 
#      Примечание. Ведущие нули в числах должны игнорироваться.

numbers = list(map(int, input().split()))
s = set()

for i in numbers:
    if i not in s:
        s.add(i)
        print('NO')
    else:
        print('YES')

# 105. На вход программе подаются две строки текста, содержащие числа. 
#      Напишите программу, которая определяет количество чисел, которые есть как в первой строке, так и во второй.
# 
#      Формат входных данных
#      На вход программе подаются две строки текста, содержащие числа, отделенные символом пробела.
# 
#      Формат выходных данных
#      Программа должна вывести количество чисел, содержащихся одновременно как в первой строке, так и во второй.

print(len(set(input().split()) & set(input().split())))

# 106. На вход программе подаются две строки текста, содержащие числа. 
#      Напишите программу, которая выводит все числа в порядке возрастания, которые есть как в первой строке, так и во второй.
# 
#      Формат входных данных
#      На вход программе подаются две строки текста, содержащие числа, отделенные символом пробела.
# 
#      Формат выходных данных
#      Программа должна вывести на одной строке через пробел числа, встречающиеся в обеих строках.

print(*sorted(set(map(int, input().split())) & set(map(int, input().split()))), sep=' ')

# 107. На вход программе подаются две строки текста, содержащие числа. 
#      Напишите программу, которая выводит все числа в порядке возрастания, которые есть в первой строке, но отсутствуют во второй.
# 
#      Формат входных данных
#      На вход программе подаются две строки текста, содержащие числа, отделенные символом пробела.
# 
#      Формат выходных данных
#      Программа должна вывести множество чисел, встречающихся только в первой строке.

print(*sorted(set(map(int, input().split())) - set(map(int, input().split()))))

# 108. На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке. 
#      Напишите программу, которая выводит все общие цифры в порядке возрастания у всех введенных чисел.
# 
#      Формат входных данных
#      На вход программе подаются натуральное число n≥1, а затем n различных натуральных чисел, каждое на отдельной строке.
# 
#      Формат выходных данных
#      Программа должна вывести цифры в соответствии с условием задачи. Если общих цифр нет, то ничего выводить не нужно.

lst = [set(input()) for _ in range(int(input()))]
print(*sorted(set.intersection(*lst)), sep=' ')

# 109. На вход программе подаются два числа. Напишите программу, определяющую, есть ли в данных числах одинаковые цифры.
# 
#      Формат входных данных
#      На вход программе подаются два натуральных числа, каждое на отдельной строке.
# 
#      Формат выходных данных
#      Программа должна вывести YES, если в записи данных чисел есть одинаковые цифры и NO если нет.

print('NO' if set(input()).isdisjoint(set(input())) else 'YES')

# 110. На вход программе подаются два числа. Напишите программу, которая определяет, входят ли в запись первого числа все цифры, 
#      содержащиеся в записи второго (независимо от повтора, то есть количества цифр) числа или нет.
# 
#      Формат входных данных
#      На вход программе подаются два натуральных числа, каждое на отдельной строке.
# 
#      Формат выходных данных
#      Программа должна вывести YES, если в запись первого числа входят все цифры, содержащиеся в записи второго числа и NO в противном случае.

print('YES' if set(input()).issuperset(set(input())) else 'NO')

# 111. Даны по 10-балльной шкале оценки по информатике трех учеников. 
#      Напишите программу, выводящую множество оценок, которые есть и у первого, и у второго учеников, но которых нет у третьего ученика.
# 
#      Формат входных данных
#      На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого ученика на отдельной строке).
# 
#      Формат выходных данных
#      Программа должна вывести множество оценок в порядке убывания на одной строке, разделенных пробелами, в соответствии с условием задачи.
# 
#      Примечание. Оценка ученика находится в диапазоне от 0 до 10 включительно.

s1, s2, s3 = [set(input().split()) for _ in range(3)]
print(*sorted(s1.intersection(s2).difference(s3), reverse=True, key=int))

# 112. Даны оценки по математике трёх учеников в 10-балльной шкале. Напишите программу, которая выводит такие оценки, которые встречаются не более, чем у двух учеников.
# 
#      Формат входных данных
#      На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого ученика на отдельной строке).
# 
#      Формат выходных данных
#      Программа должна вывести множество оценок в порядке возрастания на одной строке, разделенных пробелами, в соответствии с условием задачи.
# 
#      Примечание. Оценка ученика находится в диапазоне от 0 до 10 включительно.

s1, s2, s3 = [set(input().split()) for _ in range(3)]
print(*sorted(s1.union(s2, s3) - s1.intersection(s2).intersection(s3), key=int))

# 113. Даны по 10-балльной шкале оценки по физике трех учеников. 
#      Напишите программу, которая выводит множество оценок третьего ученика, которые не встречаются ни у первого, ни у второго ученика.
# 
#      Формат входных данных
#      На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого ученика на отдельной строке).
# 
#      Формат выходных данных
#      Программа должна вывести множество оценок в порядке убывания на одной строке, разделенных пробелами, в соответствии с условием задачи.
# 
#      Примечание. Оценка ученика находится в диапазоне от 0 до 10 включительно.

s1, s2, s3 = (set(int(i) for i in input().split()) for _ in range(3))
print(*sorted(s3.difference(s1, s2), reverse=True))

# 114. Даны по 10-балльной шкале оценки по биологии трех учеников. 
#      Напишите программу, которая выводит множество оценок, не встречающихся ни у одного из трех учеников.
# 
#      Формат входных данных
#      На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого ученика на отдельной строке).
# 
#      Формат выходных данных
#      Программа должна вывести множество оценок в порядке возрастания на одной строке, разделенных пробелами, в соответствии с условием задачи.
# 
#      Примечание. Оценка ученика находится в диапазоне от 0 до 10 включительно.

s1, s2, s3 = (set(int(i) for i in input().split()) for _ in range(3))
print(*sorted(set(range(11)) - s1.union(s2, s3)))

# 115. Используя генератор множеств, дополните приведенный код так, чтобы получить множество, содержащее уникальные значения списка items. 
#      Результат вывести на одной строке, в упорядоченном виде, разделяя элементы одним символом пробела.
# 
#      Примечание 1. Обратите внимание, некоторые элементы списка – числа, а некоторые – строки, при этом строки необходимо трактовать как числа.
#      Примечание 2. Чтобы вывести элементы множества в упорядоченном виде используйте следующий код: print(*sorted(myset))

items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
print(*sorted({i if isinstance(i, int) else int(i) for i in items}))

# 116. Используя генератор множеств, дополните приведенный код так, чтобы получить множество, содержащее первую букву каждого слова (в нижнем регистре) списка words. 
#      Результат вывести на одной строке в алфавитном порядке, разделяя элементы одним символом пробела.

words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
print(*sorted({i[0].lower() for i in words}))

# 117. Используя генератор множеств, дополните приведенный код так, чтобы получить множество, содержащее уникальные слова (в нижнем регистре) строки sentence. 
#      Результат вывести на одной строке в алфавитном порядке, разделяя элементы одним символом пробела.
# 
#      Примечание. Учтите, что знаки пунктуации не относятся к словам.

sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
print(*sorted({i.strip(':,.!?();').lower() for i in sentence.split()}))

# 118. Используя генератор множеств, дополните приведенный код так, чтобы получить множество, содержащее уникальные слова  строки sentence длиною меньше 4 символов. 
#      Результат вывести на одной строке (в нижнем регистре) в алфавитном порядке, разделяя элементы одним символом пробела.
# 
#      Примечание. Учтите, что знаки пунктуации не относятся к словам.

sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
print(*sorted({i.strip(':,.!?();').lower() for i in sentence.split() if len(i.strip(':,.!?();')) < 4}))

# 119. Используя генератор множеств, дополните приведенный код так, чтобы он выбрал из списка files уникальные имена файлов c расширением .png, 
#      независимо от регистра имен и расширений. Имена файлов вывести вместе с расширением, все на одной строке, в нижнем регистре, в алфавитном порядке через пробел.
# 
#      Примечание. Если бы список files содержал следующие имена файлов:
#      files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git', 'ZeBrA.PnG']
#      то ответом был бы:
#      apple.png python.png zebra.png

files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
print(*sorted({i.lower() for i in files if '.png' in i.lower()}))

# 120. Наполните множество set1 содержимым так, чтобы программа вывела {'p'}.

set1 = {'p'}
set2 = {'a', 't', 'f'}

print(set1 - set2)

# 121. Учитель проверяет домашнее задание в классе и получил следующие ответы: из n школьников у m домашнее задание съела собака, у k отключили свет, 
#      а p учеников постигли оба несчастья. Напишите программу, которая определяет сколько человек выполнило домашнее задание.
# 
#      Формат входных данных
#      На вход программе подаются числа n,m,k,p, каждое на отдельной строке.
# 
#      Формат выходных данных
#      Программа должна вывести количество учеников, сделавших домашнее задание.

n, m, k, p = [int(input()) for _ in range(4)]
print(n - m - k + p)

# 122. На спутнике «Восход» установлен прибор для измерения солнечной активности. Каждую минуту он передаёт в обсерваторию по каналу связи положительное целое число
#      — количество энергии солнечного излучения. Для правильного анализа результатов нет необходимости держать повторяющиеся данные, поэтому их нужно удалить. 
#     Напишите программу, которая выводит максимальное количество показаний спутника, при удалении которых результат будет правильно проанализирован.
# 
#     Формат входных данных
#     На вход программе подаётся одна строка, содержащая числа – показания спутника «Восход». Числа указываются через пробел и не содержат ведущих нулей.
# 
#     Формат выходных данных
#     Программа должна вывести максимальное количество показаний, после удаления которых анализ результатов будет произведен верно.
# 
#     Примечание. Рассмотрим 1 тест: у нас подаются данные 10 20 30 10 40 10. Мы видим, что число 10 содержится тут 3 раза – значит, повторяющиеся числа 10 надо удалить. 
#     Таких у нас 2 (первое число 10 мы не учитываем). Другие числа не повторяются, поэтому ответ будет 2.

numbers = list(map(int, input().split()))
print(len(numbers) - len(set(numbers)))

# 123. Тимур и Руслан играют в игру города. Они очень любят эту игру и знают много городов, особенно Тимур, 
#      однако к концу игры ввиду своего возраста забывают, какие города уже называли.
#      Напишите программу, считывающую информацию об игре и сообщающую ребятам, что очередной город назван повторно.
# 
#      Формат входных данных
#      На вход программе в первой строке подаётся натуральное число n – количество названных городов, 
#      в последующих n строках вводятся названные города и ещё одна строка с новым, только что названым городом.
# 
#      Формат выходных данных
#      Программа должна вывести OK, если этот город ещё не вспоминали, и REPEAT, если город уже был назван.

n = int(input())
cities = set([input() for _ in range(n + 1)])
print('OK') if n + 1 == len(cities) else print('REPEAT')

# 124. Руслан получил в конце учебного года список литературы на лето. Теперь ему надо выяснить, какие книги из этого списка у него есть. 
#      У Руслана на компьютере в текстовом файле записаны все книги из его домашней библиотеки в случайном порядке.
#      Напишите программу, определяющую для каждой книги из списка на прочтение, есть она у Руслана или нет.
# 
#      Формат входных данных
#      На вход программе в первой строке подается натуральное число m — количество книг в домашней библиотеке Руслана. 
#      Во второй строке записано натуральное число n —  количество книг в списке на лето. 
#      Далее идут m строк с названиями книг из домашней библиотеки и n строк названий из списка на лето.
# 
#      Формат выходных данных
#      Программа должна вывести n строк, в каждой из которых написано слово YES, если книга найдена в библиотеке, и NO, если нет.

m, n = int(input()), int(input())
lst = set([input() for _ in range(m)])

for _ in range(n):
    print(['NO', 'YES'][input() in lst])

# 125. Как известно, математики странные люди🤪. Не составляет исключения и Тимур — автор данного курса. Каждый день Тимур решает ровно две сложные математические задачи. 
#      Решая первую задачу, он записывает на первом листочке все числа, которые в ней встречаются. Далее он делает паузу и берется за вторую задачу. 
#      Затем записывает на втором листочке все числа, которые в ней встречаются. После этого он берет еще один листок и выписывает на него все совпадающие числа 
#      из первых двух листочков. Если такие числа есть — день удался, если общих чисел нет — Тимур считает день неудачным.
#      Напишите программу, которая находит общие числа двух листочков или сообщает, что день не удался 😏.
# 
#      Формат входных данных
#      На вход программе подаются две строки с числами: в первой строке числа с первого листочка, во второй — со второго.
# 
#      Формат выходных данных
#      Программа должна вывести числа, встретившиеся на обоих листках в отсортированном по убыванию порядке, либо словосочетание BAD DAY, если таких чисел нет.

s1, s2 = {int(i) for i in input().split()}, {int(i) for i in input().split()}
s3 = s1 & s2
print('BAD DAY') if not s3 else print(*sorted(s3, reverse=True))

# 126. При приёме новых сотрудников в онлайн-школу BEEGEEK её руководитель тестирует не только профессиональные качества кандидата, но и его память.
#      Кандидату показывают ненадолго несколько различных чисел, а затем кандидат должен их назвать. 
#      Причем неважно, в каком порядке он их вспоминает, и повторяется он или нет, главное он должен назвать все числа, не добавляя лишних.
#      Напишите программу, определяющую, успешно ли прошел кандидат тестирование памяти.
# 
#      Формат входных данных
#      На вход программе подаются две строки с числами: в первой строке показанные кандидату, а во второй ответы кандидата.
# 
#      Формат выходных данных
#      Программа должна вывести YES, если кандидат прошел испытание и его можно брать на работу и NO в противном случае.

s1, s2 = {int(i) for i in input().split()}, {int(i) for i in input().split()}
print('YES' if s1 == s2 else 'NO')

# 127. Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба эти предмета. 
#      У руководителя школы есть списки изучающих каждый предмет.
#      Напишите программу, позволяющую руководителю выяснить, сколько учеников изучает только математику.
# 
#      Формат входных данных
#      На вход программе в первых двух строках подаются числа m и n – количества учеников, изучающих математику и информатику соответственно. 
#      Далее идут m строк — фамилии учеников, которые изучают математику и n строк с фамилиями учеников, изучающих информатику.
# 
#      Формат выходных данных
#      Программа должна вывести количество учеников, которые изучают только математику.
# 
#      Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.

m, n = int(input()), int(input())
s1, s2 = set([input() for _ in range(m)]), set([input() for _ in range(n)])
print(len(s1 - s2))

# 128. Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба этих предмета. 
#      У руководителя школы есть списки изучающих каждый предмет.
#      Напишите программу, позволяющую руководителю выяснить, сколько учеников изучает только один предмет.
# 
#      Формат входных данных
#      На вход программе в первых двух строках подаются числа m и n – количества учеников, изучающих математику и информатику соответственно. 
#      Далее идут m строк — фамилии учеников, которые изучают математику и n строк с фамилиями учеников, изучающих информатику.
# 
#      Формат выходных данных
#      Программа должна вывести количество учеников, которые изучают только один предмет. Если таких учеников не окажется, то необходимо вывести NO.
# 
#      Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.

m, n = int(input()), int(input())
s1, s2 = set([input() for _ in range(m)]), set([input() for _ in range(n)])
s3 = s1.symmetric_difference(s2)
print(len(s3) if s3 else 'NO')

# 129. Руководитель онлайн-школы BEEGEEK и его помощник составили списки учеников их школы.
#      Напишите программу, которая выведет все фамилии учеников, которые вспомнили руководитель и его помощник.
# 
#      Формат входных данных
#      На вход программе в первой строке подаются фамилии, записанные руководителем школы, а на второй строке - помощником руководителя. Фамилии указываются через пробел.
# 
#      Формат выходных данных
#      Программа должна вывести все фамилии учеников, отсортированных в лексикографическом порядке, записанные руководителем и его помощником.
# 
#      Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.

s1, s2 = {i for i in input().split()}, {i for i in input().split()}
print(*sorted(s1.union(s2)))

# 130. Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба этих предмета. 
#      У руководителя школы есть списки учеников, изучающих каждый предмет. Случайно списки всех учеников перемешались.
#      Напишите программу, которая позволит руководителю выяснить, сколько учеников изучает только один предмет.
# 
#      Формат входных данных
#      На вход программе в первых двух строках подаются числа m и n – количества учеников, изучающих математику и информатику соответственно. 
#      Далее идут m+n строк — фамилии учеников, изучающих математику и информатику, в произвольном порядке.
# 
#      Формат выходных данных
#      Программа должна вывести количество учеников, которые изучают только один предмет. Если таких учеников не окажется, то необходимо вывести NO.
# 
#      Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.

m, n = int(input()), int(input())
st = set()

for _ in range(m + n):
    if (x := input()) not in st:
        st.add(x)
    else:
        st.discard(x)
        
print(len(st) if st else 'NO')

# 131. Руководителю онлайн-школы BEEGEEK захотелось узнать, кто из его учеников присутствовал на всех уроках с начала учебного года. 
#      Для каждого урока есть листок со списком присутствовавших учеников.
#      Напишите программу, определяющую фамилии учеников, которые присутствовали на всех уроках.
# 
#      Формат входных данных
#      На вход программе в первой строке дается число m – количество уроков, проведенных с начала учебного года. Далее идёт m блоков строк, описывающих листки с фамилиями. 
#      На первой строке каждого блока указано количество фамилий ni, затем идёт ni строчек с фамилиями тех, кто был на i-ом уроке.
# 
#      Формат выходных данных
#      Программа должна вывести фамилии учеников, которые были на всех уроках, отсортированных в лексикографическом порядке. 
#      Каждая фамилия должна быть записана на отдельной строке.
# 
#      Примечание 1. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.
#      Примечание 2. Гарантируется, что хотя бы один ученик был на всех уроках.

m = int(input())
students = {input() for _ in range(int(input()))}

for _ in range(m - 1):
    tmp = {input() for _ in range(int(input()))}
    students.intersection_update(tmp)
    
print(*sorted(students), sep='\n')