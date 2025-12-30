pares = 0
impares = 0

while True:
    numero = int(input("Ingresa un numero (0 para salir): "))
    if numero == 0:
        break #Salirmos del bucle
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Números pares: ", pares)
print(f"Números impares: ", impares)
