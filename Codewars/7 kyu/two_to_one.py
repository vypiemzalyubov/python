# 7 kyu
# Two to One
# 
# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.
# 
# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"
# 
# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(a1, a2):
    return ''.join(sorted(set(a1 + a2)))



# Best Practices

def longest(s1, s2):
    return ''.join(sorted(set(s1) | set(s2)))

def longest(s1, s2):
    return ''.join(sorted(set(s1).union(s2)))