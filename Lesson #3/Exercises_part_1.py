
# -------------------------------------------- Exercise 1 - Part 1 ---------------------------------------------- #

''' Define a list of values including floats and integers, and obtain the total sum of all elements, which will
    be saved in a new variable called sum'''

sum = 0                                                                     # Define an empty variable where we will sum list values

numbers_list = [1, 3.14, 850.423, 2*3, 4.5/2.34, 2, 5.63]                   # Define the numbers list

for number in numbers_list:                                                 # For cycle 

        sum += number                                                       # Sum of each list element

        print(f"The number {number} was summed to the variable 'sum'")      # We track the summed element


print("The final obtained value is", sum)                                   # Print the final value


# -------------------------------------------- Exercise 2 - Part 1 ---------------------------------------------- #

''' Define a list of numeric values (int & float) and obtain the maximum value, which will be saved in a new 
    variable callend 'maximum' '''

maximum = 0

new_numbers_list = [1, 3.14, 850.423, 2*3, 4.5/2.34, 2, 5.63]                   # Define the numbers list

for number in new_numbers_list:
        
        if number > maximum:
                
                maximum = number
        
        else:
                pass
        
print(f"The maximum registered value is {maximum}")

# -------------------------------------------- Exercise 3 - Part 1 ---------------------------------------------- #

'''Supongamos que tenemos una lista de estudiantes y sus calificaciones en diferentes materias, representada como un 
   diccionario donde la clave es el nombre del estudiante y el valor es una lista de calificaciones. Se pide calcular 
   el promedio de cada estudiante y determinar si aprobaron o reprobaron cada materia, considerando que la nota mínima 
   para aprobar es 60. calificaciones = {     'Juan': [80, 75, 90],     'María': [65, 70, 55],     'Pedro': [40, 60, 70] }'''

course_grades = {     'John': [80, 75, 90],     'Mary': [65, 70, 55],     'Peter': [40, 60, 70] }
average = 0

for student, grades in course_grades.items():                                           # We iterate in the keys() of the dictionary
        
        print(f"The first student to be evaluated is {student}")                        # We mention the student name to be evaluated
        
        for grade in grades:                                                            # We iterate inside the values of the dicc (lists)
                
                if grade > 60:                                                          # Was the exam passed?
                        
                        average += grade
                        print(f"The subject was passed with {grade} points")            # Final message

                else:
                        average += grade
                        print("The subject was not passed")                             # Final grade message

        average = (average/3)                                                           # Average grade for each student
        print(f"Average {student}'s course grade was ", average)                        
        average = 0                                                                     # Average variable reset

