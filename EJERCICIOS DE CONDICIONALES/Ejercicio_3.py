'''
Escribir un programa que pida al usuario dos números y muestre por pantalla su
división. Si el divisor es cero el programa debe mostrar un error.
'''
num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))
division = num1 / num2 
if division == "0":
    print ("Error")
else:
    print (f'el resultado es: {division}')


