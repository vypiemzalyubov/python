# 6 kyu
# Bit Counting
# 
# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def count_bits(n):
    return bin(n).count('1')



# Best Practices

def countBits(n):
    count = 0
    while n:
        if n % 2 == 0:
            n = n / 2
        else:
            count += 1
            n = n - 1
    return count