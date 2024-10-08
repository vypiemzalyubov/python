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

# 46. Напишите регулярное выражение, которое найдёт в тексте следующие языки программирования: JavaScript, C++, Python.

regex = r'(JavaScript|C\+\+|Python)'

# 47. Найдите все слова да, нет, наверное в тексте. Они могут начинаться с букв разных регистров. Не являются подпоследовательностью

regex = r'\b(?:(да|Да))\b|\b(?:(нет|Нет))\b|\b(?:(наверное|Наверное))\b'

# 48. Криптостример Григорий отмывает грязные деньги через миксеры, а также через пару своих кошельков. Но вот незадача, он потерял адрес своего биткоин кошелька, 
#     на который должны прийти все монеты. Помогите Грише. Напишите регулярное выражение, которое найдёт все адреса биткоин кошельков.
#     Что нужно найти:
#     Адрес представляет собой набор из префикса (1, или 3, или bc1) и основной части длиной от 27 до 34 символов.
#     В основной части используются:
#     Весь латинский алфавит, кроме: O, I, l.
#     Все арабские цифры, кроме 0.

regex = r'\b(?:(1|3|bc1))[1-9a-km-zA-HJ-NP-Z]{27,34}\b'

# 49. Напишите регулярное выражение, которое найдёт следующие последовательности в тексте:
#     Привет, Олег
#     Привет, Григорий
#     Пока, Олег
#     Пока, Григорий

regex = r'(?:(Привет,|Пока,)) (?:(Олег|Григорий))'

# 50. Напишите регулярное выражение, которое найдёт следующие последовательности в тексте:
#     я готов
#     я готова
#     ты готов
#     ты готова
#     он готов
#     она готова
#     мы готовы
#     вы готовы
#     они готовы

regex = r'\b(?:(я|ты)) (?:(готова|готов))\b|\b(?:он) (?:готов)\b|\b(?:она) (?:готова)\b|\b(?:(мы|вы|они)) готовы\b'

# 51. Найдите трёхзначные номера, перед которыми идёт №, Номер, или Number.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Состоит из 3 арабских цифр
#     Слева от последовательности стоит №, Номер, или Number

regex = r'(?:(?<=№ )|(?<=Номер )|(?<=Number ))\d{3}'

# 52. Напишите любое регулярное выражение, которое находит само себя полным совпадением.

regex = r'Correct!'

# 53. Напишите регулярное выражение, которое найдёт все слова «Ты» или «ты». Другие формы слова «ты», такие как «твой» и т.д. учитывать не следует.

regex = r'\bТы\b|\bты\b'

# 54. Цвета в формате HEX - способ представления rgb-цветов в шестнадцатеричной системе счисления. Они состоят из 6 шестнадцатиричных чисел, 
#     каждая пара отвечает за свой цвет:
#     Две первые цифры — красный
#     Две в середине — зелёный
#     Две последние цифры — синий
#     Напишите регулярное выражение, которое будет находить валидные hex-цвета.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     В начале стоит #
#     Потом идёт последовательность из 6 шестнадцатеричных цифр верхнего и нижнего регистров: 0123456789abcdefABCDEF
#     Последовательность не может быть подпоследовательностью

regex = r'\#[0123456789abcdefABCDEF]{6}'

# 55. Напишите регулярное выражение, которое найдёт все числа x, где:
#     x ∈ [0, 1] т.е. 0 ≤ x ≤ 1
#     x может быть как и десятичной дробью, так и целым числом
#     Если x - десятичная дробь, то её максимальная точность должна быть до сотых
#     В тестах не будет 0.00/0.0 или 1.00/1.0. Эти числа будут записаны без плавающей точки

regex = r'\b((?<!\.)[01])(?!\.)\b|\b0\.\d{1,2}\b'

# 56. Напишите регулярное выражение, которое найдёт все слова, содержащие в себе букву а.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Используются буквы кириллического алфавита нижнего и верхнего регистров
#     Последовательность должна содержать как минимум одну букву а
#     Заглавную А искать не нужно
#     Последовательность не может быть подпоследовательностью

regex = r'[А-Яа-яЁё]+а[А-Яа-яЁё]+|а[А-Яа-яЁё]+|[А-Яа-яЁё]+а|\bа\b'

# 57. Напишите регулярное выражение, которое найдёт слова, после которых следующим символом идёт один из следующих знаков препинания: .,:?!;
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Состоит из букв кириллического алфавита нижнего и верхнего регистра
#     После последовательности стоит один из знаков препинания: .,:?!;

regex = r'[А-Яа-яЁё]+(?=[\.,:?!;])'

