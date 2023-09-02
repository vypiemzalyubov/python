# 5 kyu
# ISBN-10 Validation
# 
# ISBN-10 identifiers are ten digits long. The first nine characters are digits 0-9. The last digit can be 0-9 or X, to indicate a value of 10.
# An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero.
# 
# For example:
# ISBN     : 1 1 1 2 2 2 3 3 3  9
# position : 1 2 3 4 5 6 7 8 9 10
# 
# This is a valid ISBN, because:
# (1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0
# 
# Examples
# 1112223339   -->  true
# 111222333    -->  false
# 1112223339X  -->  false
# 1234554321   -->  true
# 1234512345   -->  false
# 048665088X   -->  true
# X123456788   -->  false

def valid_ISBN10(isbn):
    if len(isbn) < 10:
        return False
    tmp = []
    for i in range(len(isbn)):
        if isbn[i].isdigit():
            tmp.append((i + 1) * int(isbn[i]))
        elif isbn[i] == 'X' and i == 9:
            tmp.append(100)
    return sum(tmp) % 11 == 0 if len(tmp) == 10 else False



# Best Practices

def valid_ISBN10(isbn):
    if len(isbn) != 10 or not (isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X')):
        return False
    return sum(i*(10 if x=='X' else int(x)) for i,x in enumerate(isbn, 1)) % 11 == 0