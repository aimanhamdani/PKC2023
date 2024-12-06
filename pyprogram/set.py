s1={2,1,3,4,5}
s2={2,4,6,7,8,9}
print(s1,type(s1))
print(s2,type(s1))
s=s1|s2
print(s)
print('------------------')
l1=list(s1)
print(l1,type(l1))
l2=list(s2)
print(l2,type(l2))
l=l1+l2
print(l,type(l))
print(f'----------------')
s3=set(l)
print(s3,type(s3))
print(f'----------------')
ss={2,1,3,4,7,6,5,5,3}
print(ss,type(ss))
ss1={'A','B','C','D','E','F','A','B','C','D','E','F'}
print(ss1,type(ss1))
ss2=sorted(ss1)
print(ss2)
print(f'--------------------------------------------')
print(f's1= {s1}')
print(f's2= {s2}')
print(s1^s2)


