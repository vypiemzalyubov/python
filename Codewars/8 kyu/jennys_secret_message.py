# 8 kyu
# Jenny's secret message
# 
# Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. 
# She added a special case to her function, but she made a mistake.
# Can you help her?

def greet(name):
    return 'Hello, my love!' if name == 'Johnny' else f'Hello, {name}!'



# Best Practices

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)