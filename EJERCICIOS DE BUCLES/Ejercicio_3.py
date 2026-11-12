'''
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla todos los números impares desde 1 hasta ese número separados por
comas.
'''
num = int(input("Introduce un número entero: "))
i = 1
for i in range(1, num + 1):
    if i % 2 != 0:
        print(i, end = ",")

'para cambiar salto de linea en cada print end = "" '