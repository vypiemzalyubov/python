# 355. Давайте начнем с легкого примера. Создадим функцию с именем keanu_reeves, которая выводит сообщение "YOU'RE BREATHTAKING".and
#      Ваша задача написать только определение функции keanu_reeves.

def keanu_reeves():
    print("YOU'RE BREATHTAKING")

# 356. Всеми любимая программа «hello world». Создайте функцию с именем say_hello_world , которая принимает на вход имя человека в виде строки и печатает фразу «{name} говорит hello world!»
#      Ваша задача написать только определение функции say_hello_world.

def say_hello_world(name):
    print(f'{name} говорит hello world!')

# 357. Напишите функцию summa_n, которая принимает одно целое положительное t число и находит сумму всех чисел от 1 до t включительно. Программа должна распечатать сообщение:
#      "Я знаю, что сумма чисел от 1 до {t} равна {S}", где в качестве t и S вам необходимо подставить значения (см. тестовые данные).
#      Ваша задача написать только определение функции summa_n, вызывать ее не нужно.

def summa_n(t):
    s = sum(range(1, t + 1))
    print(f'Я знаю, что сумма чисел от 1 до {t} равна {s}')

# 358. Напишите функцию exponentiation, которая принимает на вход целое число и выводит на экран через пробел квадрат и куб этого числа. 
#      Вам необходимо написать только определение функции exponentiation.

def exponentiation(x):
    print(f'{x ** 2} {x ** 3}')

# 359. Напишите функцию sum_num для суммирования всех цифр строки. 
#      Функция должна принимать строку, суммировать все ее символы, которые являются цифрами, и в качестве ответа выводить найденную сумму.
#      Вам необходимо написать только определение функции sum_num.

def sum_num(s):
    print(sum(int(i) for i in s if i.isdigit()))

# 360. Напишите функцию get_body_mass_index, которая принимает массу тела человека в кг и рост в см и рассчитывает индекс массы тела человека по формуле:
#      index = масса / рост ** 2
#      Рост указывается в формуле в метрах, а не в сантиметрах.
#      Функция и должна вывести на экран информацию о массе человека, отталкиваясь от найденного индекса:
#      - если индекс < 18.5 программа должна вывести Недостаточная масса тела
#      - если 18.5 <= индекс <= 25 программа должна вывести Норма
#      - если индекс > 25 программа должна вывести Избыточная масса тела
#      Вам необходимо написать только определение функции get_body_mass_index.

def get_body_mass_index(weight, height):
    index = weight / ((height / 100)) ** 2
    print('Недостаточная масса тела' if index < 18.5 else 'Избыточная масса тела' if index > 25 else 'Норма')

# 361. Напишите функцию check_password, которая проверяет переданный ей пароль на сложность и печатает на экран результат проверки.
#      Сложным паролем будет считаться комбинация символов, в которой:
#      - Есть хотя бы 3 цифры
#      - Есть хотя бы одна заглавная буква 
#      - Есть хотя бы один символ из следующего набора "!@#$%*"
#      - Общая длина не менее 10 символов
#      Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password", в противном случае - "Easy peasy".
#      Вам необходимо написать только определение функции check_password.

def check_password(password):
    len_digit = title_char = spec_char = 0
    for i in password:
        if i.isdigit():
            len_digit +=1
        if i.isupper():
            title_char += 1
        if i in '!@#$%*':
            spec_char += 1
    print('Perfect password' if len_digit >= 3 and title_char and spec_char and len(password) >= 10 else 'Easy peasy')
    
# 362. Создайте функцию count_letters, которая принимает на вход фразу и подсчитывает, какое количество в ней строчных(K) и заглавных (N) букв, 
#      все остальные символы игнорируются. Функция должна вывести на экран информацию о найденных буквах в определенном формате:
#      Количество заглавных символов: N
#      Количество строчных символов: K
#      Вам необходимо написать только определение функции count_letters.

def count_letters(s):
    n = k = 0
    for char in s:
        n += char.isupper()
        k += char.islower() 
    print(f'Количество заглавных символов: {n}\nКоличество строчных символов: {k}')

# 363. Напишите функцию repeat_please_n_times, которая принимает один аргумент n - натуральное число. 
#      Функция repeat_please_n_times должна n раз распечатать фразу "Just do it" в отдельной строчке.
#      Ваша задача написать только определение функции repeat_please_n_times, вызывать ее не нужно.

