#Getter & Setter:
class Student:
    def __init__(self):
        self.__name=""
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name
obj=Student()
obj.setname("Testing")
name1=obj.getname()
print(name1)
#OR
print(obj.getname())

