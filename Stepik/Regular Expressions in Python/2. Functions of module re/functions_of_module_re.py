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