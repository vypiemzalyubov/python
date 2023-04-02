# 8 kyu
# Be Concise I - The Ternary Operator
# 
# Be Concise I - The Ternary Operator
# You are given a function describeAge / describe_age that takes a parameter age (which will always be a positive integer) and does the following:
# 
# If the age is 12 or lower, it return "You're a(n) kid"
# If the age is anything between 13 and 17 (inclusive), it return "You're a(n) teenager"
# If the age is anything between 18 and 64 (inclusive), it return "You're a(n) adult"
# If the age is 65 or above, it return "You're a(n) elderly"
# Your task is to shorten the code as much as possible. Note that submitting the given code will not work because there is a character limit of 145.
# 
# I'll give you a few hints:
# 
# The title itself is a hint - if you're not sure what to do, always research any terminology in this description that you have not heard of!
# Don't you think the whole "You're a(n) <insert_something_here>" is very repetitive? ;) Perhaps we can shorten it?
# Write everything in one line, \n and other whitespaces counts.

def describe_age(a):return"You're a(n) "+('kid'if a<13 else'elderly'if a>64 else'adult'if 17<a<65 else'teenager')



# Best Practices

def describe_age(a): 
    return f"You're a(n) {a<13 and 'kid' or a<18 and 'teenager' or a<65 and 'adult' or 'elderly'}"

describe_age=lambda n:"You're a(n) "+"kid teenager adult elderly".split()[(n>12)+(n>17)+(n>64)]