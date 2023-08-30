# 8 kyu
# Find the position!
# 
# When provided with a letter, return its position in the alphabet.
# Input :: "a"
# Ouput :: "Position of alphabet: 1"

def position(alphabet):
    return f'Position of alphabet: {ord(alphabet) - 96}'



# Best Practices

from string import ascii_lowercase
def position(char):
    return "Position of alphabet: {0}".format(ascii_lowercase.index(char) + 1)