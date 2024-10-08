# 1. Напишите программу, которая выводит на экран текст «Здравствуй, мир!» (без кавычек).

print ("Здравствуй, мир!")

# 2. В популярном сериале «Остаться в живых» использовалась последовательность чисел 4 8 15 16 23 42,
#    которая принесла героям удачу и помогла сорвать джекпот в лотерее. Напишите программу, которая выводит
#    данную последовательность чисел с одним пробелом между ними.

print ("4", "8", "15", "16", "23", "42")

# 3. Измените предыдущую программу так, чтобы каждое число последовательности 4 8 15 16 23 42 печаталось
#    на отдельной строке.

print ("4")
print ("8")
print ("15")
print ("16")
print ("23")
print ("42")

# 4. Напишите программу, которая выводит указанный треугольник, состоящий из звездочек (*).

print ("*")
print ("**")
print ("***")
print ("****")
print ("*****")
print ("******")
print ("*******")

# 5. На вход программе подается строка текста – имя человека. Напишите программу, которая выводит на экран
#    приветствие в виде слова «Привет» (без кавычек), после которого должна стоять запятая и пробел, а затем
#    введенное имя.

name=input()
print("Привет,", name)

# 6. На вход программе подается строка текста – название футбольной команды. Напишите программу,
#    которая повторяет ее на экране со словами « - чемпион!» (без кавычек).

team=input()
print(team, "- чемпион!")

# 7. Напишите программу, которая считывает три строки по очереди, а затем выводит их в той же
#    последовательности, каждую на отдельной строчке.

a=input()
print(a)
b=input()
print(b)
c=input()
print(c)

# 8. Напишите программу, которая считывает три строки по очереди, а затем выводит их
#    в обратной последовательности, каждую на отдельной строчке.

a=input()
b=input()
c=input()
print(c)
print(b)
print(a)

# 9. Напишите программу, которая выводит на экран текст «I***like***Python» (без кавычек).

print("I", "like", "Python", sep="***")

# 10. Напишите программу, которая считывает строку-разделитель и три строки, а затем выводит указанные
#     строки через разделитель.

a=input()
b=input()
c=input()
d=input()
print(b, c, d, sep=a)

# 11. Напишите программу, которая приветствует пользователя, выводя слово «Привет» (без кавычек), после
#     которого должна стоять запятая и пробел, а затем введенное имя и восклицательный знак.

a=input()
print("Привет,", a, end="!")

# 12. Напишите программу вывода на экран трех последовательно идущих чисел, каждое на отдельной строке.
#     Первое число вводит пользователь, остальные числа вычисляются в программе.

num1 = int(input())
num2 = num1 + 1
num3 = num1 + 2
print(num1, num2, num3, sep = '\n')

# 13. Напишите программу, которая считывает три целых числа и выводит на экран их сумму. Каждое число
#     записано в отдельной строке.

num1 = int(input())
num2 = int(input())
num3 = int(input())
print(num1 + num2 + num3)

# 14. Напишите программу, вычисляющую объём куба и площадь его полной поверхности, по введённому
#     значению длины ребра.

a = int(input())
print('Объем =', a * a * a)
print('Площадь полной поверхности =', 6 * (a * a))

# 15. Напишите программу вычисления значения функции f(a, b) = 3(a + b)^3 + 275b^2 - 127a – 41 по введеным
#     целым значениям a и b.

a = int(input())
b = int(input())
print(3 * ((a + b) * (a + b) * (a + b)) + 275 * (b * b) - 127 * a - 41)

# 16. Напишите программу, которая считывает целое число, после чего на экран выводится следующее и
#     предыдущее целое число с пояснительным текстом.

a = int(input())
b = int(input())
print(3 * ((a + b) * (a + b) * (a + b)) + 275 * (b * b) - 127 * a - 41)

# 17. Напишите программу, которая считывает целое число, после чего на экран выводится следующее и
#     предыдущее целое число с пояснительным текстом.

num1 = int(input())
print('Следующее за числом', num1, 'число:', num1 + 1)
print('Для числа', num1, 'предыдущее число:', num1 - 1)

# 18. Напишите программу, которая считает стоимость трех компьютеров, состоящих из монитора, системного
#     блока, клавиатуры и мыши.

scr = int(input())
sys = int(input())
keyb = int(input())
mou = int(input())
print(scr + sys + keyb + mou) * 3

# 19. Напишите программу, в которой вычисляется сумма, разность и произведение двух целых чисел,
#     введенных с клавиатуры.

a = int(input())
b = int(input())
print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '*', b, '=', a * b)

# 20. Арифметической прогрессией называется последовательность чисел a1,a2,...,an, каждое из которых,
#     начиная с a2, получается из предыдущего прибавлением к нему одного и того же постоянного
#     числа d (разность прогрессии). Программа должна вывести n-ый член арифметической прогрессии.

a1 = int(input())
d = int(input())
n = int(input())
print(a1 + d * (n - 1))

# 21. Напишите программу, которая считывает целое положительное число x и выводит на экран
#     последовательность чисел x, 2x, 3x, 4x и 5x, разделённых тремя черточками.

x = int(input())
print(x, 2 * x, 3 * x, 4 * x, 5 * x, sep = '---')

