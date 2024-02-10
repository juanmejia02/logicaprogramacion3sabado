def es_palindromo(texto): #en esta primera linea lo que hice fue agregarle dos puntos al final
    texto = ''.join(caracter.lower() for caracter in texto if caracter.isalnum())
    return texto == texto[::-1]

palabra_frase = input("Ingrese una palabra o frase: ")
if es_palindromo(palabra_frase): # en esta parte lo que hice fue que entre los parentesis que tenia en la parte de if vacios le agregue "palabra_frase"a l
    print(f"{palabra_frase} es un palíndromo.")
else:
    print(f"{palabra_frase} no es un palíndromo.")
    #en esta parte imprime si el resultado es un palindromo o no
