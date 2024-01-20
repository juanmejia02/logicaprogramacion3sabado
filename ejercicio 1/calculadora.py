def calculadora():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")

    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        resultado = num1 / num2
    else:
        resultado = "Operación no válida"

    print("Resultado", resultado)

calculadora()

# primero que todo en la parte de arriba en la funcion float se estaba denominando para poner numeros y le estabamos poniendo un comentario entonces simplemente
# se le agrega un input al float del num1 y num2