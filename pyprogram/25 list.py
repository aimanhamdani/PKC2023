# list
# 1.Mutable
# 2.denotes as []
# 3. It works on Multiple valve
#list and how to slicing
l=[10.1,20,30,40,'Hello']
print(l[2]) #single argument
print(l[0],l[3]) #print only index 0&3
print(l[0:2]) #print 0&1range
print(l[2::2])#Multiple argument
print(l[3:])
print('-------------------------------*')
#In reversal case
u=len(l)
print(u)
print('')
print(l[-1::-1])
#or
print(l[-2::-2])
print('---------------------------***')
w=[10,20,30,40,50,100,[60,90,'hello']]
print('w = ',w)
t=len(w)
print(t,type(w))
print(w[1::2])
print('')
print(w[2],w[6][0])  #if i want to print nested list
print(w[-1][-2])
#items
print('-----------/*')
print(w[-1][-3],w[0],w[-2],l[0])
print(w[-1][-3],w[0],w[-2],w[4],w[0],w[5],w[6][-2],w[-6])
# 60,10,100,50,10.1,100,90,60,90,20