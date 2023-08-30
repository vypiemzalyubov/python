# 7 kyu
# Descending Order
# 
# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. 
# Essentially, rearrange the digits to create the highest possible number.
# 
# Examples:
# Input: 42145 Output: 54421
# Input: 145263 Output: 654321
# Input: 123456789 Output: 987654321

def descending_order(num):
    tmp = []
    while num:
        tmp.append(str(num % 10))
        num //= 10
    if tmp:
        return int(''.join(sorted(tmp, reverse=True)))
    return 0



# Best Practices

def Descending_Order(num):
    return int(''.join(sorted(str(num), reverse=True)))