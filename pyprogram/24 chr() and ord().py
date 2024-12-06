#chr function
#input integer value and it converts it to a character.
#Connvert integer 65 to ASCII Character ('A')
#INTEGER TO CHARACTER
# note: In this example, chr(65) returns the character 'A', as 65 is the Unicode code point for the capital letter
# 'A'.\ The chr function is commonly used when you need to convert integer representations of characters\ (Unicode
# code points) back into actual characters in your code.
y=chr(65)
print(type(y),y)
z=chr(89)
print(type(z),z)

k=65;
print(chr(k))

#ord
#input character value and it converts it to the integer
#if a person says convert character to integer
h='a'
print(ord(h))
#if you pass more than one letter than it will come an error.
print(ord('B'))
#CHARACTER TO INTEGER
e=chr(78)
from my_functions import p
p(e)
p(type(e))
f=ord('a')
p(f)
p(type(f))
print(f,type(f),e,type(e))
print('------------------------------------------------')

z=chr(72),
print(type(z),z)
n=ord('k')
print(type(n),n)
print('------------------')
m=chr(72),ord('k')
print(m,type(m))