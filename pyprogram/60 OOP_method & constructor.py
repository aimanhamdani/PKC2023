# #method
# class DemoClass:
#     a=10
#     b=20
#     def showvalue(self):     #method2
#         # print(a)  #no value show, because 'a' is not define
#         self.c=self.a*self.b
#         print(DemoClass.a)
#         print(self.c)
#         print(self.a)
#         print('hi')
#         print(DemoClass.b)
# demoobj=DemoClass()
# demoobj.showvalue()
# #
# print('-'*10)
# class DemoClass():
#     def showvalue1(self):     #mehod3 #print 'Welcome to WScubetech'
#         print("Welcome to WScubetech")
# # demoobj=DemoClass()
# # demoobj.showvalue1()
#     def showvalue2(self,a,b):
#         print(a+b)
# x=10
# y=20
# demoobj=DemoClass()
# demoobj.showvalue2(x,y)
# demoobj.showvalue1()
# demoobj.showvalue2(20,y)
# print(f'--------constructor started-------')
# # # #Constructors
# class DemoClass1:
#     def __init__(self):
#         print("Welcom to WScubetech")
# DemoClass1()

# print('-'*10)
# class Student:
#     def __init__(self):
#         print('I am the student')
# obj=Student()
# Student()
# print('-'*20)
# #,
# class demoClass:
#     k=10
#     l=20
#     def showValue3(self):
#         self.m=self.k*self.l
#         print(self.m)
# demoobj=demoClass()
# demoobj.showValue3()

# class demoClass:
#     k=10
#     l=20
#     def __init__(self):
#         self.m=self.k*self.l
#         print(self.m)
# obj=demoClass
# #
# class demoClass:
#     def __init__(self):
#         print("Pakistan is best choice")
# demoobj=demoClass()
# demoClass()
class Person:
    def __init__(self, name, age,school):
        self.name = name
        self.age = age
        self.school=school

    def greet(self):
        print("Hello, my name is", self.name)
        print("My age is", self.age)
    def common(self):
        print("school name is",self.school)
Person1=Person("Aiman",39,1)
Person2=Person("Saqi",35,'another school')
Comm=Person(1,2,"Sir Syed Public School Talagang")
Person1.greet()
Person2.greet()
Comm.common()

# class Person:
#     Common_School = "Sir Syed Public School Talagang"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         print("Hello, my name is", self.name)
#         print("My age is", self.age)
#
#     def abc(self):
#         print("The school name is", self.Common_School)
#
# Person1 = Person("Aiman", 39)
# Person2 = Person("Saqi", 35)
# Person1.greet()
# Person2.greet()
#
# # Calling the abc method on an instance
# Person3.abc()

# Person3=Person(0,0)
# class Python:
#     a=11
#     b=20000
#     def fee(self):
#         print(self.a)
#         print(f'fees for python basic course is {self.b}')
#         print('I am studying python')
#         c=5
#         c=self.a*self.b*c
#         print(c)
# obj=Python()
# obj.fee()

# class Python:
#     a=11
#     b=20000
#     def __init__(self):
#         print(self.a)
#         print(f'fees for python basic course is {self.b}')
#         print('I am studying python')
#         c=5
#         c=self.a*self.b*c
#         print(c)
# obj=Python()
# Python()