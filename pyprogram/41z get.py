#get() function
Some_dict = {'a': 1, 'b': 2, 'c': 3}
key = 'd'
default_value = 0
if key in Some_dict:
  value=Some_dict[key]
  print(value)
else:
  value = default_value
  print(value)

value=Some_dict.get(key,default_value)
print(value)