#Overloading:
# class Area:
#     def find_area(self,x=None,y=None):
#         if x!=None and y!=None:
#             print(x*y)
#         elif x!=None:
#             print(x*x)
#         else:
#             print("Nothing")
# obj=Area()
# obj.find_area()
# obj.find_area(10,20)
# obj.find_area(30)
# obj.find_area(300,20)

#METHOD 2 overloading
class AreaMeasurement:
    def __init__(self,x=None,y=None):
        self.axe=x
        self.vay=y
        if x!=None and y!=None:
            print("Rectangel area",self.axe*self.vay)
        elif x!=None:
            print("Area in square:",self.axe*self.axe)
        else:
            print("None value")
obj=AreaMeasurement(20)
obj=AreaMeasurement(20,20)
obj=AreaMeasurement()
#
# #Overriding:
# class A:
#     def showdata(self):
#         print('I m in A Class')
# class B(A):
#     def showdata(self):
#         print('I m in B Class')
# obj=B()
# obj.showdata() #It will override of parenting data and meorize child data. It is good for momory process and reducing the use of memory


class A:
    def displayshow(self):
        print("Value of A")
class B(A):
    def displayshow(self):
        super().displayshow()
        print("Value of B")
class C(B):
    def displayshow(self):
        super().displayshow()

        print("Value of C")
obj=C()
obj.displayshow()

























