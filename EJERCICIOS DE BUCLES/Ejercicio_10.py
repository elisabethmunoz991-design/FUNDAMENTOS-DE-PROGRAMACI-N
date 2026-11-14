'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es un número primo o no.

'''
n = int(input("Introduce un número entero: "))
primo = True
if n < 2:
    primo = False

for i in range(2, n):
    if n % i == 0:
        primo = False
if primo == False:
    print("No es primo.")
else:
    print("ES primo.")

# Primo = divisible solo entre el mismo y uno 




