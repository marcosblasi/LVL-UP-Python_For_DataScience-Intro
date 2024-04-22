# Define a function named "average" that takes 3 parameters (grades) as input and calculates the average final grade
# Then apply this function to three different values and save the final value in a variable called "promedio"
# Print the final value

def average(a, b, c):

    return ((a+b+c)/3)


grade_1 = 50
grade_2 = 24
grade_3 = 98

promedio = average(grade_1, grade_2, grade_3)

print("Final grade is (average): ", promedio)

# Define a function that shows a variable ID in memory. Call function with at leats three different variables and show how them change

def show_id(variable):

    print("Variable id is: ", id(variable))

show_id(4)
show_id(3.14)
show_id("Marcos")

# Write a program that asks the user his name and age using function "Input"
# Use notation "f-string" to concatenate name and age in a text string that says 'Hello, [name]. You are [age] years old'

name = str(input("Insert you full name here: "))
age = int(input("Insert your age here: "))

print(f"Hello, {name}. You are {age} years old.")

# Define different kind of variables in python (integer, float, string, boolean) and print their 'type'

a = 5
b = 3.14
c = 'house'
d = False

print("Integer type ", type(a))
print("Float type ", type(b))
print("String type ", type(c))
print("Boolean type ", type(d))

# Write a program that asks the user for 2 integer numbers, sum both numbers and show final result on the screen

number_1 = int(input("Insert first integer number here: "))
number_2 = int(input("Insert second integer number here: "))

result = number_1 + number_2

print("Final sum result of both integer number is equal to = ", result)




