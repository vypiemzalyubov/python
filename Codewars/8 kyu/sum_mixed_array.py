# 8 kyu
# Sum Mixed Array
# 
# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
# Return your answer as a number.

def sum_mix(arr):
    l = []
    for i in arr:
        l.append(int(i))
    return sum(l) 



# Best Practices

def sum_mix(arr):
    return sum(map(int, arr))

def sum_mix(arr):
    return sum(int(n) for n in arr)