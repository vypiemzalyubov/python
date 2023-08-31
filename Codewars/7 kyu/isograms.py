# 7 kyu
# Isograms
# 
# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. 
# Assume the empty string is an isogram. Ignore letter case.
# 
# Example: (Input --> Output)
# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)
# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false

def is_isogram(string):
    return len(string.lower()) == len(set(string.lower()))



# Best Practices

def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True