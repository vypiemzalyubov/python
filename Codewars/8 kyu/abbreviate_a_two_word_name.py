# 8 kyu
# Abbreviate a Two Word Name
# 
# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# 
# It should look like this:
# Sam Harris => S.H
# patrick feeney => P.F

def abbrev_name(name):
    return f'{name.split()[0][0].upper()}.{name.split()[1][0].upper()}'



# Best Practices

def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()

def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]