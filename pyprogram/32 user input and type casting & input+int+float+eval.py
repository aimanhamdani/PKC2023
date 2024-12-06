a=eval(input('English'))
print(a)
b=eval(input('Statistics'))
print(b)
print(a+b)

a=int(input('english'))
b=int(input('maths'))
print(a+b)


#The eval() function in Python is used to evaluate a string as a Python expression. It takes a string as an argument,\
# and returns the result of the expression.
#result = eval("2 + 3 * 5")
#print(result)  # Output: 17
#In this example, eval("2 + 3 * 5") evaluates the string "2 + 3 * 5" as a Python expression and returns the result,
# which is 17.

#However, it's important to use eval() with caution, especially when working with user-provided input,
# as it can execute arbitrary code and pose security risks.