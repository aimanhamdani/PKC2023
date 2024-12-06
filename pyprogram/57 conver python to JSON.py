#Convert python to JSON

import json
blog={'URL':'www.wscubetech.com','name':'WScubetech'}

print(blog,type(blog))
f=json.dumps(blog)
print('dump',f,type(f))
print('')
d={'course name':'Python','Fees':'15,000'}
print(d,type(d)) #before convert to json. type is dict.
print('')
g=json.dumps(d) #json dumps command
print(g,type(g)) #after applying json dump. type is changed
# to str.
print('')

vlog={"URL":"www.aimsat.com.pk","Name":"Aimsat"}
print(vlog)
print(type(vlog))
#convert to string from dictionary with json dumps()function.
g=json.dumps(vlog)
print(g,type(g))



