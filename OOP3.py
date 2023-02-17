
from dateutil.parser import parse

class Person:
    def __init__(self,name,sex,birth): #Constructor definition
        self._name = name #Attributes...
        self._sex = sex #Man or Woman
        self._birth = parse(birth).date() #Parse it only with date, no time as by default.
    
    def getName(self):
        print("getName called..")
        return self._name
    
    def getBdate(self):
        print("getBdate called..")
        return self._birth
    
    def __isMan__(self):
        if self.sex == 'M':
            return True
        return False
    
    
    def __isWoman__(self):
        if self.sex == 'F':
            return True
        return False
    

person = Person('John','M','24/10/1973')

#We verify that they are really private! Output is AttributeError
print(person.name)
print(person.sex)
print(person.birth)

#Here we can access them!
print(person._name)
print(person._sex)
print(person._birth)
