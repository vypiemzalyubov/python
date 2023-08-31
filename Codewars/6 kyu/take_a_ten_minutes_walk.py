# 6 kyu
# Take a Ten Minutes Walk
# 
# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. 
# The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter 
# strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, 
# so create a function that will return true if the walk the app gives you will take you exactly ten minutes 
# (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.
# Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). 
# It will never give you an empty array (that's not a walk, that's standing still!).

def is_valid_walk(walk):
    if len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e'):
        return True
    return False
    


# Best Practices

def isValidWalk(walk):
    my_dict = {'n': 0, 's': 0, 'e': 0, 'w': 0}
    for i in walk:
        my_dict[i] += 1
    if (len(walk) == 10 and my_dict['n'] == my_dict['s'] and my_dict['e'] == my_dict['w']):
        return True
    return False

def is_valid_walk(walk):
    x_distance = 0
    y_distance = 0
    for step in walk:
        if step == 'n':
            y_distance += 1
        elif step == 's':
            y_distance -= 1
        elif step == 'w':
            x_distance -= 1
        elif step == 'e':
            x_distance += 1
    return True if x_distance == 0 and y_distance == 0 and len(walk) == 10 else False