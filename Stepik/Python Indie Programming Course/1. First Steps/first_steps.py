# 1. Давайте попробуем написать нашу первую программу
#    Давайте выведем на экран при помощи команды print сообщение "Hello, Artem"
#    P.s. Не забывайте про апострофы

print("Hello, Artem")

# 2. Напишите программу, которая принимает на вход возраст человека (количество полных лет) и выводит сколько лет ему исполнится в следующем году

print(int(input()) + 1)

# 3. Вашей программе поступает на вход натуральное число. Ваша задача вывести в отдельных строках:
#    число, увеличенное в 2 раза;
#    число, уменьшенное в 2 раза

print((number := int(input())) * 2, number / 2, sep='\n')

# 4. Я думаю каждый знаком с квадратом - идеально симметричная и ровная фигура. Давайте напишем программу, которая вычисляет площадь квадрата по введенной длине.
#    На вход программе поступает вещественное число a
#    Программа выводит площадь квадрата

print(a := float(input()) ** 2)

# 5. Напишите программу, которая принимает на вход два целых числа в отдельных строках и выводит на экран их сумму.

a, b = int(input()), int(input())
print(a + b)

# 6. В этом задании необходимо написать программу, которая вычисляет площадь и периметр прямоугольника по введенной длине и ширине.
#    На вход программе в отдельных строках поступают два вещественных числа a и b: длина и ширина прямоугольника.
#    Программа должна вывести через пробел два значения: сперва площадь S, а затем периметр P прямоугольника

a, b = float(input()), float(input())
print(a * b, 2 * (a + b))

# 7. Дано значение температуры в градусах Фаренгейта. Определить значение этой же температуры в градусах Цельсия.
#    На вход программе поступает вещественное число F  - температура в градусах по Фаренгейту
#    Программа выводит градусы Цельсия

print((F := float(input()) - 32) * 5 / 9)

# 8. Найдите результат выражения ∣a∣+∣b∣
#    Значения переменных а и b поступают на вход в отдельных строках и могут быть только целого типа

a, b = abs(int(input())), abs(int(input()))
print(a + b)

# 9. Напишите программу, которая вычисляет длину отрезка (т.е. расстояние между двумя точками), заданного двумя значениями x1 и x2 (вещественные числа).

print(abs(float(input()) - float(input())))

# 10. Вводится вещественное число и нам нужно его округлить до 2 и 3 разряда после запятой и вывести полученный результат через пробел в одной строчке

print(round(x := float(input()), 2), round(x, 3))

# 11. Даны значения двух моментов времени, принадлежащих одним и тем же суткам: часы, минуты и секунды для каждого из моментов времени. 
#     Известно, что второй момент времени наступил не раньше первого. Определите, сколько секунд прошло между двумя моментами времени.
#     Программа на вход получает три целых числа: часы, минуты, секунды, задающие первый момент времени и три целых числа, задающих второй момент времени.
#     Выведите число секунд между этими моментами времени.

h1, m1, s1 = int(input()), int(input()), int(input())
h2, m2, s2 = int(input()), int(input()), int(input())
print((h2 * 3600 + m2 * 60 + s2) - (h1 * 3600 + m1 * 60 + s1))

# 12. Петя учится в школе и очень любит математику. Уже несколько занятий они с классом проходят арифметические выражения. 
#     На последнем уроке учительница написала на доске три положительных целых числа a, b, c. Задание заключалось в том, чтобы расставить между этими числами знаки операций '+' и '*', а также, 
#     возможно, скобки. Значение получившегося выражения должно быть как можно больше. 
#     Рассмотрим пример: пусть учительница выписала на доску числа 1, 2 и 3. Вот некоторые варианты расстановки знаков и скобок:
#     1+2*3=7
#     1*(2+3)=5
#     1*2*3=6
#     (1+2)*3=9
#     Обратите внимание на то, что знаки операций можно вставлять только между a и b, а также между b и c, то есть нельзя менять числа местами. 
#     Так, в приведенном примере нельзя получить выражение (1+3)*2.
#     Легко убедиться, что максимальное значение, которое можно получить, — это 9.
#     Ваша задача — по заданным a, b и c вывести, какое максимальное значение выражения можно получить.
#     Во входных данных записаны три целых числа a, b и c, каждое в отдельной строке (1 ≤ a, b, c ≤ 10).
#     Выведите максимальное значение выражения, которое можно получить.

a, b, c = int(input()), int(input()), int(input())
print(max(a + b * c, a * (b + c), a * b * c, (a + b) + c, (a + b) * c, a * b + c))

# 13. Напишите программу, которая вычисляет среднее арифметическое четырех введенных целых чисел.
#     Обратите внимание, что числа вводятся в одну строку через пробел

print(sum(map(int, input().split())) / 4)

