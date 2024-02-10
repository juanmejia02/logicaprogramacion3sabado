#se define una funcion
def celsius_a_fahrenheit(celsius):  #se agregan dos puntos:
 #se calcula la temperatura con una formula de conversion para luego retornar el resultado  
    return (celsius * 9/5) + 32 # en esta linea simplemente le hacia falta un "+" entre el ") y 32"
#se solicita poner la temperatura en celcius
temperatura_celsius = float(input("Ingrese la temperatura en Celsius: "))#se agrega un input
#se llama a la funcion celcius_a_fahrenheit con la temperatura_celcius para convertir la temperatura ingresada
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
#imprime el resultado convertido
print(f"{temperatura_celsius}°C es igual a {temperatura_fahrenheit}°F")
