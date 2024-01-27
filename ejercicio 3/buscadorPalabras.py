def contar_palabra(texto, palabra): # en esta primera linea lo unico que habia que corregir era al final ponerle los dos puntos
    return texto.lower().split().count(palabra.lower())

texto = "Este es un ejemplo de texto. Este texto tiene palabras repetidas."
palabra_buscada = "hola"

print(f"La palabra '{palabra_buscada}' aparece {contar_palabra(texto, palabra_buscada)} veces.") #en esta septima linea lo que pasa era en "palabra_buscada"
# habia que cerrar un corchete y una comilla, y en "contar_palabra" habia que agregar el corchete de inicio
