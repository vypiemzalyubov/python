# 8 kyu
# Convert a Boolean to a String
# 
# Implement a function which convert the given boolean value into its string representation.
# Note: Only valid inputs will be given.

def boolean_to_string(b):
    return str(True) if b == True else str(False)



# Best Practices

def boolean_to_string(b):
    return str(b)

def boolean_to_string(b):
    return 'True' if b else 'False'