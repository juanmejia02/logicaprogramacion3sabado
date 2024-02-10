def factorial(n): #en esta primera linea lo que hice fue agregarle dos puntos al final
    if n == 0 or n < (1): #en esta parte solo hizo falta encerrar el 1 en parentesis y agregar dos puntos al final y cambie el igual por un signo de menor que
        return (1)
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {numero} es {factorial(numero)}") # aca estba llamando la funcion factorial sin proporcionar el argumento "numero" y simplemetnte fue meterlo en ls parentesis que habian solos
