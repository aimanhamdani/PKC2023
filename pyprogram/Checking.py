#Method1:

import Module1
print(Module1.sum(10,20))
print(Module1.mul(20,20))
print('')
#Method2
from Module1 import sum
print(sum(10,30))
print('')
#Method3 this is called /alias' denote
#shorter key
import Module1 as m
print(m.sum(10,20))
print(m.mul(30,30))
print('')

import Module1 as k
print(k.sum(10,30))
