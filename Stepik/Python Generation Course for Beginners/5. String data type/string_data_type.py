# 160. Дополните приведенный код, используя индексатор, так чтобы он вывел символ запятой.

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[7])

# 161. Дополните приведенный код, используя индексатор, так чтобы он вывел символ w.

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-10])

# 162. На вход программе подается одна строка. Напишите программу, которая выводит элементы строки с
#      индексами 0, 2, 4, ... в столбик.
#      На вход программе подается одна строка.
#      Программа должна вывести элементы строки с индексами 0, 2, 4, ..., каждое на отдельной строке.

s = input()
for i in range(0, len(s), 2):
    print(s[i])

# 163. На вход программе подается одна строка. Напишите программу, которая выводит в столбик элементы
#      строки в обратном порядке.
#      На вход программе подается одна строка.
#      Программа должна вывести в столбик элементы строки в обратном порядке. 

s = input()
for i in range(1, len(s) + 1):
    print(s[-i])

# 164. На вход программе подаются три строки: имя, фамилия и отчество. Напишите программу, которая выводит
#      инициалы человека.
#      На вход программе подаются три строки, каждая на отдельной строке.
#      Программа должна вывести ФИО человека.
#      Гарантируется, что имя, фамилия и отчество начинаются с заглавной буквы.

s1, s2, s3 = input(), input(), input()
print(s2[0], s1[0], s3[0], sep='')

# 165. На вход программе подается одна строка состоящая из цифр. Напишите программу, которая считает сумму
#      цифр данной строки.
#      На вход программе подается одна строка состоящая из цифр.
#      Программа должна вывести сумму цифр данной строки.

s = input()
total = 0
for i in s:
    total += int(i)
print(total)

# 166. На вход программе подается одна строка. Напишите программу, которая выводит сообщение «Цифра» (без
#      кавычек), если строка содержит цифру. В противном случае вывести сообщение «Цифр нет» (без кавычек).

s = input()
flag = False
for i in range(len(s)):
    if s[i] in '0123456789':
        flag = True
if flag == True:
    print('Цифра')
else:
    print('Цифр нет')

# 167. На вход программе подается одна строка. Напишите программу, которая определяет сколько раз в строке
#      встречаются символы + и *.
#      На вход программе подается одна строка.
#      Программа должна вывести сколько раз встречаются символы  + и * в строке.

s = input()
count1 = 0
count2 = 0
for i in range(len(s)):
    if s[i] in '+':
        count1 += 1
    if s[i] in '*':
        count2 += 1
print('Символ + встречается', count1, 'раз')
print('Символ * встречается', count2, 'раз')

# 168. На вход программе подается одна строка. Напишите программу, которая определяет сколько в
#      ней одинаковых соседних символов.
#      На вход программе подается одна строка.
#      Программа должна вывести количество одинаковых соседних символов.

s = input()
count = 0
for i in range(len(s)-1):
    if s[i] == s[i + 1]:
        count += 1
print(count)

# 169. На вход программе подается одна строка с буквами русского языка. Напишите программу, которая
#      определяет количество гласных и согласных букв.
#      На вход программе подается одна строка.
#      Программа должна вывести количество гласных и согласных букв.

s = input()
vowel = 0
consonant = 0
for i in range(len(s)):
    if s[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        vowel += 1
    if s[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        consonant += 1
print('Количество гласных букв равно', vowel)
print('Количество согласных букв равно', consonant)

# 170. На вход программе подается натуральное число, записанное в десятичной системе счисления. Напишите
#      программу, которая переводит данное число в двоичную систему счисления.
#      На вход программе подается одно натуральное число.
#      Программа должна вывести число записанное в двоичной системе счисления.

n = int(input())
text = ''
while n != 0:
    text = str(n % 2) + text
    n //= 2
print(text)

# 171. Дополните приведенный код, используя срезы, так чтобы он вывел первые 12 символов строки s.

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[:12])

# 172. Дополните приведенный код, используя срезы, так чтобы он вывел последние 9 символов строки s.

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-9:])

# 173. Дополните приведенный код, используя срезы, так чтобы он вывел каждый 7 символ строки s начиная от
#      начала строки.

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::7])

# 174. Дополните приведенный код, используя срезы, так чтобы он вывел строку s в обратном порядке.

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::-1])

# 175. На вход программе подается одно слово, записанное в нижнем регистре. Напишите программу, которая
#      определяет является ли оно палиндромом.
#      На вход программе подается одно слово в нижнем регистре.
#      Программа должна вывести «YES», если слово является палиндромом и «NO» в противном случае.

