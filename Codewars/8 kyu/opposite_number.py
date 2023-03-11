# 8 kyu
# Opposite number
# 
# Very simple, given an integer or a floating-point number, find its opposite.
# 
# Examples:
# 1: -1
# 14: -14
# -34: 34

def opposite(number):
    return number * (-1)



# Best Practices

def opposite(number):
    return -number

opposite = lambda x: -x