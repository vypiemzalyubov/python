# 1. В переменную s записана строка с текстом. Сделайте эту строку сырой, и посмотрите, что изменится в выводе.

s = r"Последовательность \n используется для переноса строк"
print(s)

# 2. На вход программе подаётся целое число. Выведите в консоль строку вида: a * a = b, где a - полученное число, а b - результат произведения числа a на само себя.

a = int(input())
b = a * a
print(f'{a} * {a} = {b}')

# 3. Выведите в консоль следующую строку: \\\'. Попробуйте решить задачу двумя способами.

print(r"\\\'")
print('\\\\\\' + '\'')

# 4.На вход программе подаётся два целых числа a и b, каждое на новой строке.
#   Выведите в консоль строку вида: a\n + \nb\n = \nc, где a и  b - полученные числа, а c - их сумма.

a = int(input())
b = int(input())
c = a + b
print(f'{a}\\n + \\n{b}\\n = \\n{c}')

# 5. Напишите регулярное выражение, которое найдёт все последовательности тест в тексте.

regex = r'тест'

# 6. Напишите регулярное выражение, которое найдёт все последовательности ТеСт в тексте.

regex = r'ТеСт'

# 7. Напишите регулярное выражение, которое найдёт все последовательности ты в тексте.

regex = r'ты'

# 8. В прошлом задании мы также находили последовательности ты даже в таких словах, как цветы. 
#    Попробуйте найти все слова ты, не последовательности. Словами будем считать последовательность букв, отделённую с двух сторон пробелами.

regex = r' ты '

# 9. Напишите регулярное выражение, которое найдёт все последовательности \n в тексте.

regex = r'\\n'

# 10. Напишите регулярное выражение, которое найдет все последовательности: сон, сок, сом.

regex = r'со[кнм]'

# 11. Напишите регулярное выражение, которое найдёт все последовательности Привет и привет в тексте.

regex = r'[Пп]ривет'

# 12. Дано регулярное выражение [12346789]. Запишите его сокращённую версию в переменную regex.

regex = r'[1-46-9]'

# 13. Напишите регулярное выражение, которое найдёт все цифры из шестнадцатеричной системы счисления.

regex = r'[0-9A-F]'

# 14. Напишите регулярное выражение, которое найдёт все кабинеты с трёхзначным номером: 100 - 999. 

regex = r'[1-9][0-9][0-9] кабинет'

# 15. Напишите регулярное выражение, которое находит все шестизначные коды подтверждения.

regex = r'[0-9]{6}'

# 16. Напишите регулярное выражение, которое найдёт все последовательности из любых пяти символов, кроме перехода на следующую строку.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Состоит из 5 символов
#     Используются все символы, кроме перехода на новую строку

regex = r'.{5}'

# 17. Напишите регулярное выражение, которое найдёт все трёхбуквенные слова.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Состоит из 3 букв
#     Используется латинский и кириллический алфавиты верхнего и нижнего регистров
#     Окружена пробелами с двух сторон

regex = r' [A-Za-zА-Яа-яёЁ]{3} '

# 18. Из-за того, что вхождения в регулярных выражениях не пересекаются, мы потеряли некоторые слова в прошлом задании. Попробуйте вместо пробелов использовать шаблон \b, и посмотреть что получится.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Состоит из 3 букв
#     Используется латинский и кириллический алфавиты верхнего и нижнего регистров
#     Слева и справа от последовательности стоят промежутки \b

regex = r'\b[A-Za-zА-Яа-яёЁ]{3}\b'

# 19. Напишите регулярное выражение, которое найдёт четырёхбуквенное слово в начале строки.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Состоит из 4 букв
#     Используется латинский и кириллический алфавиты верхнего и нижнего регистров
#     Стоит в начале строки
#     Справа от последовательности граница слова

regex = r'^[A-Za-zА-Яа-яЁё]{4}\b'

# 20. Напишите регулярное выражение, которое найдёт все многоточия в тексте.

regex = r'\.{3}'

# 21. Напишите регулярное выражение, которое найдёт все use strict; и use strict в тексте.

regex = 'use strict;?'

