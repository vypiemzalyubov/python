# 5 kyu
# Simple Pig Latin
# 
# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
# 
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


def pig_it(text):
    return ' '.join(f'{c[1:]}{c[0]}ay' if c.isalpha() else c for c in text.split())



# Best Practices

import re
def pig_it(text):
    return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.I)