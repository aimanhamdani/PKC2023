#there are two types of loops:
#1. while loop
#2. for loop
#while loop
x=0
while x<5:
    print(x)
    x=x+1
    print("x = ",x)
#for loop
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print(days)
# for d in days:
#     if (d=="Fri"):break
#     print(d)
for d in days:
    if d=="Fri":continue
    print(d)




