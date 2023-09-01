# 6 kyu
# Break camelCase
# 
# Complete the solution so that the function will break up camel casing, using a space between words.
# 
# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

def solution(s):
    return ''.join(f' {c}' if c == c.upper() else c for c in s)



# Best Practices

import re
def solution(s):
    return re.sub('([A-Z])', r' \1', s)