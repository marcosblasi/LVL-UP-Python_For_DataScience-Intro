# Define a list of integer and float and obtain a total sum of elements in the list, in a new variable

numbers = [2, 3.14, 45, 30, 446, 55, 43]

total = 0
total_iterations = 0

for number in numbers:

    total += number
    total_iterations += 1


print("The total sum of elements in list is = ", total)
print("The total number of iterations is = ", total_iterations)
print("The total number of iterations is = ", len(numbers))
