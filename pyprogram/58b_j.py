#use 58a as json to convert in 58b
#3steps to make workable in python of json file
#1.open
#2.read
#3.loads
#then iterate as per your requirement and need of work
import json
file=open("58a_post.json","r")
print("open",file,type(file))
print('--'*20)
x=file.read()
print('read',x,type(x))
f=json.loads(x)
print('convert to python',f,type(f))
for a in f:
    print(a['name'],a['city'])