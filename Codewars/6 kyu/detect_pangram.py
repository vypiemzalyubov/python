# 6 kyu
# 
# Detect Pangram
# 
# A pangram is a sentence that contains every single letter of the alphabet at least once. 
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

import string

def is_pangram(s):
    alphabet = list(string.ascii_lowercase)
    res = set()
    for char in s.lower():
        if char in alphabet:
            res.add(char)
    if len(res) == 26:
        return True
    return False



# Best Practices

import string

def is_pangram(s):
    s = s.lower()
    for char in string.ascii_lowercase:
        if char not in s:
            return False
    return True


import string

def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())