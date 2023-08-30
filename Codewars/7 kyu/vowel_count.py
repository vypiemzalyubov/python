# 7 kyu
# Vowel Count
# 
# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    return sum([1 for c in sentence if c in 'aeiou'])



# Best Practices

def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels + 1
    return num_vowels

import re
def getCount(str):
    return len(re.findall('[aeiou]', str, re.IGNORECASE))