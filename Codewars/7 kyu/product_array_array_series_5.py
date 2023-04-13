# 7 kyu
# Product Array (Array Series #5)
# 
# Task
# Given an array/list [] of integers , Construct a product array Of same size Such That prod[i] is equal to The Product of all the elements of Arr[] except Arr[i].
# 
# Notes
# Array/list size is at least 2 .
# Array/list's numbers Will be only Positives
# Repetition of numbers in the array/list could occur.
# 
# Input >> Output Examples
# productArray ({12,20}) ==>  return {20,12}
# 
# Explanation:
# The first element in prod [] array 20 is the product of all array's elements except the first element
# The second element 12 is the product of all array's elements except the second element .

def product_array(numbers):
    res = 1
    for element in numbers:
        res *= element
    return [res / element for element in numbers]



# Best Practices

from operator import mul
from functools import reduce

def product_array(numbers):
    tot = reduce(mul,numbers)
    return [tot//n for n in numbers]



def product_array(numbers):
    prod = eval("*".join(map(str, numbers)))
    return [ prod / x for x in numbers ]