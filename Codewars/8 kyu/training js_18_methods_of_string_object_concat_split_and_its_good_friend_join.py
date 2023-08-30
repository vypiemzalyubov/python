# 8 kyu
# Training JS #18: Methods of String object--concat() split() and its good friend join()
# 
# Task
# Implement a function which accepts 2 arguments: string and separator.
# The expected algorithm: split the string into words by spaces, split each word into separate characters and join them back with the specified separator, 
# join all the resulting "words" back into a sentence with spaces.
# 
# For example:
# splitAndMerge("My name is John", " ")  ==  "M y n a m e i s J o h n"
# splitAndMerge("My name is John", "-")  ==  "M-y n-a-m-e i-s J-o-h-n"
# splitAndMerge("Hello World!", ".")     ==  "H.e.l.l.o W.o.r.l.d.!"
# splitAndMerge("Hello World!", ",")     ==  "H,e,l,l,o W,o,r,l,d,!"

def split_and_merge(string_, separator):
    return ' '.join(separator.join(c) for c in string_.split())



# Best Practices

def split_and_merge(string, sp):
    return ' '.join(map(sp.join, string.split()))