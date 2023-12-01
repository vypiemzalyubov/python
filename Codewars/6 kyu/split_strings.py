# 6 kyu
# Split Strings
# 
# Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
# 
# Examples:
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']

def solution(s):
    res = __import__("re").findall("[a-z]{1,2}", fr"{s}")
    return [w if len(w) == 2 else f"{w}_" for w in res]



# Best Practices

import re

def solution(s):
    return re.findall(".{2}", s + "_")


def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result