# 7 kyu
# Valid Parentheses
# 
# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. 
# The function should return true if the string is valid, and false if it's invalid.
# 
# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# 
# Constraints
# 0 <= length of input <= 100
# 
# All inputs will be strings, consisting only of characters ( and ).
# Empty strings are considered balanced (and therefore valid), and will be tested.
# For languages with mutable strings, the inputs should not be mutated.

def valid_parentheses(paren_str):
    while '()' in paren_str:
        paren_str = paren_str.replace('()', '')
    return True if paren_str == '' else False  



# Best Practices

def valid_parentheses(array):
    count = 0
    for item in array:
        if item == '(':
            count += 1
        elif count:
            count -= 1
        else:
            return False
    return count == 0

def valid_parentheses(s):
    while '()' in s: s = s.replace('()', '')
    return len(s) == 0