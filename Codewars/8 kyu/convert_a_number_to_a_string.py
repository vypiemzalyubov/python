# 8 kyu
# Convert a Number to a String!
# 
# We need a function that can transform a number (integer) into a string.
# 
# What ways of achieving this do you know?
# 
# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"

def number_to_string(num):
    return str(num)



# Best Practices

def number_to_string(num):
    try:
        return str(num)
    except:
        return None

def number_to_string(num):
    return "{}".format(num)