# Single Inhheritance: #One class to other class
class A:
    def display_A(self):
        print("Welcome to Inheratance A")
class B(A):
    def display_B(self):
        print("Welcome to Inheratance B")
# demoobj=B()
# demoobj.display_A()
# demoobj.display_B()
# print("-"*20)
# print("Multi level Inheritance:")
class C(B):
    def display_C(self):
        print("Welcom to Inheratance C")
demoobj=C()
demoobj.display_A()
demoobj.display_B()
demoobj.display_C()
#
# print("Multiple Inheritance: Class C(A,B):")
# class A:
#     def display_A(self):
#         print("Welcome to Inheratance A")
# class B:
#     def display_B(self):
#         print("Welcome to Inheratance B")
# class C(A,B):
#     def display_C(self):
#         print("Welcome to Inheratance C")
#
# demoobj=C()
# demoobj.display_A()
# demoobj.display_B()
# demoobj.display_C()