# 58. Очень часто студенты в своих проектах, исследованиях, диссертациях, курсовых и дипломных работах заменяют символы кириллицы на другие, 
#     похожие на символы русского алфавита, пытаясь спрятать следы использованных источников.
#     Помогите написать регулярное выражение, которое находит все:
#     Слова, состоящие из кириллических символов, но в них есть как минимум 1 некириллический символ
#     Слова, состоящие из некириллических символов, но в них есть как минимум 1 кириллический символ
#     Последовательности, состоящие полностью из кириллических или некириллических символов нужно игнорировать
#     Используются буквы верхнего и нижнего регистров
#     Знаки препинания не считаются некириллическими символами
#     Не может являться подпоследовательностью

regex = r'\w*[^A-Zа-яА-Я\s]+\w*\b'

# 59. Напишите регулярное выражение, которое найдёт первое слово в тексте.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Используются буквы кириллического алфавита верхнего и нижнего регистров
#     В последовательности может содержаться дефис
#     Последовательность стоит в начале строки, если её нет - первого слова нет

regex = r'\b\A[Ё-ё][^a-zA-Z\s]*\b'

# 60. Найдите все слова, которые начинаются на n или N.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Состоит из букв латинского алфавита нижнего и верхнего регистров, -
#     Начинается на n или N
#     Не может быть подпоследовательностью

regex = r'(?<!\S)[nN]-?[a-z]+\b'

# 61. Напишите регулярное выражение, которое найдёт все переменные, записанные в стиле lowerCamelCase.
#     Нужно найти переменные, записаные в стиле lowerCamelCase, который включает в себя следующее:
#     Первое слово начинается всегда с буквы нижнего регистра
#     Последующие слова начинаются с букв в верхнем регистре
#     Больше верхний регистр нигде не используется
#     Используются буквы латинского алфавита
#     Цифры в переменных из тестовых данных находятся только в конце

regex = r'\b[a-z]+([A-Z][a-z]+)*\d*\b'

# 62. Напишите регулярное выражение, которое найдёт все переменные, записанные в стиле snake_case.
#     Как вы уже поняли - snake_case это тоже стиль наименования переменных. В Python переменные принято называть, используя этот стиль. 
#     Вот что он из себя представляет:
#     Всегда используется нижний регистр
#     Слова разделяются нижним подчёркиванием
#     Используются буквы латинского алфавита
#     Цифры в переменных из тестовых данных находятся только в конце.

regex = r'\b[a-z]+[_a-z]*\d*\b'

# 63. У Дурова отжали ВКонтакте, но он не сдался и создал уже не социальную сеть, а мессенджер - Телеграм. 
#     Вы наверное знаете, что в Телеграме любой пользователь может выбрать себе username, чтобы его было легче искать. 
#     Давайте поможем Паше и напишем регулярное выражение, которое будет проверять валидность username.
#     Что нужно найти:
#     Используются символы a-z, A-Z, 0-9, _
#     Длина от 5 до 32 символов включительно
#     Не может начинаться с цифры или _
#     Не может заканчиваться на _

regex = r'(?<!\S)([^0-9_]?[a-zA-Z0-9_]{5,32}[^_]?)(?!\S)'

# 64. Найдите в тексте все названия файлов и их расширения.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Название файла состоит из: букв латинского алфавита верхнего и нижнего регистров, цифр, -
#     Между названием и расширением файла стоит .
#     Расширение файла состоит из букв латинского алфавита верхнего и нижнего регистров, цифр
#     Минимальная длина названия и расширения - один символ
#     Найденная последовательность может являться подпоследовательностью, только если стоит в абсолютном или относительном пути: 
#     C:\Users\test.txt, ../Users/test.txt, т.е. перед ней стоят символы / или \

regex = r'(?:(?<=\\)|(?<=[ /])|(?<=^))[a-zA-Z0-9-]+\.[a-zA-Z0-9]+\b'

# 65. Получите все идентификаторы видеороликов на YouTube, используя регулярные выражения.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Cостоит из символов латинского алфавита обоих регистров, цифр, а также _
#     Перед последовательностью стоит v=

regex = r'(?<=v=)[A-Za-z0-9_]+'

# 66. Найдите все валидные пустые массивы, или массивы с числами. Числом считаем произвольную последовательность из цифр.
#     Нужно найти последовательности, подходящие по следующим условиям:
#     Начинается с [ и заканчиваются на ]
#     Внутри может быть пусто, а могут находиться числа
#     Числом считаем произвольную последовательность из цифр
#     Между числами должны стоять запятые
#     Запятые могут быть как и с пробелом, так и без
#     После последнего числа может стоять запятая, т.к. такие массивы: [123, 123, ] и [23, ] валидные в Python

regex = '\[(\d+(,|, )*)*\]'

# 67. Исправьте регулярное выражение, не используя атомарную группировку и притяжательные квантификаторы, чтобы у него не было Catastrophic Backtracking.
#     regex = r'(?:a+)+b'

regex = r'a+b'

# 68. Исправьте следующее регулярное выражение с помощью атомарной группировки или притяжательных квантификаторов, чтобы у него не было Catastrophic Backtracking:
#     regex = r'(?:a+)+b'

regex = r'(?>a+)+b'