import json

# Load and print the contents of the JSON file
with open('contacts.json', 'r') as file:
    contacts = json.load(file)
    print(contacts)