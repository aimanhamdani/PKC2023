hamad_age=input('enter hamad age? =')
hamad_age=int(hamad_age)
school_age=5
# calculate whether hamad can go to school or not
if hamad_age==school_age:
    print("hamad can join the school")
elif hamad_age>school_age:
    print("hamad can join higher  classes")
elif hamad_age<school_age and hamad_age >2:

    print("hamad can't join the school")
elif hamad_age<=2:
    print("hamad is a baby and need care in home")
else:
    print("enter value integer not string")
