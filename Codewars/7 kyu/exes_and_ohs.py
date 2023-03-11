# 7 kyu
# Exes and Ohs
# 
# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
# 
# Examples input/output:
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):
    s.lower()
    count1 = 0
    count2 = 0
    for char in s:
        if char == 'x' or char == 'X':
            count1 += 1
        if char == 'o' or char == 'O':
            count2 += 1
    if count1 == count2:
        return True
    elif count1 != count2:
        return False
    else:
        return True
    


# Best Practices

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

def xo(s):
  exes = 0
  ohs = 0
  for c in s.lower():
    if c == 'x':
      exes += 1
    elif c == 'o':
      ohs += 1
  return exes == ohs

def xo(s):
    return True if s.lower().count('x') == s.lower().count('o') else False