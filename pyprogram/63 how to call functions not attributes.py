#if you want to give limited access. He could call the function but he couldnot call all its attributes \n
# then use
# private variables.
# class Student:
#     __name="Ravi"
#     def __init__(self):
#         print(self.__name)
#         self.__displayinfo()
#     def __displayinfo(self):
#         print("Welcome to WScubetech")
# obj=Student()

class Student:
    k=20
    a=f'a quick brown fox jumps over the lazy dog {k}'
    __name=f'Aiman Aali {a}'
    def __init__(self):
        print(self.__name)
        self.__displayname()
    def __displayname(self):
        print("Welcome to wscubetech")

obj=Student()


# class School:
#     __name='sir syed'
#     def __init__(self):
#         print(self.__name)
#         self.__name1()
#         self.__name2()
#     def __name1(self):
#         print('Other school')

#     def __name2(self):
#         print(f'school2 {self.__name}')
#     def __name3(self):
#         pass
# obj=School()
















