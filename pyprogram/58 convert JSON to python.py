#Convert JSON to python

import json
d='[{"course name":"Python","Duration":"6months","Fees":"15,000"}]'
print(d,type(d))
f=json.loads(d)  #convert files from json to python
print(f,type(f))

import json as j
f='[{"120":32,"124":36,"854":69}]' #keys in json format always in double quotation.
print(f,type(f))
f1=j.loads(f) #after loading from json to python, keys double quote replace with single quotation and single quote of
#square bracket will remove.
print(f1,type(f1))