# #Ejemplos con while

# i = 0

# while i < 100:
#     print(i)
#     i += 1

#---------------------------------

# #Ejemplo con for

# for i in range(100):
#     print(i)

# for i in range(5):
#     print("Hola, alumnos!, linea", i)

#---------------------------------

# Uso de range() con un solo argumento

# for i in range(5):
#     print(i)  # Imprime números del 0 al 4

#---------------------------------

# Dos argumentos: inicio y fin

# for i in range(3, 8):
#     print(i)
# Imprime números del 3 al 7
# Tres argumentos: inicio, fin y paso

#---------------------------------

# Tres argumentos: inicio, fin y secuencia
# for i in range(2, 17, 3):
#     print("El valor de i es:", i)
    
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# numeros = [1, 20, 3, 4, 5, 6, 7, 8, 9]
# objetivo = 20
# for num in numeros:
#     if num == objetivo:
#         print(f"¡Encontre el numero {objetivo}!")
#         break
# else:
#     print(f"No se encontro el numero {objetivo}")

# for i in range(5):
#     print(i)
# else:
#     print("El bucle termino normalmente")
