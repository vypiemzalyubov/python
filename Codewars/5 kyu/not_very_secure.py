# 5 kyu
# Not very secure
# 
# In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.
# 
# The string has the following conditions to be alphanumeric:
# - At least one character ("" is not valid)
# - Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
# - No whitespaces / underscore

def alphanumeric(password):
    return len(password) == len([c for c in password if c.isdigit() or c.isalpha()]) if password else False



# Best Practices

def alphanumeric(string):
    return string.isalnum()

import re
pattern = re.compile('^[0-9a-zA-Z]+$')
def alphanumeric(string):
    return pattern.match(string) is not None