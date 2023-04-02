# 7 kyu
# Remove consecutive duplicate words
# 
# Your task is to remove all consecutive duplicate words from a string, leaving only first words entries. For example:
# 
# "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"
# --> "alpha beta gamma delta alpha beta gamma delta"
# 
# Words will be separated by a single space. There will be no leading or trailing spaces in the string. An empty string (0 words) is a valid input.

def remove_consecutive_duplicates(s : str) -> str:
    s = s.split(" ")
    lst = [s[0]]
    for i in range(1, len(s)):
        if s[i] != lst[-1]:
            lst.append(s[i])
    return ' '.join(lst) 



# Best Practices

from itertools import groupby
def remove_consecutive_duplicates(s):
    return ' '.join(k for k,_ in groupby(s.split()))

def remove_consecutive_duplicates(s):
    results =[]
    for word in s.split():
        if word not in results:
            results.append(word)
        elif results[-1] != word:
            results.append(word)
    return ' '.join(results)

import re
def remove_consecutive_duplicates(s):
    return re.sub(r"\b(\w+)(\s(\1\b))+", r"\1", s)