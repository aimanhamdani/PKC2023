# a=int(input('Enter the value:-'))
# if a % 2==0:
#     print(a,'Even Number')
#     print('Welcome to wscubetech')
#     print('Syed Aiman Aali Hamdani')
#     print('Learning python')
# else:
#     print(a,'odd number')
#     print('this is odd that is why others are not printed')
#
# per=int(input('Enter the value1:-'))
# if per>=60:
#     print('First Div')
# elif per>48:
#     print('Second Div')
# elif per>=35:
#     print('Third Div')
# elif per>=33:
#     print('Pass')
# else:
#     print('Fail')
# #
# # How to make a simple calculator
# print('''
# + ADD
# - SUBSTRACT
# * MULTIPLE
# / DIVISION
# % PERCENTAGE
# ''')
# num1=int(input('Enter the value1:-'))
# num2=int(input('Enter the value2:-'))
# opr=input('Enter the opr'',''+-*/%')  #no need int. enter the operator
# if opr=='+':
#     print(num1+num2)
# elif opr=='-':
#     print(num1-num2)
# elif opr=='*':
#     print(num1*num2)
# elif opr=='/':
#     print(num1/num2)
# elif opr=='%':
#     print(num1/num2*100,'%')
# else:
#     'Invalid opr...'

print("""
+add
-substract
* multiple
/divide
% percentage
""")

num1=int(input("Enter the value 1 :-"))
num2=int(input("Enter the value 2 :-"))
opr=input("Enter the operators""," "+-*/%")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
elif opr=="%":
    print((num1/num2)*100 ,"%")
else:
    print("invalid operators")
