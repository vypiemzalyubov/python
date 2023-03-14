# 7 kyu
# Shortest Word
# 
# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

def find_short(s):
    list1 = s.split()
    list1.sort(key=len)
    return len(list1[0])



# Best Practices

def find_short(s):
    return min(len(x) for x in s.split())

def find_short(s):
    return len(min(s.split(' '), key=len))