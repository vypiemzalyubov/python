# 7 kyu
# Divide and Conquer
# 
# Given a mixed array of number and string representations of integers, add up the non-string integers and subtract the total of the string integers.
# Return as a number.

def div_con(x):
    result = 0
    for i in x:
        if isinstance(i, int):
            result += i
        if isinstance(i, str):
            result -= int(i)
    return result



# Best Practices

def div_con(x):
    return sum([a for a in x if isinstance(a, int)]) - sum([int(a) for a in x if not isinstance(a, int)])