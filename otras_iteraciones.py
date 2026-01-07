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

#--------------------------------

# subcadena_uno = "mi"
# subcadena_dos = "la"
# subcadena_tres = "ne"
# subcadena_cuatro = "sas"

# #Sumo las subcadenas

# cadena = subcadena_uno + subcadena_dos + subcadena_tres + subcadena_cuatro
# print(cadena)

# #Multiplico las subcadenas

# print(subcadena_uno *4)

#Uso de len()

# comidas = "pizza"

# print("La longitud de " + comidas + " es: " + str(len(comidas)))

#index

# provincia = "Mendoza"
# print(provincia[2])

# ciudad = "Mar del plata"
# len_total = len(ciudad)

# for indice in range(len_total):
#     print(ciudad[indice])

# cadena = "Python es un lenguaje multiproposito"
# # mostrar los primeros 6 caracteres
# print(cadena[0:6])

# #mostrar la primera posicion
# print(cadena[0])

# #Mostrar la palabra "es un"
# print(cadena[7:12])

# # Mostrar el ultimo caracter

# print(cadena[-1])

# # Mostrar la palabra "multiproposito"

# print(cadena[-14:])

# #Mostrar la cadena sin los 2 primeros y 2 ultimos caracteres
# print(cadena[2:-2])

# #Mostrar los caracteres en posicion impar
# print(cadena[::2])

# abecedario = "abcdefghijklmnopqrstuvwxyz"

# if "a" in abecedario:
#     print("La letra 'a' se encuentra en el abecedario.")
# if "33" not in abecedario:
#     print("El numero '33' no se encuentra en el abecedario.")
# if "z" in abecedario:
#     print("La letra 'z' se encuentra en el abecedario.")

# cadena = "Python es un lenguaje multiproposito"

# indice = cadena.index("l")
# print(indice)


# cadena = "Python es un lenguaje de codigo abierto"
# letra_e_cantidad = cadena.count("e")
# print("Cantidad de veces que aparece: " + str(letra_e_cantidad))

#upper() / lower()

# cadena = "Python es un lenguaje de codigo abierto"
# cadena_mayuscula = cadena.upper()
# print(cadena_mayuscula)
# cadena_minuscula = cadena.lower()
# print(cadena_minuscula)

#lstrip() / rstrip()

# cadena = "Python es un lenguaje de alto nivel"

# cadena_centrado_izquierda = cadena.ljust(50, '-')
# print(cadena_centrado_izquierda)
# cadena_centrado_derecha = cadena.rjust(50, '-')
# print(cadena_centrado_derecha)