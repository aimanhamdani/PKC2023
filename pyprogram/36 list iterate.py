l=[10,20,30,40,60,80,90]
t=len(l)
print(t)
#use for loop
for a in range(t):

    print(l[a])
    #direct iterate method2
print('')
print('')
for a in l: #for reverse case, this method would not work.
    print(a)
#reverse
print('')
print('new')
l=[10,20,30,40,60,80,90]
t=len(l)
print(t)
for a in range(t-1,-1,-1):
    print(l[a])
