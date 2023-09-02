# 5 kyu
# The Hashtag Generator
# 
# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:
# - It must start with a hashtag (#).
# - All words must have their first letter capitalized.
# - If the final result is longer than 140 chars it must return false.
# - If the input or the result is an empty string it must return false.

# Examples
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false

def generate_hashtag(s):
    res = '#'
    for c in s.split():
        res += c.capitalize()       
    return res if 1 < len(res) < 141 else False



# Best Practices

def generate_hashtag(s):
    return '#' + ''.join([word.title() for word in s.split(' ')]) if s and len(s) <= 140 else False