# 7 kyu
# Dropcaps
# 
# DropCaps means that the first letter of the starting word of the paragraph should be in caps and the remaining lowercase, just like you see in the newspaper.
# But for a change, let"s do that for each and every word of the given String. Your task is to capitalize every word that has length greater than 2, leaving smaller words as they are.
# *should work also on Leading and Trailing Spaces and caps.
# 
# "apple"            => "Apple"
# "apple of banana"  => "Apple of Banana"
# "one   space"      => "One   Space"
# "   space WALK   " => "   Space Walk   " 
# 
# Note: you will be provided atleast one word and should take string as input and return string as output.

def drop_cap(words):
    return ' '.join(c.capitalize() if len(c) > 2 else c for c in words.split(' '))



# Best Practices

import re
def drop_cap(s):
    return re.sub(r'\w{3,}', lambda m: m[0].title(), s)