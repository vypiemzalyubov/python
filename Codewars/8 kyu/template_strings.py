# 8 kyu
# Template Strings
# 
# Template Strings, this kata is mainly aimed at the new JS ES6 Update introducing Template Strings
# Task
# Your task is to return the correct string using the Template String Feature.
# Input
# Two Strings, no validation is needed.
# Output
# You must output a string containing the two strings with the word ```' are '```

def temple_strings(obj, feature): 
    return f'{obj} are {feature}'



# Best Practices

def temple_strings(obj, feature):
    return obj + ' ' + 'are' + ' ' +  feature

temple_strings = lambda o, f: f'{o} are {f}'