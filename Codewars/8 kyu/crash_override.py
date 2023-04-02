# 8 kyu
# Crash Override
# 
# Every budding hacker needs an alias! The Phantom Phreak, Acid Burn, Zero Cool and Crash Override are some notable examples from the film Hackers.
# Your task is to create a function that, given a proper first and last name, will return the correct alias.
# 
# Notes:
# Two objects that return a one word name in response to the first letter of the first name and one for the first letter of the surname are already given. 
# See the examples below for further details.
# If the first character of either of the names given to the function is not a letter from A - Z, you should return "Your name must start with a letter from A - Z."
# Sometimes people might forget to capitalize the first letter of their name so your function should accommodate for these grammatical errors.
# 
# Examples
# # These two dictionaries are preloaded, you need to use them in your code
# FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', ...}
# SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst' ...}
# 
# alias_gen('Larry', 'Brentwood') == 'Logic Bomb'
# alias_gen('123abc', 'Petrovic') == 'Your name must start with a letter from A - Z.'

FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', '...':'...'}
SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst', '...':'...'}

def alias_gen(f_name, l_name):
    if f_name[0].isalpha() and l_name[0].isalpha():
        return f'{FIRST_NAME.get(f_name[0].title())} {SURNAME.get(l_name[0].title())}'
    return "Your name must start with a letter from A - Z."



# Best Practices

def alias_gen(f_name: str, l_name: str) -> str:
    try:
        return f"{FIRST_NAME[f_name[0].upper()]} {SURNAME[l_name[0].upper()]}"
    except KeyError:
        return "Your name must start with a letter from A - Z."

alias_gen = lambda f,l:f[0].isalpha()and l[0].isalpha()and'%s %s'%(FIRST_NAME[f[0].upper()],SURNAME[l[0].upper()])or 'Your name must start with a letter from A - Z.'

