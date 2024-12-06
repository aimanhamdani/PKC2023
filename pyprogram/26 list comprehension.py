#elegent way to create list
#smart work
l=[]
for a in range(1,101):
    l.append(a)
print(l)
print("from list -1=",l[-1])
print(l[-2:-101:-3])
print('---------------------------**/')
l1=[z for z in range(1,50) if z%2!=0]
print('l1=',l1)
l2=[z for z in range(1,50) if z%2==0]
print('l2=',l2)
l3=[k for k in range(1,40) if k%2==0]
print('l3',l3) #[2,4,6,...,38,100,101,102,...,119]
for n in range(100,120):
    l3.append(n)
print('appended l3 and n',l3)
print(len(l3))
print(l3[-1::-1])
print(l3[-1:-12:-1])
print('-----------------*******')
print(l1<l2)
print(sum(l1))
print(sum(l2))
print(sum(l1)>sum(l2))
print(sum(l3))
#
n=[h for h in range(1,101) if h%2==0] #expansion
print(n)
m=[h for h in range(1,13)   if  h%3==0]
print(m)
print('-----------------------*/*/*/')
s='hello'
s=[g for g in s]
print(s)
print(s[1])
print('-------')
j="a quick brown fox jumps over the lazy dog"
print(j[2] )
print(j)
print('------')
j=[k for k in j]
print(j)
print(j[0],j[2])

g='gold'
k=[p for p in g]
print(k)

l = []  # Initialize an empty list

for a in range(0, 10,2):
    l.append(a)  # Append each value to the list

print(l)  # Print the list after the loop completes
squares=[2**x for x in range(64)]
print('squares',squares[-1])
