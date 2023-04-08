# 7 kyu
# Odd-Even String Sort
# 
# Given a string s. You have to return another string such that even-indexed and odd-indexed characters of s are grouped and groups are space-separated (see sample below)
# 
# Note: 
# 0 is considered to be an even index. 
# All input strings are valid with no spaces
# 
# input: 'CodeWars'
# output 'CdWr oeas'
# 
# S[0] = 'C'
# S[1] = 'o'
# S[2] = 'd'
# S[3] = 'e'
# S[4] = 'W'
# S[5] = 'a'
# S[6] = 'r'
# S[7] = 's'
# Even indices 0, 2, 4, 6, so we have 'CdWr' as the first group
# odd ones are 1, 3, 5, 7, so the second group is 'oeas'
# And the final string to return is 'Cdwr oeas'

def sort_my_string(s):
    l = [char for char in s]
    l1, l2 = [], []
    for i in range(len(l)):
        if i % 2 == 0:
            l1.append(l[i])
        else:
            l2.append(l[i])
    return ''.join(l1) + ' ' + ''.join(l2) 



# Best Practices

def sort_my_string(s):
    return f'{s[::2]} {s[1::2]}'

def sort_my_string(s):
    return s[::2] + ' ' + s[1::2]

def sort_my_string(s):
    odd, even = [], []
    for i, char in enumerate(s):
        even.append(char) if i % 2 == 0 else odd.append(char)
    return "".join(even) + " " + "".join(odd)