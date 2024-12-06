from functools import reduce
l=[1,2,3,4,5,6,7,8,9]
print(l)
def add2(x):
    return x*2
print(list(map(add2,l
               )))
def add(x,y):
    return x+y
print(reduce(add,l))

def is_even(x):
    return x%2==0
print(list(filter(is_even,l)))

print('All above use with lambda function to minize the code')
print(list(map(lambda x:x*2,l)))
print(f'even numbers are {list(filter(lambda x:x%2==0,l))}')
odd_numbers=list(filter(lambda x:x%2==1,l))
print('odd number are',odd_numbers)
print(f'---------------------------------------')

import math
def area(r):
  return math.pi*r**2
radii=[1,2,3,4,5,6]
areas=[]
for i in radii:
  a=area(i)
  areas.append(a)
print(areas)
#OR

Areas=list(map(lambda x:math.pi*x**2,radii))
print(f'Areas={Areas}')
print(f'--------------------')
#convert celcius to ferhanheight
Temprature_C=[('Mumbai',35),('Islamabad',35),('Tokyo',40),('Berlin',25)]
print(type(Temprature_C))
#formula to ferhanheight=(9/5*C)+32
Temp_F=list(map(lambda x:(x[0],(9/5)*x[1]+32),Temprature_C))
print(Temp_F)
#OR
print(f'-----------------------------------')
Temprature=[('Mumbai',35),('Islamabad',35),('Tokyo',40),('Berlin',25)]
def temp(x):
    return 9/5*x[1]+32
temp_in_F=[]
for i,j in Temprature:
    # print(i)
    a=temp((i,j))
    temp_in_F.append((i,a))
print(temp_in_F)



# Temperature = [('Mumbai', 35), ('Islamabad', 35), ('Tokyo', 40), ('Berlin', 25)]

# def temp(x):
#     return 9/5 * x[1] + 32
#
# temp_in_F = []
#
# for i, j in Temperature:
#     # Convert the temperature from Celsius to Fahrenheit
#     a = temp((i, j))
#     temp_in_F.append((i, a))  # Append both city and temperature in Fahrenheit
#
# print(temp_in_F)  # Output the list of cities with temperatures in Fahrenheit

