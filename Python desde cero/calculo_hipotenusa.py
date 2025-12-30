# Calculo de una hipotenusa

# Pedimos las longitudes de los catetos
cateto_a = float(input("Ingresa la longitudo del primer cateto: "))
cateto_b = float(input("Ingresa la longitudo del segundo cateto: "))

# Calculamos la hipotenusa
hipotenusa = (cateto_a**2 + cateto_b**2) ** 0.5

# Mostramos el resultado coo un string 
print("La hipotenusa es: " + str(hipotenusa))

