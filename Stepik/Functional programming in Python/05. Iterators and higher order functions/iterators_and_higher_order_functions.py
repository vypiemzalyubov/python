# Программе на вход поступают слова, разделенные пробелом. Ваша задача - проверить, во всех ли словах есть английская буква A вне зависимости от регистра. 
# В качестве ответа программа должна вывести True или False.

print(all(['a' in word.lower() for word in input().split()]))

# На вход программе поступает список из целых чисел. Ваша задача - вывести True, если элементы в списке отсортированы строго по убыванию. 
# В противном случае выведите False.

lst = list(map(int, input().split()))
print(all([lst[i] > lst[i+1] for i in range(len(lst)-1)]))

# Кто не помнит со школьных уроков английского эту запоминашку для написания английских слов, таких, как например, bought?
# Вашей программе на вход будут поступать слова, разделенные пробелом. Программа должна вывести True , если встретилось хотя бы одно слово, заканчивающееся на ought. 
# В противном случае нужно вывести False. Регистр букв не имеет значения, значит, интересующиеся нас слова могут заканчиваться как на ought, так и, например, на OUGHT.

print(any([word.endswith('ought') for word in input().lower().split()]))