def repeat_please_n_times(n):
    for i in range(n):
        print('Just do it')

# 364. Напишите функцию is_between, которая принимает три аргумента и печатает True, если первое число находится между двумя вторыми включительно, и False в противном случае.
#      Ваша задача дописать только тело функции is_between.

def is_between(name, surname, middlename):
    print(b <= a <= c or c <= a <= b)

a, b, c = map(int, input().split())

is_between(a, b, c)

# 365. Напишите функцию count_letter(text, letter), которая принимает два параметра:
#      - text – текст, в котором нужно посчитать сколько раз появилась буква letter, учитывая регистр буквы;
#      - letter – буква, количество которой мы должны посчитать в text.
#      Функция count_letter должна выводить на экран найденное количество букв  letter в тексте text.
#      Ваша задача дописать только тело функции count_letter.

def count_letter(text, letter):
    print(sum([i.count(symbol) for i in text]))
    
text = input()
symbol = input()

count_letter(text, symbol)

# 366. Напишите функцию print_initials(name, surname, middlename), которая принимает три параметра:
#      - name – имя человека;
#      - surname – фамилия человека;
#      - middlename– отчество человека;
#      а затем выводит на печать фамилию и инициалы в определенном формате (первая буква фамилии должна стать заглавной, все остальные строчные; 
#      в имени и отчестве остаются только по одной букве в верхнем регистре).
#      Ваша задача дописать только тело функции print_initials.

def print_initials(name, surname, middlename):
    print(f'{surname.title()} {name.upper()[0]}.{middlename.upper()[0]}.')

name = input()
surname = input()
middlename = input()

print_initials(name, surname, middlename)

# 367. Ниже в коде представлено несколько проверок. Ваша задача исправить код так, чтобы все проверки прошли.

assert 200 > 100                             
assert [100] * 4 < [100, 100, 100, 10000]    
assert sum([1, 3, 5]) == sum([6, 3])             
assert max(3, -1, 9) != -1                   
print('Проверки пройдены')

# 368. Давайте считать человека подростком, если его возраст находится в пределах от 12 до 17 лет включительно. Напишите функцию is_person_teenager, 
#      которая помогает по возрасту определить является ли человек подростком или нет. Функция is_person_teenager принимает на вход возраст человека и возвращает True или False.
#      Нужно написать только определение функций is_person_teenager.

def is_person_teenager(age):
    return 12 <= age <= 17

# 369. Напишите функцию factorial, которая принимает на вход одно неотрицательное число, и возвращает значение факториала данного числа.
#      Нужно написать только определение функции factorial.

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

n = int(input())
print(factorial(n))

# 370. Напишите функцию generate_fizz_buzz_list, которая принимает одно целое число n - размер списка. Функция generate_fizz_buzz_list должна:
#      - обойти числа от 1 до n включительно и для каждого такого числа выполнить последовательно проверки с пункта 2 по пункт 5
#      - Если число кратно и трем, и пяти, то в список заносим строку FizzBuzz 
#      - Если число кратно трем, то в список заносим строку Fizz
#      - Если число кратно пяти, то в список заносим строку Buzz
#      - Если число не кратно ни трем ни пяти, то в список заносим само это число
#      В итоге функция generate_fizz_buzz_list должна вернуть сформированный список из n элементов. Ваша задача написать только определение функции generate_fizz_buzz_list.

def generate_fizz_buzz_list(n):
    return ["FizzBuzz" if not i % 3 and not i % 5 else "Fizz" if not i % 3 else "Buzz" if not i % 5 else i for i in range(1, n + 1)]

# 371. В этой задаче вам необходимо воспользоваться уже готовой функцией gcd(a, b), которая принимает два числа и находит наибольших общий делитель для них.
#      Ваша задача при помощи функции gcd определить НОД произвольного количества чисел.
#      Входные данные: На первой строке вводится натуральное число n – количество чисел. Далее идут n строк, в каждой из которых натуральное число.
#      Выходные данные: НОД введенных чисел.

from functools import reduce

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

l = [int(input()) for _  in range(int(input()))]
print(reduce(gcd, l))

