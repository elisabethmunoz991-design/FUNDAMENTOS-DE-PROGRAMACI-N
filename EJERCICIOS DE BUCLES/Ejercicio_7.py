'''
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
'''

num = int(input("Introduce un número entero: "))

for i in range(1, 11):
    resultado = num * i
    print (num, "x",  i, "=", resultado)
    i += 1 


    