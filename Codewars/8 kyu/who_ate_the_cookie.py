# 8 kyu
# Who ate the cookie?
# 
# For this problem you must create a program that says who ate the last cookie. If the input is a string then "Zach" ate the cookie. 
# If the input is a float or an int then "Monica" ate the cookie. If the input is anything else "the dog" ate the cookie. The way to return the statement is: "Who ate the last cookie? It was (name)!"
# Ex: Input = "hi" --> Output = "Who ate the last cookie? It was Zach! (The reason you return Zach is because the input is a string)
# Note: Make sure you return the correct message with correct spaces and punctuation.
# Please leave feedback for this kata. Cheers!

def cookie(x):
    if isinstance(x, bool):
        return 'Who ate the last cookie? It was the dog!'
    elif isinstance(x, str):
        return 'Who ate the last cookie? It was Zach!'
    elif isinstance(x, float | int):
        return 'Who ate the last cookie? It was Monica!'



# Best Practices

def cookie(x):
    return "Who ate the last cookie? It was %s!" % {str:"Zach", float:"Monica", int:"Monica"}.get(type(x), "the dog")

def cookie(x):
  return f'Who ate the last cookie? It was {"Zach" if type(x) is str else "Monica" if type(x) in [int, float] else "the dog"}!'