# 372. Ваша задача написать функцию find_duplicate, которая принимает один аргумент - список чисел. Функция должна возвращать список из дублей, 
#      каждый дубль нужно брать только один раз в том порядке, в котором они встречаются в исходном списке. Под дублем будем подразумевать число, которое присутствовало в списке несколько раз. 
#      find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]) => [1, 2]
#      find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]) => [2, 1]
#      find_duplicate([1, 2, 3, 4]) => []
#      find_duplicate([1, 2, 3, 4, 3]) => [3]
#      Ваша задача написать только определение функции find_duplicate.

def find_duplicate(lst):
    l = []
    for i in lst:
        if lst.count(i) > 1 and i not in l:
            l.append(i)
    return l

assert find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]) == [1, 2]
assert find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]) == [2, 1]
assert find_duplicate([1, 2, 3, 4]) == []
assert find_duplicate([8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8]) == [8, 7, 6, 5, 4]
print('Все успешно')

# 373. Напишите функцию first_unique_char, которая принимает строку символов и возвращает целое число: позицию первого уникального символа в строке. 
#      В случае, если уникальных символов в переданной строке нет, верните -1. Регистр символов не учитывайте.
#      Ваша задача написать только определение функции first_unique_char.

def first_unique_char(s):
    for i, n in enumerate(s):
        if s.count(n) == 1:
            return i
    return -1

s = input()
print(first_unique_char(s))

# 374. Ваша задача написать функцию format_name_list, которая принимает список словарей, у каждого словаря в этом списке есть только ключ name.
#      Функция format_name_list должна вернуть строку, в которой все имена из списка разделяются запятой кроме последних двух имен, они должны быть разделены союзом "и". 
#      Если в списке нет ни одного имени, функция должна вернуть пустую строку. Ниже представлены примеры:
#      format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) => 'Bart, Lisa и Maggie'
#      format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]) => 'Bart и Lisa'
#      format_name_list([{'name': 'Bart'}]) => 'Bart'
#      format_name_list([]) => ''
#      Ваша задача написать только определение функции format_name_list.

def format_name_list(names: list):
    tmp = [i['name'] for i in names]
    if len(tmp) == 0:
        return ''
    elif len(tmp) == 1:
        return tmp[0]
    s = ', '.join(tmp[0:-1])
    return f'{s} и {tmp[-1]}'

assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]) == 'Bart, Lisa, Maggie, Homer и Marge'
assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) == 'Bart, Lisa и Maggie'
assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]) == 'Bart и Lisa'
assert format_name_list([{'name': 'Bart'}]) == 'Bart'
assert format_name_list([]) == ''
assert format_name_list([{'name': 'Maggie'}, {'name': 'Lisa'}, {'name': 'Barney'}, {'name': 'Homer'}, {'name': 'Bart'}, {'name': 'Moe'}]) == 'Maggie, Lisa, Barney, Homer, Bart и Moe'
assert format_name_list([{'name': 'Marge'}, {'name': 'Maggie'}, {'name': 'Seymour'}]) == 'Marge, Maggie и Seymour'
assert format_name_list([{'name': 'Maude'}, {'name': 'Bart'}]) == 'Maude и Bart'
print('Проверки пройдены')

# 375. Ваша задача написать функцию get_domain_name, которая принимает строку url, извлекает из нее доменное имя и возвращает его в качестве строки.
#      get_domain_name("http://google.com") => "google"
#      get_domain_name("http://google.co.jp") => "google"
#      get_domain_name("www.xakep.ru") => "xakep"
#      get_domain_name("https://youtube.com") => "youtube"
#      get_domain_name("https://www.asos.com") => "asos"
#      get_domain_name("http://www.lenovo.com") => "lenovo"
#      Строка url может начинаться с протоколов http://  https:// или с www. URL, начинающиеся с протоколов http://  https://, могут также содержать www.
#      Ваша задача написать только определение функции get_domain_name.

def get_domain_name(url):
    s = url.replace('http://', '').replace('https://', '').replace('www.', '', 1)
    return s.split('.')[0]

assert get_domain_name("http://google.com") == "google"
assert get_domain_name("http://google.co.jp") == "google"
assert get_domain_name("www.xakep.ru") == "xakep"
assert get_domain_name("https://youtube.com") == "youtube"
assert get_domain_name("http://github.com/carbonfive/raygun") =='github'
assert get_domain_name("http://www.zombie-bites.com") == 'zombie-bites'
assert get_domain_name("https://www.siemens.com") == 'siemens'
assert get_domain_name("https://www.whatsapp.com") == 'whatsapp'
assert get_domain_name("https://www.mywww.com") == 'mywww'
print('Проверки пройдены')

