# 8 kyu
# Welcome to the City
# 
# Create a method that takes as input a name, city, and state to welcome a person. 
# Note that name will be an array consisting of one or more values that should be joined together with one space between each, and the length of the name array in test cases will vary.
# 
# Example:
# ['John', 'Smith'], 'Phoenix', 'Arizona'
# This example will return the string Hello, John Smith! Welcome to Phoenix, Arizona!

def say_hello(name, city, state):
    return f"Hello, {' '.join(str(c) for c in name)}! Welcome to {city}, {state}!"



# Best Practices

def say_hello(name, city, state):
  return "Hello, {}! Welcome to {}, {}!".format(" ".join(name), city, state)

def say_hello(name, city, state):
    return f"Hello, {' '.join(name)}! Welcome to {city}, {state}!"