# 5 kyu
# Scramblies
# 
# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
# 
# Notes:
# - Only lower case letters will be used (a-z). No punctuation or digits will be included.
# - Performance needs to be considered.
# 
# amples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

def scramble(s1, s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True



# Best Practices

from collections import Counter
def scramble(s1,s2):
    return len(Counter(s2)- Counter(s1)) == 0