#implement logics in string function

w='Welcome123'
print(len(w))
print(w.index("e")) #index will work on split. but find will not work.
# find
print(w.find('e')) #first character find and give result
# that where this character is in place.
print(w.find('e',2)) #we can change the starting point
# # like range function
# #1parameter means find , 2parameter meaing start point
# # change
print(w.find('z',2))  #if not find index than give
# result as -1, find will not work on split()
#
# # index
# #index and find is like same function
print(w.index('c',3))

# print(w.index('z'))      # if valve not fond then it gives
# error, but in find it is showing -1.
# isalpha #give answer ture/false
print('-----------------------------++++++++++')
# #means all string is alphabetics
print(w.isalpha())
# # isdigit
w='123'
print(w.isdigit())
# #all string is digit
#
# # isalnum  #only digit and alphabets then true.
# # if @$%etc or space then result gives false
w='welcome@123'
print(w.isalnum())