# 376. В этой задаче вам необходимо воспользоваться уже готовой функцией factorial, которая принимает неотрицательное число, и возвращает значение факториала данного числа.
#      Ваша задача создать функцию trailing_zeros, которая принимает неотрицательное число, находит его факториал и возвращает сколько нулей на конце этого факториала.
#      trailing_zeros(6) =>  1, потому что 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720
#      trailing_zeros(10) => 2, потому что 10! = 3 628 800
#      trailing_zeros(20) => 4, потому что 20! = 2 432 902 008 176 640 000
#      Нужно написать только определение функций trailing_zeros и factorial.

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

def trailing_zeros(n):
    x = factorial(n)
    count = 0
    while x % 10 == 0:
        count += 1
        x //= 10
    return count 

assert trailing_zeros(0) == 0
assert trailing_zeros(6) == 1
assert trailing_zeros(30) == 7
assert trailing_zeros(12) == 2      
print('Проверки пройдены')

# 377. К азотистым основаниям относят аденин (A), гуанин (G), цитозин (C) и тимин (T), который входит в состав только ДНК. Они обладают схожими структурами и химическими свойствами. 
#      Это гетероциклические органические соединения, производные пиримидина и пурина, входящие в состав нуклеотидов. 
#      Аденин и гуанин — производные пурина, а цитозин и тимин — производные пиримидина.
#      В этой задаче вам необходимо создать функцию count_AGTC, которая принимает на вход строку - последовательность ДНК, состоящая только из символов A, G, T, C. 
#      Функция count_AGTC должна подсчитать количество каждого элемента в переданной последовательности и вернуть кортеж из найденных четырех количеств. 
#      Порядок элементов в кортеже должен быть именно таким A, G, T, C
#      count_AGTC('AGGTC') => (1, 2, 1, 1)
#      count_AGTC('AAAATTT') => (4, 0, 3, 0)
#      count_AGTC('AGTTTTT') => (1, 1, 5, 0)
#      count_AGTC('CCT') => (0, 0, 1, 2)
#      Нужно написать только определение функции count_AGTC.

def count_AGTC(dna):
    return dna.count('A'), dna.count('G'), dna.count('T'), dna.count('C')

assert count_AGTC('AGGTC') == (1, 2, 1, 1)
assert count_AGTC('AAAATTT') == (4, 0, 3, 0)
assert count_AGTC('AGTTTTT') == (1, 1, 5, 0)
assert count_AGTC('CCT') == (0, 0, 1, 2)     
print('Проверки пройдены')

# 378. Ниже имеется готовая функция add_binary, которая принимает два числа и возвращает их сумму в двоичной системе счисления.
#      Ваша задача только добавить докстроку «Возвращает сумму чисел a и b в двоичном виде».

def add_binary(a, b):
    """Возвращает сумму чисел a и b в двоичном виде"""
    binary_sum = bin(a+b)[2:]
    return binary_sum

# 379. Напишите функцию first_repeated_word , которая принимает строку, состоящую из нескольких слов, слова разделяются между собой пробелом. 
#      Функция должна найти первое повторяющееся слово и вернуть его в качестве результата. Если передана строка, в которой все слова различны, функция first_repeated_word должна вернуть None.
#      Регистр букв при сравнении нужно учитывать
#      first_repeated_word("ab ca bc ab") => "ab"
#      first_repeated_word("ab ca bc Ab cA aB bc") => "bc"
#      first_repeated_word("ab ca bc ca ab bc") => "ca"
#      first_repeated_word("ab ca bc") => None
#      Для функции first_repeated_word нужно добавить док-строку "Находит первый дубль в строке" и не забудьте проаннотировать аргументы и возврат функции.
#      Нужно написать только определение функции first_repeated_word.

def first_repeated_word(s: str, st = set()) -> str|None:
    """Находит первый дубль в строке"""
    for i in s.split():
        if i not in st: st.add(i)
        else: return i