s = input()
flag = False
for i in range(len(s)):
    if s[::1] == s[::-1]:
        flag = True
if flag == True:
    print('YES')
else:
    print('NO')

# 176. На вход программе подается одна строка. Напишите программу, которая выводит:
#      1.	общее количество символов в строке;
#      2.	исходную строку повторенную 3 раза;
#      3.	первый символ строки;
#      4.	первые три символа строки;
#      5.	последние три символа строки;
#      6.	строку в обратном порядке;
#      7.	строку с удаленным первым и последним символом.
#      На вход программе подается одна строка, длина которой больше 3 символов.
#      Программа должна вывести данные в соответствии с условием. Каждое значение выводится на отдельной
#      строке.

s = input()
total = len(s)
three_times = s * 3
first_symbol = s[0]
first_three_sym = s[:3]
last_three_sym = s[-3:]
reverse = s[::-1]
del_first_last = s[1:-1]
print(total)
print(three_times)
print(first_symbol)
print(first_three_sym)
print(last_three_sym)
print(reverse)
print(del_first_last)

# 177. На вход программе подается одна строка. Напишите программу, которая выводит:
#      1.	третий символ этой строки;
#      2.	предпоследний символ этой строки;
#      3.	первые пять символов этой строки;
#      4.	всю строку, кроме последних двух символов;
#      5.	все символы с четными индексами;
#      6.	все символы с нечетными индексами;
#      7.	все символы в обратном порядке;
#      8.	все символы строки через один в обратном порядке, начиная с последнего.
#      На вход программе подается одна строка, длина которой больше 5 символов.
#      Программа должна вывести данные в соответствии с условием. Каждое значение выводится на
#      отдельной строке.

s = input()
third_sym = s[2]
pre_last = s[-2]
first_five = s[:5]
without_two_last = s[:-2]
all_even = s[::2]
all_not_even = s[1::2]
reverse = s[::-1]
all_sym = s[::-2]
print(third_sym)
print(pre_last)
print(first_five)
print(without_two_last)
print(all_even)
print(all_not_even)
print(reverse)
print(all_sym)

# 178. На вход программе подается строка текста. Напишите программу, которая разрежет ее на две равные части,
#      переставит их местами и выведет на экран.
#      На вход программе подается строка текста.
#      Программа должна вывести текст в соответствии с условием задачи.
#      Если длина строки нечетная, то длина первой части должна быть на один символ больше.