# 22. Абитуриент Александр пытается поступить в университет. Но вот незадача. В документах, описывающих процесс поступления, так много аббревиатур, 
#     что читать их становится невозможно. Он решил найти все аббревиатуры с помощью регулярных выражений и потом посмотреть их значения в интернете. 
#     Помогите Александру написать регулярное выражение, которое найдёт все аббревиатуры.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Состоит как минимум из 2-ух букв
#     Используется латинский и кириллический алфавиты верхнего регистра

regex = r'[A-ZА-ЯЁ]{2,}'

# 23. В России используются регистрационные знаки нескольких типов. Найдите все валидные знаки типа 1 и 1А.
#     Нужно найти номерные знаки 1 и 1А, подходящие по следующим условиям:
#     Левая часть:
#     Используются арабские цифры и 12 букв кириллицы в нижнем регистре, имеющие графические аналоги в латинском алфавите: авекмнорстух
#     Правая часть (регион):
#     Регионом считаем любую последовательность арабских цифр длиной от 2 до 3 включительно
#     Номера не могут быть подпоследовательностью, они должны быть отделены
#     Да, в номерных знаках используются заглавные буквы, но в задании используются буквы в нижнем регистре. 

regex = r'\b[авекмнорстух]\d{3}[авекмнорстух]{2}\d{2,3}\b'

# 24. Напишите регулярное выражение, которое найдёт все IMEI в тексте.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Состоит из 15 арабских цифр
#     Не является подпоследовательностью

regex = r'\b\d{15}\b'

# 25. Напишите регулярное выражение, которое найдёт все пары координат в тексте: широту и долготу.
#     Нужно найти все пары координат, подходящие по следующим условиям:
#     Координата:
#     Может быть отрицательной или положительной
#     В левой части может стоять от 1 до 3 арабских цифр включительно
#     В правой части количество цифр неограничено
#     Левая и правая части разделены точкой
#     Координаты разделены пробелами
#     Т.е. нужно написать регулярное выражение, которое будет искать 2 координаты, разделённые пробелом.

regex = r'\b-?\d{1,3}\.\d* -?\d{1,3}\.\d*\b'

# 26. Напишите регулярное выражение, которое найдёт все адреса ETH кошельков.
#     Адрес ETH кошельков состоит из двух частей:
#     Левая часть (префикс): 
#     0x
#     Правая часть (регион):
#     Длина 40 символов
#     Исползуются все символы шестнадцатеричной системы счисления в нижнем и верхнем регистрах
#     Адрес не может быть подпоследовательностью, он должен быть отделён

regex = r'0x[A-Fa-f0-9]{40}'

# 27. Напишите регулярное выражение, которое извлекает протокол полученной ссылки: http или https. Если протокола нет - ничего искать не надо.

regex = r'\bhttp[s]?\b'

# 28. Напишите регулярное выражение, которое найдёт все числа, написанные с помощью римских цифр.

regex = r'\b[A-Z]+\b'

# 29. Составьте регулярное выражение, которое найдёт все смайлики в тексте.
#     Смайлик состоит из трёх частей: глаз, носа (который может отсутствовать) и рта. В них используются следующие символы:
#     Глаза: :8;¦=
#     Нос: ^-
#     Рот: |\0()/PODIC

regex = r'[:8;¦=][\^\-]?[\|\\\\\\0\()\/PODIC]'

# 30. Напишите регулярное выражение, которое разделит число из тестовых данных на числа, в конце которых стоит единица. 
#     Это число будет единицей, только если перед ним не будет других цифр.
#     Что нужно найти:
#     Все последовательности арабских цифр с минимально возможной длиной, заканчивающиеся на 1.

regex = r'\d*?1'

# 31. Составьте регулярное выражение, которое найдёт все чётные числа в тестовой строке.
#     Что нужно найти:
#     Все чётные числа с минимально возможной длиной.

regex = r'\d*?[24680]'

# 32. Напишите регулярное выражение, которое найдёт все квадратные скобки и их содержимое.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     В начале и в конце последовательности стоят квадратные скобки
#     Между квадратными скобками могут находиться последовательности из любых символов
#     Длина последовательности должна быть минимально возможной

regex = r'\[.*?\]'

# 33. Напишите регулярное выражение, которое найдёт минимальную последовательность, начинающуюся на букву и заканчивающуюся буквой.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Начинается и заканчивается буквой
#     Используются буквы из латинского и кириллического алфавитов верхнего и нижнего регистров
#     Между буквами могут находиться последовательности из любых символов
#     Длина последовательности должна быть минимально возможной

