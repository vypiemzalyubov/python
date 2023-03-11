# 8 kyu
# Are You Playing Banjo?
# 
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
# 
# The function takes a name as its only argument, and returns one of the following strings:
# name + " plays banjo" 
# name + " does not play banjo"
# 
# Names given are always valid strings.

def are_you_playing_banjo(name):
    if name[0] == 'R' or name[0] == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    


# Best Practices

def areYouPlayingBanjo(name):
   return name + " plays banjo" if name[0].lower() == 'r' else name + " does not play banjo"

def areYouPlayingBanjo(name):
    if name.startswith('R') or name.startswith('r'):
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'