# 7 kyu
# Double value every next call
# 
# This kata is about static method that should return different values.
# On the first call it must be 1, on the second and others - it must be a double from previous value.

class Class:
    
    counter = 0
    
    @staticmethod
    def get_number():
        res = 2 ** Class.counter
        Class.counter += 1
        return res
    


# Best Practices

class Class:
    value=1
    def get_number():
        result=Class.value
        Class.value*=2
        return result



from itertools import count
class Class: get_number = map(2 .__pow__, count()).__next__