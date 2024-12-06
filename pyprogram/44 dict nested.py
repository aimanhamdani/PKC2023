#python nested dictionary
courses={
    'php':{'duration':'2months','fees':'15,000'},
    'python':{'duration':'3months','fees':'10,000'},
    'java':{'duration':'4months','fees':'20,000'}
}
print(courses)
print('')
print(courses['php'])
print(courses['php']['duration'])
print('')
print('FOR LOOP')
# #use loop
# print('print l,m check')
for a,b in courses.items():
     # print(a,b)
     # print('')
     print(a,b['duration'])
# print('--'*20)
# print('PRINT COURSES')
#
courses['java']['duration']='6months'
print(courses)

family={
    'jawad':{'Ami':59,'saqi':36},
    'Aiman':{'zahra':34,'mehdi':13,'fatima':10}
}
print(family)
print(family['Aiman'])
print(f'--------------')
family['jawad']['Aiman']=39
print(family)
print(f'-----after deletion-----')
del family['jawad']['Aiman']
print(family)
print(f'-----------ttttt---------')
for k,v in family.items():
    print(f'hi {k,v}')
