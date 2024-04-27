# Lists
# Sets
# Arrays


# Lists: ordered values collection (objects) of different data types. Objects in the lists or lists are mutable.
# With lists we can:
# --> Obtain an element
# --> Change an element
# --> Get an element
# --> Replace an element
# --> Delete an element

# Sets: are like list but they not admit equal values. Operations that can be done are:
# --> Union
# --> Intersection
# --> Get an element
# --> Delete an element
# --> Simetric difference
# --> Non simetric difference

# Arrays: bidimensional data structure. We say that its a list of lists. Data is 
# --> Sum and difference
# --> Product
# --> Product by a unique number
# --> Transpose
# --> Inverse
# --> Determinant

# Loops: While / For

# Conditionals practice

a = 10
b = 20

if (a > b) and b (b%2 == 0):
    print("Validation not successfull")
elif a < b:
    print("Validation successfull")
else:
    print("Values are equal")

age = 20
active = True

if age > 18 and active == True:
    print("Active partner")

else:
    print("Non-active partner")

user_number = int(input("Insert number to be evaluated: "))

if user_number > 0:
    print("Inserted number is positive")
elif user_number == 0:
    print("Inserted number is equal to cero")
else: 
    print("Inserted number is negative")

list1 = []
list2 = ['Jonh', 'Mary', 'Peter', 'Michaela']
list3 = ['John', 10, 3.14, True, 11, 33, 44, 'Hey', 9, 33, 444, 55]

print(list1)
print(list2)
print(list3)

print(list3[-4])
print(len(list2))

list3.append('Marcos_B')    # add an element at the end a list
print(list3)

position = list3.index(33)  # define a position of an element inside a list
print(position)
list3[position] = 140       # Replacing a value
print(list3)

pertaining = 'Peter' in list2
print(pertaining)           # See if an element is inside a list

