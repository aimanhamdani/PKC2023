# #DEL,POP,REMOVE,CLEAR,UPDATE,INSERT,APPEND,EXTEND
#
l=[20,30,50,60]
#
# del l[1] #delete number, put index value.
# print(l)
# print('')
#
# l=[20,30,50,60]
# print(l.pop(2)) #will show both values, deleted and updated list
# print(l)
# print('')
#
# l=[20,30,50,60]
# l.remove(60) #remove work on value only
# print(l)
# print('')
# l=[20,30,50,60]
# l.clear() #all list will clear
# print(l)
# print('')
# l=[20,30,50,60]
# l[0]=100 #update element inside of list
# print(l)
# print('')
# #insert we can set value inplace
l=[20,30,50,60]
l.insert(0,10) #0 position inser 10 extra in list.
print(l)
# print('')
#append any data can append or add only in the last
l=[20,30,50,60]
print(l)
l.append(70) #when add value, it will add inside the same list. not create a seprate list
print(l)
n=[50,50]
l.append(n) #inside value but in seprate/2nd list will append
print('along appended list',l)
#extend, work inside the value and put in one list set
l=[20,30,50,60]
n=[50,60]
l.extend(n) # it will update inside the same value list.
print(l)
l1=['orange','banana','tomato']
print(l1)
l1[0]='grapes'
print(l1)
l1.append('guava')
print(l1)
l2=['strawberry','water melon']
print(l2)
l1.append(l2)
print(l1)
l3=['kerala','bhindi']
print(l3)
l1.extend(l3)
print(l1)
