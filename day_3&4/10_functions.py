def future_age(age):
    new_age=age+20
    return new_age
l=[]
for i in range(5):
    a=int(input("enter your age? = "))
    predicted_age=future_age(a)
    print(predicted_age)
    l.append(predicted_age)
    print("after apend = ",l)
print("after apend all = ",l)
