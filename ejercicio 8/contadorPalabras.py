def contar_palabras_en_archivo(nombre_archivo):#en esta primera linea lo que hice fue agregarle dos puntos al final
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            return len(palabras)
    except FileNotFoundError:
        return f"El archivo {nombre_archivo} no fue encontrado." #aca fue simplemente corregir un error de escritura en el return que estaba escrito "retunr"

archivo_nombre = input("Ingrese el nombre del archivo de texto: ")
print(f"El archivo contiene {contar_palabras_en_archivo(archivo_nombre)} palabras.")
# se imprime el resultado
