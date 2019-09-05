from enum import Enum

class student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age


s1 = student("Mike",18)
print(s1.name)



class teacher(object):
    def __init__(self,name):
        self.__name = name

    def get_name(self):
        print(self.__name)

s2 = teacher("Siri")
s2.get_name()

print(type('123'))
print(isinstance(s2,teacher))
print(dir(s2))

Month = Enum('Month',('Ja','Fe'))