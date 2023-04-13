# 7 kyu
# Building blocks
# 
# Write a class Block that creates a block (Duh..)
# 
# Requirements
# The constructor should take an array as an argument, this will contain 3 integers of the form [width, length, height] from which the Block should be created.
# 
# Define these methods:
# `get_width()` return the width of the `Block`
# `get_length()` return the length of the `Block`
# `get_height()` return the height of the `Block`
# `get_volume()` return the volume of the `Block`
# `get_surface_area()` return the surface area of the `Block`
# 
# Examples
# b = Block([2,4,6]) -> create a `Block` object with a width of `2` a length of `4` and a height of `6`
# b.get_width() -> return 2# 
# b.get_length() -> return 4  
# b.get_height() -> return 6  
# b.get_volume() -> return 48  
# b.get_surface_area() -> return 88

class Block:
    
    def __init__(self, lst):
        self.width = lst[0]
        self.length = lst[1]
        self.height = lst[2]

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height
            
    def get_volume(self):
        return self.width * self.length * self.height
    
    def get_surface_area(self):
        return (self.width * self.length + self.width * self.height + self.length * self.height) * 2
    


# Best Practices

class Block(object):
    def __init__(self, wlh):
        self.w, self.l, self.h = w,l,h = wlh
        self.v = w*h*l
        self.a = 2 * (w*l + w*h + l*h)
    
    def get_width(self):        return self.w
    def get_length(self):       return self.l
    def get_height(self):       return self.h
    def get_volume(self):       return self.v
    def get_surface_area(self): return self.a



class Block:
    def __init__(s, dimensions):
        s.W, s.L, s.H = dimensions
    
    get_width  = lambda s: s.W
    get_length = lambda s: s.L
    get_height = lambda s: s.H
    get_volume = lambda s: s.W * s.L * s.H
    get_surface_area = lambda s: (s.W * s.L + s.L * s.H + s.H * s.W) * 2        