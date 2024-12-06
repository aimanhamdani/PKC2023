# d={
#     'course':'python',
#     'fees':'8,000',
#     'duration':'2months'
# }
# # print(type(d))
# # f=d['fees']
# # print(f)
# # print('------'*20)
# # for n in d:
# #     print(n) #only return key
# #     print(d[n]) #only return value
# #    # print(n, ":", d[n]) # both key and value will return
# # print('---***************************')
# # c=d.get('course')
# # print('get course=',c)
#
# # #simple method to get
# # c1=d['course']
# # print(c1)
# print(f'----------k,v---------')
# for k,v in d.items():
#     print(k)
#
# print(f"{'-'*10}working my own practice{'-'*10}")
# # Create a dictionary of contacts; names as keys, phone numbers as values
# contacts = {"Suresh Datta": "345-555-0101", "Colette Browning": "483-555-0119", "Skey Homsi": "485-555-0195"}
#
# # Ask user for a name, then display the number
# # name = input("Enter a name: ")
#
# # If name is not in the contacts dictionary, a KeyError exception will be raised
# # number = contacts[name]
#
# # print("Number is: {:s}".format(number))
# print('----------------------------------')
# # contact1={"Aiman":3008503524,"Saqi":3005071439,"Abu":6228038}
# # print(contact1,type(contact1))
# # name=input("entry name:")
# # number=contact1[name]
# # print(number)



import json
import os

# Define the filename for storing contacts
filename = 'contacts.json'

# Load existing contacts if the file exists
contact1 = {}
if os.path.exists(filename):
    with open(filename, 'r') as file:
        contact1 = json.load(file)

print(contact1,type(contact1))
for i in range(1,6):
    print(i)
    name=input("enter the name:")
    contact=int(input("update the contact number:"))
    contact1[name]=contact
    print(contact1)
print(f"final result= {contact1}")

# Save contacts to a JSON file
with open(filename, 'w') as file:
    json.dump(contact1, file)


