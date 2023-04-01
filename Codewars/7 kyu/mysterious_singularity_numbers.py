# 7 kyu
# Mysterious Singularity Numbers
# 
# This is a rather simple but interesting kata. Try to solve it using logic. The shortest solution can be fit into one line.
# 
# Task
# The point is that a natural number N (1 <= N <= 10^9) is given. 
# You need to write a function which finds the number of natural numbers not exceeding N and not divided by any of the numbers [2, 3, 5].
# 
# Example
# Let's take the number 5 as an example:
# 
# 1 - doesn't divide integer by 2, 3, and 5
# 2 - divides integer by 2
# 3 - divides integer by 3
# 4 - divides integer by 2
# 5 - divides integer by 5
# Answer: 1
# because only one number doesn't divide integer by any of 2, 3, 5

def real_numbers(n):
    return n - n // 2 - n //3 - n // 5 + n // 6 + n // 10 + n // 15 - n // 30



# Best Practices

def real_numbers(n):
    return n - (n // 2 + n // 3 + n // 5 + n // 30) + (n // 6 + n // 10 + n // 15)

real_numbers = lambda n : n - n//2 - n//3 - n//5 + n//6 + n//10 + n//15 - n//30