regex = r'[A-Za-zА-Яа-яЁё].*?[A-Za-zА-Яа-яЁё]'

# 34. Напишите регулярное выражение, которое найдёт все последовательности символов, окруженные двойными кавычками.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     В начале и в конце последовательности стоят двойные кавычки: "
#     Между кавычками могут находиться последовательности из любых символов
#     Между кавычками стоит как минимум один символ
#     Длина последовательности должна быть минимально возможной

regex = r'\".{0,}?"*\"'

# 35. Напишите регулярное выражение, которое найдёт все теги img в тексте.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Начинается с <img
#     Заканчивается на >
#     Между началом и концом могут находиться последовательности из любых символов

regex = r'<img.*?>'

# 36. Напишите регулярное выражение, которое найдёт все повторяющиеся последовательности из трёх цифр, которые идут друг за другом. Для этого используйте скобочные группы.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     В левой части любая последовательность из 3 арабских цифр
#     В правой части точно такая же последовательность

regex = r'([0-9]{3})\1+?'

# 37. Напишите регулярное выражение, которое найдёт все слова и словосочетания, состоящие из двух одинаковых частей. Между одинаковыми половинами слова может стоять дефис.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     В левой части любая последовательность букв кириллического алфавита нижнего регистра
#     В правой части точно такая же последовательность
#     Между ними может стоять тире
#     Последовательность не может быть подпоследовательностью

regex = r'\b(?P<word>[а-яё]+)-*?(?P=word)\b'

# 38. Напишите регулярное выражение, которое найдёт все повторяющиеся буквы в тексте.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Последовательность из 2 одинаковых букв
#     Используются буквы латинского и кириллического алфавитов нижнего и верхнего регистров

regex = r'([A-Za-zА-Яа-яЁё]+)\1'

# 39. Напишите регулярное выражение, которое найдёт все повторяющиеся последовательности из двух цифр, которые идут друг за другом. Используйте нумерованные группы.
#     Что нужно найти:
#     Нужно найти последовательности из 2 одинаковых арабских цифр

regex = r'([0-9][0-9])\1'

# 40. Напишите регулярное выражение, которое найдёт все последовательности if и <if>, но не <if и if>, стоящие между началом и концом строки.
#     Что нужно найти:
#     Последовательности if без скобок или со скобками, стоящими с двух сторон: if и <if>
#     Последовательность стоит в начале строки
#     После последовательности строка заканчивается

regex = r'^(\<)?if(?(1)\>|)$'

# 41. Напишите регулярное выражение, которое получит последовательность из любых символов от [^START] до {(END.)}.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Слева от неё стоит [^START]
#     Справа от неё стоит {(END.)}
#     Состоит из любых символов, кроме символа перехода на новую строку

regex = r'(?<=\[\^START\]).*(?=\{\(END\.\)\})'

# 42. Напишите регулярное выражение, которое найдёт все символы /, слева и справа от которых ничего нет или стоят другие символы, не равные /.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Слева от неё не стоит /
#     Справа от неё не стоит /
#     Последовательность состоит из одного слеша: /

regex = r'(?<!\/)\/(?!\/)'

# 43. Напишите регулярное выражение, которое найдёт все последовательности x с чётной длиной.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Состоит из символов x
#     Длина последовательности чётная
#     Последовательность не может быть подпоследовательностью

regex = r'(?<!x)(xx)*(?!x)'

# 44. Напишите регулярное выражение, которое найдёт все имена и названия в тексте. 
#     Слова в начале предложения не считаются, так как невозможно проверить это имя или просто слово с заглавной буквы.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Последовательность букв, которая начинается на заглавную букву
#     Используется кириллический алфавит нижнего и верхнего регистров
#     Последовательность не стоит в начале предложения
#     Перед последовательностью не должно заканчиваться предложение, т.е. не стоит: .!?

regex = r'(?<!\. )(?<!\A)[А-ЯЁ][а-яё]*\b'

# 45. Напишите регулярное выражение, которое найдёт все неотрицательные числа.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Состоит из арабских цифр
#     Перед последовательностью не стоит минус
#     Не является подпоследовательностью

regex = r'\b(?<!-)[0-9]+'