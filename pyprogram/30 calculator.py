print('''
+ ADD
- SUBTRACT
* MULTIPLE
/ DIVISION
''')
nums=[]
for a in range(1,4):
    print(a)
    num1=int(input('Enter the value 1:-'))
    num2 = int(input('Enter the value 2:-'))
    opr=input('Enter the opr */-+')  #no need int. enter the operator
    if opr=='+':
        result=num1+num2
    elif opr=='-':
        result=num1-num2
    elif opr=='/':
        result=num1/num2
    elif opr=='*':
        result=num1*num2
    else:
        print('Invalid opr')
        a-=1
    if result is not None:
        print(result)
        nums.append(result)
        print('nums = ', nums)
    else:
        continue


print('nums = ', nums)


