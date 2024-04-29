# ------------------------------------------------------- Exercises ----------------------------------------------------------------------- #

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

product_list = ['Moon burguer', 'Super hot dog', 'Extra cheese chicken nuggets', 'Empanadas']
new_supplier_list = ['Super double hot dog','Individual pizza']

new_product_list = product_list + new_supplier_list

new_product_list.remove('Empanadas')

print(new_product_list)
print(type(new_product_list))

# ------------------------------------------------------------------------------------------------------------------------------------------ #

# Parte 2 - Ejercicio de tarea 1
# Dada la siguientes lista en Python correspondiente a la nómina inicial de la selección juvenil de futbol mixto del Club MateAmargo: ['Juan', 'Micaela', 'Emilia', 'Cecilia', 'Juan Manuel', 'Valentina', 'Luciano']
# Recientemente se sumaron al equipo: "Augusto" y "David". Agregar dichos elementos a la lista inicial.
# Además Juan tuvo que salir de la lista por estar fuera por lesión durante al menos 6 meses.
# Sumar a la lista inicial concatenando la lista de suplentes: ['Julieta', 'Jose', 'Franco']
# Realizar una copia de 'back up' de la nomina y guardarlo en una nueva variable lista_backup

initial_team = ['Juan', 'Micaela', 'Emilia', 'Cecilia', 'Juan Manuel', 'Valentina', 'Luciano']

initial_team.append('Augusto')
initial_team.append('David')
initial_team.remove('Juan')

initial_team = initial_team + ['Julieta', 'Jose', 'Franco']

backup_list = initial_team

print(initial_team)
print(backup_list)

# ------------------------------------------------------------------------------------------------------------------------------------------ #

# Parte 2 - Ejercicio de tarea 2
# Dada los siguientes conjuntos:
# c1 = {1, 2, 'Juan', 'Maria', True, 5.55, 24.3}
# c2 = {1, 10, 'Diego', 'Karina', False, True, 33.3}
# Obtener la interseccion y la union de los conjuntos e imprimir en pantalla el resultado.

c1 = {1, 2, 'Juan', 'Maria', True, 5.55, 24.3}
c2 = {1, 10, 'Diego', 'Karina', False, True, 33.3}

union1 = c1|c2
intersection1 = c1&c2

print("Sets insersection is: ", intersection1)
print("Sets union is: ", union1)


