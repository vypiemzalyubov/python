# 6 kyu
# Highest Scoring Word
# 
# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# For example, the score of abad is 8 (1 + 2 + 1 + 4).
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.

def high(x):
    d = {}
    for c in x.split():
        for s in c:
            d.setdefault(c, []).append(ord(s) - 96)
    for k, v in sorted(d.items(), key=lambda d: sum(d[1]), reverse=True):
        return k
    


# Best Practices

def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))