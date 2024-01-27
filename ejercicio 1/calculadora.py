#este codigo define una funcion que sirve para hacer operaciones aritmeticas basicas( como suma, resta, multiplicacion y division)
def calculadora():
    #la funcion contiene tres variables, de las cuales dos son de tipo float y una de tipo string
    num1 = float(input("Ingrese el primer número: ")) #se agrega la funcion input
    num2 = float(input("Ingrese el segundo número: ")) #se agrega la funcion input
    operacion = input("Ingrese la operación (+, -, *, /): ")

    if operacion == '+':
        resultado = num1 + num2 #se le agrega el 1 a num y queda el codigo num1
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2 #se le agrega el 1 a num y queda el codigo num1
    elif operacion == '/':
        resultado = num1 / num2 #se le agrega el 1 a num y queda el codigo num1
    else:
        resultado = "Operación no válida"

    print("Resultado:", resultado) #la parte del codigo no estaba concatenado

calculadora() #simplemente fue ponerle un a porque estaba escrito originalmente calcu"l"dora y se le pone la a y queda calcu"la"dora
