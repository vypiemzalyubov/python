# 8 kyu
# Even or Odd
# 
# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    return 'Odd' if number % 2 else 'Even'



# Best Practices

def even_or_odd(number):
  return ["Even", "Odd"][number % 2]

even_or_odd = lambda number: "Odd" if number % 2 else "Even"