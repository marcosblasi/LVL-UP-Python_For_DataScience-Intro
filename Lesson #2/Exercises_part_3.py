# ------------------------------------------------------- Exercises ----------------------------------------------------------------------- #

# Parte 3 - Ejercicio de clase
# Escribir un programa que declare una variable tipo lista que contenta elementos numéricos.
# Recorrer la lista definida, evaluando si el elemento iterado es "mayor o igual a cero" o si es "menor a cero" e imprimirlo en pantalla.

number_list = [1, 2, 6, 80, -3.14, 8, 25, -5/2]

for number in range(1, 8):

    if number_list[number] > 0:

        print("Evaluated number is greater than zero")

    elif number_list[number] < 0:

        print("Evaluated number is lower than zero")

    else:

        print("Evaluated number is equal to zero")

# ------------------------------------------------------------------------------------------------------------------------------------------ #

# Parte 3 - Ejercicio de tarea 1
# Definir una lista con al menos 5 nombres entre los cuales esté "Pedro" y luego iterar la lista hasta encontrar a Pedro para luego imprimir en qué posición de la lista se encuentra.
# Tipo: Utilizar la función index para obtener la posicion del elemento en la lista.

name_list = ['John', 'Alfred', 'Mary', 'Peter', 'Louis', 'Jane', 'Sophie', "Niamh"]

for name in name_list:

    if name == 'Peter':

        print('Peter was found in position {} of the list'.format(name_list.index('Peter')))

# ------------------------------------------------------------------------------------------------------------------------------------------ #

# Parte 3 - Ejercicio de tarea 2

# Escribe un programa que solicite al usuario ingresar un número entero positivo 
# y luego imprima todos los números restantes hasta el 10, desestimando en caso 
# de que el valor sea 5. Notificar en caso de que un valor superior a 10 sea ingresado.

number = int(input("Insert number to be evaluated: "))

if number > 10:

    print("Inserted number is greater than 10")

else:

    for i in range(number, 11):

        if i == 5:
            pass
        else:
            print(i)









