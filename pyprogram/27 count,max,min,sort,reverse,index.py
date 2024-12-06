l=[10,20,30,10,10,50]
c=l.count(10) #most repeated number
print(c)
if 10 in l:
    print(l)
if 60 in l:
    print(l)   # it will not print becz 60 is not in l
print('-------****')
#max
m=max(l) #big value
print(m)
z=['Hello','World']
m=max(z)
print(m)
print('-------------------------**')
#min
d=[10,50,60,20,5,88,99]
m=min(d) #smaller value from list
print("min",m)
print(min(d))

m=min(z)
print(m)
#sort
#ascending order, kam sa zyada5,10,20
l=[10,2,5,7,9,10]
l.sort() #arrange numbers in ascending orders
print('sort',l)
l.reverse() #arrange list in reversal order
print(l)
l=['hello','world','a','b']
l.reverse()
print('reverse',l)
l9=['hello','world','a','b']
print('reverse with slicing',l9[-1::-1])
print('---------**index**')
#index
l=['hello','world']
a=l.index('world')
print(a) # where 'world' stands in index numbers
print(l[1])
print(l.index('world'))
l10=[1,4,3,5,7,6,2]
l10.sort()
print('assending order',l10)
l10.sort(reverse=True) #if reverse=true in function then it become decending order
print('reverse',l10)
print('------************************************')
numbers=[1,2,3,4,5]
first,second,*_ =numbers
print(first)
print(second)
print(numbers)
letters=['a','b','c']
letters.append('d')
print(letters)
letters.insert(0,'1')
print(letters)
letters.pop(0)
print(letters)
letters.remove('c')
print(letters)
del letters[0:2]
print(letters)
letters.clear()
print(letters)