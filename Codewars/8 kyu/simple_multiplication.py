# 8 kyu
# Simple multiplication
# 
# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9

   
    
# Best Practices

def simple_multiplication(number) :
    return number * 9 if number % 2 else number * 8

def simple_multiplication(n):
    return n * (8 + n%2)