# d={
#     'name':'python',
#     'fees':'8,000',
#     'duration':'2months'
#     }
# #Get, (keys, value,items we use for loop)
# n=d.get('name')   #get
# print(n)
# for a in d.keys():   #only print keys
#     print(a)
# for b in d.values():
#     print(b)
# for c,d in d.items():
#     print(c,d)
#######
d={
    'name':'python',
    'fees':'8,000',
    'duration':'2months'
    }   #delete,pop,dict,update,insert,
print(d)
del d['fees']
print(d)
print('***************+++++++//////')
e={
    'name':'python',
    'fees':'8,000',
    'duration':'2months'
    }
print(e)
o=e.pop('duration')
print(o)
print(e)

print('++++++++++++++++++++++++++++')
f={
    'name':'python',
    'fees':'8,000',
    'duration':'2months'
    }
a="The value of f is  {}.".format(f).upper()
print(a)
f.update({'fees':'10,000'})
print('updated fees',f)
f['desc']='This is python'
print(f)
f['powerBI']='1month'
print(f)
f['ms excel']='15days'
print('updated with excel',f)
del f['powerBI']
print(f)
g=f.pop('desc')
print(g)
print('-----------------')
print(f)
#