# 380. Напишите функцию shift_letter , которая принимает два аргумента:
#      - letter одна английская буква в нижнем регистре
#      - shift целое число - значение сдвига буквы (может быть как положительным, так и отрицательным)
#      Функция shift_letter  сдвигает символ letter вперед или назад на заданное значение shift .Сдвиг может быть цикличным в пределах от a до z. Ниже примеры:
#      shift_letter('b', 2)=> 'd'
#      shift_letter('d', 1) => 'e'
#      shift_letter('z', 1) => 'a'
#      shift_letter('d', -2) => 'b'
#      shift_letter('d', 26) => 'd'
#      shift_letter('b', -3) => 'y'
#      Не забудьте проаннотировать аргументы и также добавьте doc-строку «Функция сдвигает символ letter на shift позиций».
#      Функция shift_letter должна вернуть новый символ. Вот вам в помощь ascii коды английских буквы, вам нужны только символы в нижнем регистре.
#      Нужно написать только определение функции shift_letter.

def shift_letter(letter: str, shift: int) -> str:
    '''Функция сдвигает символ letter на shift позиций'''
    char = ord(letter) + shift
    while char not in range(97, 123):
        if char < 97: char += 26
        else: char -= 26
    return chr(char)

# 381. На основании предыдущей задачи мы с вами можем реализовать знаменитый шифр Цезаря. Этот шифр брал каждую букву исходной фразы и смещал ее на значение ключа, это так раз был на сдвиг. 
#      В пределах кодирования одной фразы значение сдвига всегда постоянно. И так, ваша задача создать функцию caesar_cipher , которая принимает на вход текст и значение сдвига.
#      Внутри функции caesar_cipher  необходимо последовательно пройтись по каждому символу и преобразовать его по следующим правилам:
#      - если символ является знаком пунктуации, оставляем его как есть
#      - если это буква, то сместить ее при помощи ранее написанной функции shift_letter 
#      Закодированный текст необходимо вернуть в качестве ответа. Вот пример работы:
#      caesar_cipher('leave out all the rest', -1) => 'kdzud nts zkk sgd qdrs'
#      caesar_cipher('one more light', 3) => 'rqh pruh oljkw'
#      Аннотации, мой друг, не забываем прописывать. И еще нужно сделать док-строку для функции caesar_cipher со значением «Шифр цезаря».
#      Нужно написать только определение функций shift_letter и caesar_cipher.

def shift_letter(letter: str, shift_1: int) -> str:
    '''Функция сдвигает символ letter на shift позиций'''
    return chr((ord(letter) - 97 + shift_1) % 26 + 97)

def caesar_cipher(text: str, shift_2: int) -> str:
    """Шифр цезаря"""
    answer = ''
    for symbol in text:
        if symbol.isalpha(): answer += shift_letter(symbol, shift_2)
        else: answer += symbol
    return answer

# 382. Напишите функцию, которая принимает имя и возраст водителя. Функция должна распечатать на экран заключение, может ли данный водитель управлять транспортом
#      и определять она должна это по возрасту водителя: он должен быть больше или равен MIN_DRIVING_AGE.
#      Если водитель может управлять, выведите фразу "<name> может водить" , в противном случае "<name> еще рано садиться за руль".
#      MIN_DRIVING_AGE = 18
#      allowed_driving('tim', 17) # выведет "tim еще рано садиться за руль"
#      allowed_driving('bob', 18) # выведет "bob может водить"

MIN_DRIVING_AGE = 18

def allowed_driving(name: str, age: int) -> None:
    print(f'{name} может водить' if age >= MIN_DRIVING_AGE else f'{name} еще рано садиться за руль')

# 383. В этой задаче вам необходимо создать функцию get_word_indices, которая принимает список строк и возвращает словарь, 
#      где ключи - это уникальные слова из списка строк в нижнем регистре, а значения - это списки индексов строк, в которых эти слова встречаются.
#      assert get_word_indices(['This is a string',
#                               'test String',
#                               'test',
#                               'string']) => {'this': [0], 'is': [0], 'a': [0],
#                                             'string': [0, 1, 3], 'test': [1, 2]}
#      get_word_indices(['Look at my horse',
#                         'my horse',
#                         'is amazing']) => {'look': [0], 'at': [0], 'my': [0, 1],
#                                            'horse': [0, 1], 'is': [2], 'amazing': [2]}
#      get_word_indices([]) => {}
#      get_word_indices(['Avada Kedavra',
#                        'avada kedavra',
#                        'AVADA KEDAVRA']) => {'avada': [0, 1, 2],
#                                              'kedavra': [0, 1, 2]}
# Регистр букв не учитывается поэтому слова «String» и «STRING» считаются одинаковыми.
# Нужно написать только определение функции get_word_indices.

