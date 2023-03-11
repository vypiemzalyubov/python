# 8 kyu
# Reversed Strings
# 
# Complete the solution so that it reverses the string passed into it.
# 
# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

def solution(string):
    return string[::-1]



# Best Practices

def solution(string):
    temp = list(string)
    temp.reverse()
    return ''.join(temp)

def solution(string):
    return ''.join(i for i in reversed(string))

def solution(string):
    s1=''
    for x in string:
        s1= x+s1
    return s1