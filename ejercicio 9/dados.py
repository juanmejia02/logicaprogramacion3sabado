import random #simplemente fue colocarle la letra n a la palabra random

def simular_lanzamiento_dados(cantidad_dados, caras_por_dado):
    resultados = [random.randint(1, caras_por_dado) for _ in range(cantidad_dados)]
    return resultados #aca fue simplemente corregir un error de escritura en el return que estaba escrito "retunr"

cantidad_dados = int(input("Ingrese la cantidad de dados a lanzar: "))
caras_por_dado = int(input("Ingrese la cantidad de caras por dado: "))
lanzamientos = simular_lanzamiento_dados(cantidad_dados, caras_por_dado)
print(f"Resultados del lanzamiento: {lanzamientos}")