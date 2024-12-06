# t=(10)
# print(t,type(t)) #output is class int.
# t=(10,) # for tuple class make sure to add comma,
# print(t,type(t),'**********************')
# t=(10,20,30,40,50)
# print(t[3]) #output is 40
# print()
# #how to iterate tuple:
# #method no.1 with use of range.
# l=len(t)
# print(l)
# for a in range(l):
#     print(t[a])
# #method no.2 with use of tuple
# print('+++++++++++++++++++++++++++***************')
# for a in t:
#     print(a)
# print('-'*20)
# print('functions of tuple')
# #TUPLE Min,Max,Count,Index,Sum(sum will work only on integers)
# print('')
# k=(15,30,40,50,55,15,60)
# print(min(k),'min')
# m=min(k)
# print(m)
# m=max(k)
# print(m)
# c=k.count(15)
# print(c)
# i=k.index(15)
# print(i)
# #sum work on one and two arguments
# y=sum(k)    #single argument
# print(y)
# z=sum(k,10) # sum 2 arguments
# print(z)
# print('')
t=(15,40,30,15,45,65,75,50)
print(t,type(t))
print(len(t))
print(t[-1])
print(t.count(5))
t1=tuple(sorted(t))
print(t1,type(t1))
print(sum(t1))
print(t1.index(50))