# 8 kyu
# Beginner - Reduce but Grow
# 
# Given a non-empty array of integers, return the result of multiplying the values together in order. 
# Example:
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

def grow(arr):
    res = 1
    for i in arr:
        res *= i
    return res 



# Best Practices

from functools import reduce
def grow(arr):
    return reduce(lambda x, y: x * y, arr)


import math
def grow(arr):
    return math.prod(arr)


from functools import reduce
from operator import mul
def grow(arr):
    return reduce(mul, arr, 1)