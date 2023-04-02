# 7 kyu
# MinMaxMin: Bounded Nums
# 
# Given an unsorted array of integers, find the smallest number in the array, the largest number in the array, 
# and the smallest number between the two array bounds that is not in the array.
# 
# For instance, given the array [-1, 4, 5, -23, 24], the smallest number is -23, the largest number is 24, and the smallest number between the array bounds is -22. 
# You may assume the input is well-formed.
# 
# You solution should return an array [smallest, minimumAbsent, largest]
# The smallest integer should be the integer from the array with the lowest value.
# The largest integer should be the integer from the array with the highest value.
# The minimumAbsent is the smallest number between the largest and the smallest number that is not in the array.
# 
# minMinMax([-1, 4, 5, -23, 24]); //[-23, -22, 24]
# minMinMax([1, 3, -3, -2, 8, -1]); //[-3, 0, 8]
# minMinMax([2, -4, 8, -5, 9, 7]); //[-5, -3,9]

def min_min_max(arr):
    x = sorted(arr)
    l = [x[0], None, x[-1]]
    num = x[0] + 1
    while num in x[1:-1]:
        num += 1
    return [x[0], num, x[-1]]  



# Best Practices

def minMinMax(arr):
    return [min(arr), min([x for x in range(min(arr), max(arr)) if x not in arr ]), max(arr)]

def minMinMax(arr):
    for i in range(min(arr),max(arr)):
        if i not in arr: 
            return [min(arr),i,max(arr)]