def es_primo(numero): #en esta primera linea lo que hice fue agregarle dos puntos al final
    if numero < (2): #en esta parte solo hizo falta encerrar el 2 en parentesis y agregar dos puntos al final
        return False
    for i in range(2, int(numero**0.5) + 1):#en esta linea lo que hice fue agregarle dos puntos al final
        if numero % i == (0): #en esta parte solo hizo falta encerrar el 0 en parentesis y agregar dos puntos al final
            return False # en esta parte organice la ortografia de return
    return True # en esta parte organice la ortografia de return

limite = int(input("Ingrese el límite superior para encontrar números primos: "))
primos = [num for num in range(2, limite + 1) if ("es_primo")] #aca simplemente arregle el es_primo encerrandolo en parentesis y comillas dentro de los parentesis
print("Números primos:", primos) 
# se imprime el resultado
