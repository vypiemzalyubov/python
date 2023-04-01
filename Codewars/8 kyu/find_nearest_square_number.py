# 8 kyu
# Find Nearest square number
# 
# Your task is to find the nearest square number, nearest_sq(n) or nearestSq(n), of a positive integer n.
# For example, if n = 111, then nearest\_sq(n) (nearestSq(n)) equals 121, since 111 is closer to 121, the square of 11, than 100, the square of 10.
# If the n is already the perfect square (e.g. n = 144, n = 81, etc.), you need to just return n.

def nearest_sq(n):
    return round(n ** 0.5) ** 2



# Best Practices

from math import sqrt

def nearest_sq(n):
    return pow(round(sqrt(n)), 2)