# 69. В переменной match записан объект Match. Выведите на экран:
#     Его нулевую группу
#     Начало вхождения нулевой группы
#     Конец вхождения нулевой группы
#     Атрибут pos
#     Атрибут endpos
#     Атрибут re
#     Атрибут string

import re

match = re.match(input(), input())
print(match.group(0))
print(match.start(0))
print(match.end(0))
print(match.pos)
print(match.endpos)
print(match.re)
print(match.string)

# 70. Многие функции возвращают None в результате своей работы, если ничего не было найдено.
#     Попробуйте вывести нулевую группу в Match-объекте, если совпадение было найдено. Если его нет - ничего не выводите.

import re

match = re.match(input(), input())
if match:
    print(match[0])