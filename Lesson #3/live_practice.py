
my_dictionary = {"name": 'Luciano', "Languaje": 'Python', "Location": 'Coghlan (44.33, 55.43)', "Number": 45}

print(my_dictionary)

print(id(my_dictionary))      # "id" function returns the memory space of the variable.

dicc = {}                     # we define an empty dictionary

dicc2 = {
    'name': 'Marcos',
    'age': 30,
    'language': 'spanish', 
    'location': (53.4, 44.3)  # Location lat longs are defined as tuples
}

print(dicc2)

print(dicc2['location'])
print(dicc2['location'][0])
print(dicc2['location'][1])

# How to obtain keys in a dictionary

print(dicc2.keys())         # This methods return lists, so we can go through each element of the dictionary
print(dicc2.values())       
print(dicc2.items())        # This methods return tuples

for item in dicc2.items():  # How to iterate dictionaries

    print(item)
    print(item[0])

