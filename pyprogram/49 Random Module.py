#Random Randint Method:
#return a number b/w integer 5,10 #5 & 10 will include.
import random
# n=random.randint(5,10)
# print('randint',n)
# print('')
# #Random Randrange Method:
# n1=random.randrange(5,10) # only 5 included, range fun. use
# print('random range=',n1)

#Random Choice Method:
#Will use return a random element from list:
# l=[10,20,30,40,50,60]
# lc=random.choice(l)
# print('lc no=',lc)
# print('random choice',lc)
# print('')
# m=['apple','orange','banana','grapes']
# print(random.choice(m))
#         # OR
# m1=random.choice(m)
# print(m1)
# print('')
#Random,Shuffle, Uniform
#Random #give random value b/w 0to1
r=random.random()
print(r)
# #Shuffle    #Shuffle works in list, give value by shuffling the list
l=[5,10,15,20,25]
random.shuffle(l)
print('shuffle',l)
#Uniform #Give value in float like random but
# random give value b/w 0 and 1.
u=random.uniform(3,7)
print(u)