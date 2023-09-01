# 6 kyu
# CamelCase Method
# 
# Write a method (or function, depending on the language) that converts a string to camelCase, that is, all words must have their first letter capitalized and spaces must be removed.
# 
# Examples (input --> output):
# "hello case" --> "HelloCase"
# "camel case word" --> "CamelCaseWord"

def camel_case(s):
    return ''.join(c for c in s.title() if c.isalpha())



# Best Practices

def camel_case(string):
    return string.title().replace(" ", "")