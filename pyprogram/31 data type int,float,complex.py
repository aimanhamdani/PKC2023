a=5         #integer
print(a,type(a))
a=5.5       #float
print(a,type(a))
a=1+2j      #complex number
print(a,type(a))

print('------')

# Note: Number never comes in single or double quotation.

s="Hello@123"
print(s,type(s))

print('-----')

s='''
Hello
Welcome
to
Wscubetech 123
'''
print(s,type(s))

print('')

s='10'
print(s,type(s))
print('')
print('IMPORTANT')
#List
l=[0,'ws',5.5]
print(l,type(l))
print('')
#how to update a list
l[0]=10 #here 0 is index number of list which update
print(l,type(l))
l[2]=7.6
print(l,type(l))
print('')
t=(10,20,'Hello')   #tuple
print(t,type(t))     #tuple not support any updation
# or changes. and it is immutable

print('----')
t=(20,)
print(t,type(t))
d={
'course_name':'Python','course_duration':'2months'}
print(d,type(d))
print(d['course_duration'],type(d))



#set
s={1,2,3}
print(s,type(s))
s={10,20,30,10}   #set will not repeat value
print(s,type(s))