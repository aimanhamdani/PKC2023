# pickle.load() - takes file object and return corresponding python format (readable )
# pickle.loads() - takes the binary format and returns python format
# pickle.dumps() - takes the variable and returns binary string
import pickle
l=[10,20,30,40,50,60225555555]
write_binary=open('56a_writedata.txt', 'wb')
pickle.dump(l,write_binary)
write_binary.close()

read_binary=open('56a_writedata.txt','rb')
f=pickle.load(read_binary)
print('f',f)

# import pickle
#
# # Pickling
# with open('data.pkl', 'wb') as file:
#     data = {
#         'integer': 42,
#         'float': 3.14,
#         'string': 'Hello, Pickle!',
#         'list': [1, 2, 3],
#         'custom_object': {'name': 'CustomObject'},
#         'function': lambda x: x * 2
#     }
#     pickle.dump(data, file)
#
# # Unpickling
# with open('data.pkl', 'rb') as file:
#     loaded_data = pickle.load(file)
#
# print(loaded_data)


