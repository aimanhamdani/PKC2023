# def showdate(a):
#     print(a)
#
# #calling
# a='hamdani'
# showdate('hi')
# print(a)
#
# print('*******')
# #function argument
# def sum(a,b):
#     print(a+b)
#     #calling
# sum(10,20)
# def mul(a,b):
#     print(a*b)
# mul(10,20)
# print('DEFAULT PARAMETER')
# #Default parameter value
# def sum(a,b=10):
#     print(a+b)
# sum(5,4)
# print('')
# sum(10)
# sum(20,1)
# #RETURN VALUE:
# def square(x):
#     return x*x,x**2
# s=square(5)
# print('square',s)
# #OR
# print('square',square(5))
# # print('')
# def cube(x):
#     return x**3
# c=cube(5)
# print(c)
# print('*************************++++++++++++++++++++++-------------------')
# def dmas(x,y):
#     d=x/y
#     m=x*y
#     a=x+y
#     s=x-y
#     return d,m,a,s
# x=int(input('enter the value x = '))
# y=int(input('enter the value y= '))
# d,m,a,s=dmas(x,y)
# a=a+10
# print(a)

# def table(x):
#     for a in range(1,11):
#         print(x,'x',a, '=' ,x*a)
#
# x=2
# tab=table(x)
#
# def table(x):
#     result=[]
#     for a in range(1,11):
#         result.append(f"{x},x {a} = {x*a}".upper())
#
#     return result
#
# x=2
# tab=table(x)
# print(tab)
# for row in tab:
#     print(row)
def table(x):
    result=[]
    for a in range(1,11):
        result.append(f"{x} x {a} = {x*a}".upper())
    return result
n=int(input('enter the table ='))
tab=table(n)
print(tab)
for i in tab:
    print(i)
# for row in tab:
#     print(row)