# 22. Геометрической прогрессией называется последовательность чисел b1,b2,…,bn, каждое из которых,
#     начиная с b2, получается из предыдущего умножением на одно и то же
#     постоянное число q (знаменатель прогрессии). На вход программе подаётся три целых числа: b1, q и n,
#     каждое на отдельной строке. Программа должна вывести n-ый член геометрической прогрессии.

b1 = int(input())
q = int(input())
n = int(input())
print(b1 * q ** (n - 1))

# 23. Напишите программу, которая находит полное число метров по заданному числу сантиметров. На вход
#     программе подаётся натуральное число – количество сантиметров. Программа должна вывести одно число
#     – полное число метров.

x = int(input())
print(x // 100)

# 24. n школьников делят k мандаринов поровну, неделящийся остаток остается в корзине. Сколько целых
#     мандаринов достанется каждому школьнику? Сколько целых мандаринов останется в корзине? На вход
#     программе подаётся два целых числа: количество школьников и количество мандаринов, каждое на
#     отдельной строке. Программа должна вывести два числа: количество мандаринов, которое достанется
#     каждому школьнику, и количество мандаринов, которое останется в корзине, каждое на отдельной строке.

n = int(input())
k = int(input())
print(k // n)
print(k % n)

# 25. Безумный титан Танос собрал все 6 камней бесконечности и намеревается уничтожить половину населения
#     Вселенной по щелчку пальцев. При этом если население Вселенной является нечетным числом, то титан
#     проявит милосердие и округлит количество выживших в большую сторону. Помогите Мстителям
#     подсчитать количество выживших. На вход дается число целое n – население Вселенной. Программа
#     должна вывести одно число – количество выживших.

n = int(input())
print((n + 1) // 2)

# 26. В купейном вагоне имеется 99 купе с четырьмя местами для пассажиров в каждом. Напишите программу,
#     которая определяет номер купе, в котором находится место с заданным номером (нумерация мест сквозная,
#     начинается с 1). На вход программе подаётся целое число – место с заданным номером в вагоне. Программа
#     должна вывести одно число – номер купе, в котором находится указанное место.

n = int(input())
print((n + 3) // 4)

# 27. Напишите программу для пересчёта величины временного интервала, заданного в минутах, в величину,
#     выраженную в часах и минутах. На вход программе подаётся целое число – количество минут. Программа
#     должна вывести текст в соответствии с условием задачи.

t = int(input())
print(t, 'мин - это', t // 60 ,'час', t % 60, 'минут.')

# 28. Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного
#     числа. На вход программе подаётся положительное трёхзначное число. Программа должна вывести два
#     числа с поясняющим текстом: сумма цифр и произведение цифр.

x = int(input())
digit3 = x % 10
digit2 = (x % 100) // 10
digit1 = x // 100
print('Сумма цифр =', digit1 + digit2 + digit3)
print('Произведение цифр =', digit1 * digit2 * digit3)

# 29. Дано трехзначное число abc, в котором все цифры различны. Напишите программу, которая выводит шесть
#     чисел, образованных при перестановке цифр заданного числа. На вход программе подаётся положительное
#     трёхзначное целое число, все цифры которого различны. Программа должна вывести шесть чисел,
#     образованных при перестановке цифр заданного числа в следующем порядке: abc, acb, bac, bca, cab, cba.

x = int(input())
c = x % 10
b = (x % 100) // 10
a = x // 100
print(a * 100 + b * 10 + c)
print(a * 100 + c * 10 + b)
print(b * 100 + a * 10 + c)
print(b * 100 + c * 10 + a)
print(c * 100 + a * 10 + b)
print(c * 100 + b * 10 + a)

# 30. Напишите программу для нахождения цифр четырёхзначного числа. На вход программе подаётся
#     положительное четырёхзначное целое число. Программа должна вывести текст в соответствии с условием
#     задачи.

x = int(input())
a4 = x % 10
a3 = (x % 100) // 10
a2 = (x % 1000) // 100
a1 = x // 1000
print('Цифра в позиции тысяч равна', a1)
print('Цифра в позиции сотен равна', a2)
print('Цифра в позиции десятков равна', a3)
print('Цифра в позиции единиц равна', a4)

# 31. Напишите программу, которая выводит прямоугольник, по периметру состоящий из звездочек (*). Высота и
#     ширина прямоугольника равны 44 и 1717 звёздочкам соответственно.

print('*****************')
print('*                          *')
print('*                          *')
print('*****************')

# 32. Напишите программу, которая считывает два целых числа a и b и выводит на экран квадрат суммы (a+b)2 и
#     сумму квадратов a2+b2 этих чисел.

a = int(input())
b = int(input())
print('Квадрат суммы', a, 'и', b, 'равен', (a + b) ** 2)
print('Сумма квадратов', a, 'и', b, 'равна', a ** 2 + b ** 2)

# 33. Как известно, целые числа в языке Python не имеют ограничений, которые встречаются в других языках
#     программирования. Напишите программу, которая считывает четыре целых положительных числа a, b,
#     c и d и выводит на экран значение выражения ab+cd.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(a ** b + c ** d)

# 34. Напишите программу, которая считывает целое положительное число n, n∈[1;9] и выводит значение
#     числа n+nn+nnn.

n = int(input())
print(n + (n * 10 + n) + (n * 10 + n * 100 + n))