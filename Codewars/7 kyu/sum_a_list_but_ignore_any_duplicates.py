# 7 kyu
# Sum a list but ignore any duplicates
# 
# Please write a function that sums a list, but ignores any duplicate items in the list.
# For instance, for the list [3, 4, 3, 6] , the function should return 10.

def sum_no_duplicates(l):
    res = list(filter(lambda x: l.count(x) < 2, l))
    return sum(res)



# Best Practices

def sum_no_duplicates(l):
    return sum(n for n in set(l) if l.count(n) == 1)

def sum_no_duplicates(l):
    new = []
    for x in l:
        if l.count(x) == 1:
            new.append(x)
    return sum(new)