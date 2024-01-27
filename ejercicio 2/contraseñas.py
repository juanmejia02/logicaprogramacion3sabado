# se importan las funciones random y string
import random #en esta primera linea simplemente fue corregir la palabra random ya que estaba como "rando"
import string
# se define una funcion llamada generar contraseña con la palabra longitud como argumento

def generar_contraseña(longitud=8): #en esta cuarta linea la funcion no estba definid y simplemente fue corregir eso agregandole un "def"
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña # en esta septima linea se corrige el return ya que estaba mal escrito "retunr"

print(generar_contraseña()) #en esta novena linea la palabra contraseña estaba escrita "contrasena"