# 14. Напишите программу, которая находит наилучшую оценку ученика за решение пяти контрольных работ. 
#     Оценки всех пяти работ вводятся в одну строку, могут быть только целые числа от 1 до 100

print(max(map(int, input().split())))

# 15. Известно, что на обработку одного квадратного метра панели требуется 1г сульфида. 
#     Всего необходимо обработать N прямоугольных панелей размером A на B метров. Вам необходимо подсчитать, сколько всего сульфида необходимо на обработку всех панелей. 
#     И не забудьте, что панели требуют обработки с обеих сторон.
#     На вход программе подаются 3 положительных целых числа N,A,B в одну строку

n, a, b = map(int, input().split())
print(n * a * b * 2)

# 16. Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
#     Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#     Поступает одно натуральное число S – общее количество сделанных журавликов.
#     В единственную строку нужно вывести три числа, разделенных пробелами – количество журавликов, которые сделал каждый ребенок (Петя, Катя и Сережа).

s = int(input())
print(int(s / 6), int(s - s / 3), int(s / 6))

# 17. Однажды, посетив магазин канцелярских товаров, Вася купил X карандашей, Y ручек и Z фломастеров. Известно, что цена ручки на 2 рубля больше цены карандаша и на 7 рублей меньше цены фломастера. 
#     Также известно, что стоимость карандаша составляет 3 рубля. Требуется определить общую стоимость покупки.

x, y, z = map(int, input().split())
print(x * 3 + y * 5 + z * 12)

# 18. Бандиты Гарри и Ларри отдыхали на природе. Решив пострелять, они выставили на бревно несколько банок из-под кока-колы (не больше 10). 
#     Гарри начал простреливать банки по порядку, начиная с самой левой, Ларри — с самой правой. В какой-то момент получилось так, что они одновременно прострелили одну и ту же последнюю банку.
#     Гарри возмутился и сказал, что Ларри должен ему кучу денег за то, что тот лишил его удовольствия прострелить несколько банок. 
#     В ответ Ларри сказал, что Гарри должен ему еще больше денег по тем же причинам. Они стали спорить кто кому сколько должен, но никто из них не помнил сколько банок было в начале, 
#     а искать простреленные банки по всей округе было неохота. Каждый из них помнил только, сколько банок прострелил он сам.
#     Определите по этим данным, сколько банок не прострелил Гарри и сколько банок не прострелил Ларри.

[print(y - 1, x - 1) for x, y in [map(int, input().split())]]

# 19. Напишите программу, которая выводит на экран сообщение Привет, Мир!

print("Привет, Мир!")

# 20. Напишите программу, которая  принимает на вход три целых числа в одной строке через пробел и выводит их последовательно через запятую как в примерах ниже

[print(a, b, c, sep=',') for a, b, c in [map(int, input().split())]]

# 21. Программа, считывает натуральное число n, после чего выводит двойное неравенство этого числа с его соседними числами.

print((n := int(input())) - 1, n, n + 1, sep='<')

# 22. Вам необходимо вывести три фразы, разделяя их тремя дефисами. Сами фразы вводятся с клавиатуры на трех разных строчках

print(input(), input(), input(), sep='---')

# 23. В этой задаче мы сами будем решать, какое значение использовать в качестве разделителя в параметре sep
#     Программа принимает на вход строку - разделитель, вам необходимо распечатать числа от 1 до 5, выводя между ними введенный разделитель

print(*range(1, 6), sep=input())

# 24. Перед вами персонажи одного знаменитого сериала. Один из главных героев любит в конце своего предложения вставлять фразу «Сказала она!»
#     Давайте и мы напишем такую программу. Она принимает на вход предложение и и затем печатает его с фразой «Сказала она!» в конце определенным образом (см. примеры). 
#     Пользуйтесь аргументом end  и следите за символами, которые печатаются.

print(input(), end=' - Сказала она!')

# 25. Напишите программу, которая найдет сколько полных килограмм умещается в заданное число грамм.
#     На вход программе подаётся натуральное число – количество грамм.
#     Программа должна вывести одно число – полное число килограмм .

print(int(input()) // 1000)

# 26. n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику? Программа получает на вход сперва число n, а потом k.

n, k = int(input()), int(input())
print(k // n)

# 27. У вас есть N рублей и вы хотите купить максимальное количество пар кроссовок по цене R рублей. Сколько пар кроссовок Вы можете себе купить?
#     На вход программе поступают два натуральных числа N и R

(lambda n, k: print(n // k)) (int(input()), int(input()))

# 28. Программе поступает на вход одно целое положительное число, ваша задача вывести его последнюю цифру

print(int(input()) % 10)

# 29. Дано целое положительное число, ваша задача вывести разряд сотен этого числа

print(int(input()) // 100 % 10)

# 30. Дано целое положительное трехзначное число, ваша задача найти сумму разрядов этого числа

print((x := int(input())) // 100 + x // 10 % 10 + x % 10)