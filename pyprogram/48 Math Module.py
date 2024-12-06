#Math Module is built in module
#functions like #math.ceil(),math.fabs(),math.factorial(),
# math.floor(),math.fsum(),math.sqrt()
#Math.Ceil: Work on forword value. #Show exact value.
#Work on e-commerce websites. e.g: if 12.1 then output 13.
import math
x=12.1
c=math.ceil(x)
print(c)
#math.fabs() always absolute value will return.
x=-5
c=math.fabs(x)
print(c)
#math.factorial() #negative value comes as error
x=5     #means x=5x4x3x2x1=120
c=math.factorial(x)
print(c)
#math.floor() it shows same value. no next value like
# math.ceil()
x=14.9
c=math.floor(x) #output will be 14.
print(c)
#math.fsum() it will add all list number and give output
print('++++++math.fsum()+++++++++++++')
l=[1,2,3,4,5,6,7,8,9,122]
c=math.fsum(l)
print(c)
print('test')
l=[]
for n in range(1,123):
    l.append(n)
print(l)
print(math.fsum(l))
l1=[]
for a in range(1,1000):
    l1.append(a)
print('sum of 1 to 999 is',math.fsum(l1))
#math.sqrt(x) it will square root of value.
x=81
c=math.sqrt(x)
print(c)
x=21
c=math.sin(x)
print(c)
z=math.pow(2,64) # sequence double each next value. here 2 is the base and 64 is the exponent like chess game.
print('pow',z)

print(math.comb(10,4)) #combination nCr
#for fmod for % exact value in float will come only in math.fmod
print(math.fmod(5.6, 4.1))
print(5.6%4.1)
print(1e-100 % 1e100) #output is 1e-100
print(math.fmod(-1e-100 , 1e100)) #output is -1e-100

#Convert angle x from degrees to radians.
x=90
r=math.radians(x)
print(r)
#Convert angle x from radians to degrees.
print(math.degrees(r))
