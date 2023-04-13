# 7 kyu
# Person Class Bug
# 
# The following code was thought to be working properly, however when the code tries to access the age of the person instance it fails.
# 
# person = Person('Yukihiro', 'Matsumoto', 47)
# print(person.full_name)
# print(person.age)
# 
# For this exercise you need to fix the code so that it works correctly.
# Note: the order of the person's full name is first name and last name.

class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = f'{self.first_name} {self.last_name}'



# Best Practices

class Person:
    __init__ = lambda s,f,l,a: (setattr(s,'full_name',f'{f} {l}'),setattr(s,'age',a),None)[2]

    

class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    


class Person():
  
    def __init__(self, first_name, last_name, age):
        self.full_name = first_name + " " + last_name
        self.age = age