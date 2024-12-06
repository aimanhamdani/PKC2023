l=[10,20,40,50,60]
l1=[3,4,88,77,78,80,100]
#for loop logic using zip
for a,b in zip(l1,l):
    print(a,b)
print('----------------****')
#without zip function:-
t=len(l)
print(t)
for h in range(t):
    print(h)
    print(l1[h],l[h])
#

# list_1=['a','b','c','d','e','f']
# list_2=[1,2,3,4,5,6]
# print(list_1)
# print(list_2)
# for a,b in zip(list_1,list_2):
#     print(a,b)
# print('-----------------------')
#
# t=len(list_2)
# print(t)
# for h in range(t):
#     print(list_2[h],list_1[h])
