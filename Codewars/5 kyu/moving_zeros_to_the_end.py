# 5 kyu
# Moving Zeros To The End
# 
# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            if lst[j] == 0:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst



# Best Practices

def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i != 0]
    return l + [0] * (len(arr) - len(l))

def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)


def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i)
            array.append(i)
    return array

def move_zeros(a):
    a.sort(key=lambda v: v == 0)
    return a