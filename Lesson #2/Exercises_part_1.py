# ------------------------------------------------------- Exercises ----------------------------------------------------------------------- #

# Parte 1 - Ejercicio de clase

# Escribe un programa en Python que solicite al usuario que ingrese un número.
# Determinar si el número ingresado es positivo, negativo o cero, e imprimir el resultado correspondiente en pantalla.
# Si es positivo multuplicar el número por 2
# Si es negativo multuplicar el número por 3
# Imprimir los resultados en pantalla

# Insert number 
user_num = float(input("Insert number to be evaluated: "))

# Condition

if user_num > 0:
    
    print("The double of chosen number is = ", user_num*2)

elif user_num < 0:

    print("The triple of inserted number is= ", user_num*3)

else:

    print("Inserted number is equal to zero")

# ------------------------------------------------------------------------------------------------------------------------------------------ #

# Escribe un programa en Python que solicite al usuario que ingrese un número.
# Luego, el programa debe determinar si el número ingresado es par o impar, y realizar una transformación sobre el número según el caso.
# Si el número es par, dividirlo por 2.
# Si el número es impar, elevarlo al cuadrado. Finalmente, el programa debe imprimir el resultado transformado en pantalla.    

# Insert number 
user_num = float(input("Insert number to be evaluated: "))

if (user_num % 2 == 0):
    
    print("Half of chosen number is = ", user_num/2)

else:

    print("Square of chosen number is = ", user_num**2)

# ------------------------------------------------------------------------------------------------------------------------------------------ #

# Parte 1 - Ejercicio de tarea 2

# Supongamos que tienes cuatro productos en una tienda en línea: zapatillas, antiparras, mancuernas y tobilleras. 
# Cada producto tiene un estado activo que indica si está disponible para la venta o no, y un precio asociado. 
# Se debe definir una variable por cada producto (4), sus estados (4 variables más) y su precio (4 variables más).

# Escribir un programa en Python que determine el primer producto en oferta que encuentre.
# Un producto se considera en oferta si está disponible para la venta y su precio es menor o igual a $20.000. 
# El programa debe imprimir en pantalla el nombre de los productos en oferta.

product1 = 'shoes'
product2 = 'goggles'
product3 = 'dumbbell'
product4 = 'ankle brace'

state1 = 'unavailable'
state2 = 'unavailable'
state3 = 'available'
state4 = 'unavailable'

price1 = 10000
price2 = 25000
price3 = 10000
price4 = 5000


if state1 == 'available' and price1 <= 20000:
            
    print("Product on sale is: ", product1)

elif state2 == 'available' and price2 <= 20000:

    print("Product on sale is: ", product2)

elif state3 == 'available' and price3 <= 20000:

    print("Product on sale is: ", product3)

elif state4 == 'available' and price4 <= 20000:

    print("Product on sale is: ", product4)


# ------------------------------------------------------------------------------------------------------------------------------------------ #

# Definir una lista de productos de un local de comida para obtener el maestro de produtos
# Hamburguesa Moon
# Mega panchos
# Nuggets extra queso
# Empanadas
# Se contrata un nuevo proveedor el cual adiciona 2 nuevos productos a nuestro maestro que antes no estaban:
# Super pancho doble
# Pizza individual
# De la misma forma, el proveedor de el artículo empanadas deja de producir en el pais.
# Definir una lista que contenga el maestro de productos inicial y realizarle las actualizaciones correspondientes imprimiendo el maestro inicial y el final.
