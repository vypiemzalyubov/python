# 5 kyu
# Convert PascalCase string into snake_case
# 
# Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation. Lowercase characters can be numbers. 
# If the method gets a number as input, it should return a string.
# 
# Examples
# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7Test"        -->  "app7_test"
# 1                 -->  "1"

def to_underscore(string):
    s = ''
    if isinstance(string, str):
        for c in range(len(string)):
            if string[c].isupper() and c == 0:
                s += string[c].lower()
            elif string[c].isupper():
                s += '_' + string[c].lower()
            else:
                s += string[c]
    else:
        s += str(string)
    return s



# Best Practices

def to_underscore(string):
    string = str(string)
    camel_case = string[0].lower()
    for c in string[1:]:
        camel_case += '_{}'.format(c.lower()) if c.isupper() else c
    return camel_case