def get_word_indices(strings: list[str]) -> dict:
    d = {}
    for i, v in enumerate(strings):
        for j in v.lower().split():
            d[j] = d.get(j, []) + [i]
    return d

# 384. Напишите функцию replace, которая принимает три параметра:
#      - обязательный строковый параметр text - текст, в котором необходимо выполнить замены;
#      - обязательный строковый параметр old - строка поиска для замены;
#      - необязательный строковый параметр new - значение замены для найденного значения old. По умолчанию равен пустой строке.
#      Функция replace должна возвращать новую строку, в которой все символы old были заменены на new. При замене регистр букв должен учитываться.
#      replace('Нет', 'т') => 'Не'
#      replace('Bella Ciao', 'a') => 'Bell Cio'
#      replace('nobody; i myself farewell analysis', 'l', 'z') => 'nobody; i mysezf farewezz anazysis'
#      replace('commend me to my kind lord meaning', 'M', 'w') => 'commend me to my kind lord meaning'
#      Ваша задача дописать только тело функции replace.

def replace(text: str, old: str, new: str = ''):
    return text.replace(old, new)

# 385. В HTML используются специальные теги для определения заголовков в веб-странице.
#      Всего существует шесть тегов заголовков HTML:
#      <h1> - заголовок первого уровня;
#      <h2> - заголовок второго уровня;
#      <h3> - заголовок третьего уровня;
#      <h4> - заголовок четвертого уровня;
#      <h5> - заголовок пятого уровня;
#      <h6> - заголовок шестого уровня.
#      Разница между заголовками только в размере.
#      Ваша задача создать функцию make_header, которая принимает:
#      - обязательный параметр - строку, которую нужно обернуть в тег заголовка
#      - необязательный числовой параметр - уровень заголовка, по умолчанию принимает значение 1.
#      Функция make_header должна возвращать переданную строку в обернутый тег заголовка определенного уровня.
#      make_header('Нет') => '<h1>Нет</h1>'
#      make_header('Bella Ciao', 4) => '<h4>Bella Ciao</h4>'
#      make_header('Go little rock star', 6) => '<h6>Go little rock star</h6>'
#      make_header('Девальвации не будет. Твердо и четко') => '<h1>Девальвации не будет. Твердо и четко</h1>'
#      Ваша задача дописать только тело функции make_header.

def make_header(text: str, level: int = 1) -> str:
    return f'<h{level}>{text}</h{level}>'

# 386. Ваша задача создать функцию create_matrix, которая принимает:
#      - необязательный числовой параметр size - размер квадратной матрицы, по умолчанию принимает значение 3;
#      - необязательный числовой параметр up_fill - значение заполнителя элементов, находящихся выше главной диагонали. По умолчанию равен 0;
#      - необязательный числовой параметр down_fill - значение заполнителя элементов, находящихся ниже главной диагонали. По умолчанию равен 0;
#      Функция create_matrix должна возвращать квадратную матрицу размером size х size, на диагонали которой располагаются числа от 1 до size. 
#      Все остальные элементы заполнены согласно параметрам up_fill и down_fill.
#      create_matrix() => [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
#      create_matrix(4) => [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]]
#      create_matrix(up_fill=7) => [[1, 7, 7],
#                                  [0, 2, 7],
#                                  [0, 0, 3]]
#      create_matrix(up_fill=7, down_fill=9) => [[1, 7, 7],
#                                               [9, 2, 7],
#                                               [9, 9, 3]]
#      create_matrix(size=4, up_fill=7, down_fill=9) => [[1, 7, 7, 7],
#                                                       [9, 2, 7, 7],
#                                                       [9, 9, 3, 7],
#                                                       [9, 9, 9, 4]]
#      Ваша задача дописать только тело функции create_matrix.

def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0) -> list[list[int]]:
    tmp = [[i] * size for i in range(1, size + 1)]
    for i in range(size):
        for j in range(size):
            if i < j: tmp[i][j] = up_fill
            if i > j: tmp[i][j] = down_fill
    return tmp