'''Write a program that asks the user its age and name 
and verifies if the user has at least 18 years old and its name starts with 'a' or 'A'.
If not, access is denied '''

name = str(input("Insert user name: "))
age = int(input("Insert user age: "))

if ( ((name[0] == 'A') or (name[0] == 'a')) and (age >= 18) ):

    print("Access granted")

else:
    
    print("Access denied")

'''Write a program that asks the user to insert two numbers.
   Program must calculate the final result as the sum of the 
   squares of each number. If result is greater than 100 the 
   program must print "greater than maximum surface. Otherwise
   the program must print 'surface enabled'''

number_1 = float(input("Insert first number = "))
number_2 = float(input("Insert second number = "))

surface = number_1**2 + number_2**2

if surface > 100:

    print("Greater than maximum surface.")

else: 

    print("Surface enabled")