s = input()
length = len(s)
s1 = ''
s2 = ''
flag = False
if length % 2 == 0:
    flag = True
    for i in range(length//2):
        s1 += s[i]
    for j in range(length//2, length):
        s2 += s[j]
elif length % 2 != 0:
    for k in range(length//2 + 1):
        s1 += s[k]
    for g in range(length//2 + 1, length):
        s2 += s[g]
if flag == True:
    print(s2 + s1)
else:
    print(s2 + s1)

# 179. На вход программе подается строка состоящая из имени и фамилии человека, разделенных одним
#      пробелом. Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.
#      На вход программе подается строка. 
#      Программа должна вывести «YES» если имя и фамилия начинаются с заглавной буквы и «NO» в противном
#      случае.
#      Строка содержит только буквы.

s = input()
if s == s.title():
    print('YES')
else:
    print('NO')

# 180. На вход программе подается строка. Напишите программу, которая меняет регистр символов, другими
#      словами замените все строчные символы заглавными и наоборот.

s = input()
print(s.swapcase())

# 181. На вход программе подается строка текста. Напишите программу, которая определяет является ли оттенок
#      текста хорошим или нет. Текст имеет хороший оттенок, если содержит подстроку «хорош» во
#      всевозможных регистрах.
#      На вход программе подается строка текста.
#      Программа должна вывести «YES» если текст имеет хороший оттенок и «NO» в противном случае.
#      Текст содержащий хорош, ХОРОШ, Хорош, хОРОШ и т.д. имеет хороший оттенок.

s = input()
s = s.lower()
if 'хорош' in s:
    print('YES')
else:
    print('NO')

# 182. На вход программе подается строка. Напишите программу, которая подсчитывает количество буквенных
#      символов в нижнем регистре.
#      На вход программе подается строка.
#      Программа должна вывести количество буквенных символов в нижнем регистре.

s = input()
count = 0
for i in range(len(s)):
    if 'a' <= s[i] <= 'z':
        count += 1
print(count)

# 183. На вход программе подается строка текста, состоящая из слов, разделенных ровно одним пробелом.
#      Напишите программу, которая подсчитывает количество слов в ней.
#      На вход программе подается строка текста.
#      Программа должна вывести количество слов.
#      Строка текста не содержит пробелов в начале и конце.
#      Используйте для решения задачи метод count.

s = input()
print(s.count(' ') + 1)

# 184. На вход программе подается строка генетического кода, состоящая из букв А (аденин), Г (гуанин),
#      Ц (цитозин), Т (тимин). Напишите программу, которая подсчитывает сколько аденина, гуанина, цитозина и
#      тимина входит в данную строку генетического кода.
#      На вход программе подается строка генетического кода, состоящая из символов А, Г, Ц, Т, а, г, ц, т.
#      Программа должна вывести сколько гуанина, тимина, цитозина, аденина входит в данную строку
#      генетического кода.
#      Строка не содержит символов, кроме как А, Г, Ц, Т, а, г, ц, т.

s = input()
s = s.lower()
print('Аденин:', s.count('а'))
print('Гуанин:', s.count('г'))
print('Цитозин:', s.count('ц'))
print('Тимин:', s.count('т'))

# 185. Джим Хоппер с помощью радиоприемника пытается получить сообщение Оди. На приемник ему
#      поступает n различных последовательностей кода Морзе. Декодировав их, он получает
#      последовательности из цифр и строчного латинского алфавита, при этом во всех сообщениях Оди
#      содержится число 11, причем минимум 3 раза. Помогите определить Джиму количество сообщений от Оди.
#      В первой строке подаётся число n – количество сообщений, в последующих n строках вводятся строки,
#      содержащие латинские строчные буквы и цифры.
#      Программа должна вывести количество строк в которых содержится число 11 минимум 3 раза.
#      Числа 11 необязательно должны быть разделены другими символами, нужно подсчитать вхождение
#      последовательности символов "11", т.е. например в строке "111" содержится одна такая
#      последовательность, в то время как в "1111" их уже две.

n = int(input())
count = 0
for i in range(n):
    s = input()
    if s.count('11') >= 3:
        count += 1
print(count)

# 186. На вход программе подается строка текста. Напишите программу, которая подсчитывает количество цифр
#      в данной строке.
#      На вход программе подается строка текста.
#      Программа должна вывести количество цифр в данной строке.

s = input()
count = 0
for i in range(len(s)):
    if '0' <= s[i] <= '9':
        count += 1
print(count)

# 187. На вход программе подается строка текста. Напишите программу, которая проверяет, что строка
#      заканчивается подстрокой .com или .ru.
#      На вход программе подается строка текста.
#      Программа должна вывести «YES» если введенная строка заканчивается подстрокой .com или .ru и
#      «NO» в противном случае.

s = input()
if s.endswith('.com') or s.endswith('.ru'):
    print('YES')
else:
    print('NO')

# 188. На вход программе подается строка текста. Напишите программу, которая выводит на экран символ,
#      который появляется наиболее часто.
#      На вход программе подается строка текста. Текст может содержать строчные и заглавные буквы
#      английского и русского алфавита, а также цифры.
#      Программа должна вывести символ, который появляется наиболее часто.
#      Если таких символов несколько, следует вывести последний по порядку символ.
#      Следует различать заглавные и строчные буквы, а также буквы русского и английского алфавита.

s = input()
count1 = 0
count2 = 0
for i in s:
    if s.count(i) >= count1:
        count1 = s.count(i)
        count2 = i
print(count2)

# 189. На вход программе подается строка текста. Если в этой строке буква «f» встречается только один раз,
#      выведите её индекс. Если она встречается два и более раз, выведите индекс её первого и последнего
#      вхождения на одной строке, разделенных символом пробела. Если буква «f» в данной строке не
#      встречается, следует вывести «NO».


s = input()
index1 = 0
index2 = 0
for i in s:
    if s.count('f') == 1:
        index1 = s.find('f')
        print(index1)
        break
    if s.count('f') > 1:
        index1 = s.find('f')
        index2 = s.rfind('f')
        print(index1, index2)
        break
    if s.count('f') == 0:
        print('NO')
        break

# 190. На вход программе подается строка текста, в которой буква «h» встречается минимум два раза. Напишите
#      программу, которая удаляет из этой строки первое и последнее вхождение буквы «h», а также все
#      символы, находящиеся между ними.

s = input()
s1 = s.find('h')
s2 = s.rfind('h') + 1
print(s[:s1] + s[s2:])

# 191. Дополните приведенный код, используя форматирование строк с помощью метода format, так чтобы он
#        вывел текст: 
#                     «In 2010, someone paid 10k Bitcoin for two pizzas.» (без кавычек).

year = '2010'
price = '10k'
coin = 'Bitcoin'
s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(year, price, coin)
print(s)

# 192. Дополните приведенный код, используя форматирование строк с помощью f-строк, так чтобы он вывел
#        текст: 
#                     «In 2010, someone paid 10K Bitcoin for two pizzas.» (без кавычек).

year = 2010
amount = '10K'
currency = 'Bitcoin'
print(f'In {year}, someone paid {amount} {currency} for two pizzas.')

# 193. На вход программе подаются два числа a и b. Напишите программу, которая для каждого кодового
#      значения в диапазоне от a до b (включительно), выводит соответствующий ему символ из таблицы
#      символов Unicode.

a = int(input())
b = int(input())
result = ''
for i in range(a, b + 1):
    result += chr(i) + ' '
print(result)

# 194. На вход программе подается строка текста. Напишите программу, которая переводит каждый ее символ
#      в соответствующий ему код из таблицы символов Unicode.
#      На вход программе подается строка текста.
#      Программа должна вывести кодовые значения символов строки разделенных одним символом пробела.

s = input()
for i in s:
    print(ord(i), end=' ')

# 195. Легион Цезаря, созданный в 23 веке на основе Римской Империи не изменяет древним традициям
#      и использует шифр Цезаря. Это их и подвело, ведь данный шифр очень простой. Однако в
#      постапокалипсисе люди плохо знают все тонкости довоенного мира, поэтому ученые из НКР не могут
#      понять как именно нужно декодировать данные сообщения. Напишите программу для декодирования этого
#      шифра.
#      В первой строке дается число n (1 ≤ n ≤ 25) – сдвиг, во второй строке даётся закодированное сообщение в
#      виде строки со строчными латинскими буквами.
#      Программа должна вывести одну строку – декодированное сообщение. Обратите внимание, что нужно
#      декодировать сообщение, а не закодировать.

n = int(input())
s = input()
for i in range(len(s)):
    x = ord(s[i]) - n
    if x < 97:
        x = 122 - (96 - x)
    print(chr(x), end='')

# 196. Вставьте пропущенный фрагмент кода, так чтобы в результате выполнения программы была выведена
#      длина строки s.

s = 'Python rocks!'
print(len(s))

# 197. Вставьте пропущенный фрагмент кода, так чтобы в результате выполнения программы был выведен
#      четвертый символ строки s.

s = 'Python rocks!'
print(s[3])

# 198. Вставьте пропущенный фрагмент кода, так чтобы в результате выполнения программы
#      были выведены символы строки s со 2 по 5 включительно.

s = 'Python rocks!'
print(s[1:5])

# 199. Вставьте пропущенный фрагмент кода, так чтобы в результате выполнения программы была выведена
#      строка s без ведущих и замыкающих пробельных символов.

s = '    Python rocks!     '
print(s.strip())

# 200. Вставьте пропущенный фрагмент кода, так чтобы в результате выполнения программы была выведена
#      строка s заглавными буквами (в верхнем регистре).

s = 'Python rocks!'
print(s.upper())

# 201. Вставьте пропущенный фрагмент кода, так чтобы в результате выполнения программы была выведена
#      строка s в которой символ «o» заменен на символ «@».

s = 'Python rocks!'
print(s.replace('o', '@'))

# 202. На вход программе подается строка текста. Напишите программу, которая удаляет из нее все символы с
#      индексами кратными 3, то есть символы с индексами 0, 3, 6, ....

s = input()
for i in range(len(s)):
    if i % 3 == 0:
        continue
    print(s[i], end='')

# 203. На вход программе подается строка текста. Напишите программу, которая заменяет все вхождения цифры
#      1 на слово «one».

s = input()
for i in s:
    if i == '1':
        s = s.replace('1', 'one')
print(s)

# 204. На вход программе подается строка текста. Напишите программу, которая удаляет все вхождения
#      символа «@».

s = input()
for i in s:
    if i == '@':
        s = s.replace('@', '')
print(s)

# 205. На вход программе подается строка текста. Напишите программу, которая выводит индекс второго
#      вхождения буквы «f». Если буква «f» встречается только один раз, выведите число -1, а если не
#      встречается ни разу, выведите число -2.

s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') == 0:
    print(-2)
else:
    s = s.replace('f', ' ', 1)
    s = s.find('f')
    print(s)

# 206. На вход программе подается строка текста в которой буква «h» встречается как минимум два
#      раза. Напишите программу, которая возвращает исходную строку и переворачивает последовательность
#      символов, заключенную между первым и последним вхождением буквы «h».

s = input()
first_entry = s.find('h')
second_entry = s.rfind('h')
print(s[:first_entry], s[second_entry:first_entry:-1], s[second_entry:], sep='')