'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es par o impar.
'''
num = int(input("Introduce un número entero: "))
if (num%2) == 0:
    '''
     cuando ponemos el número entre comillas no sale el resultado cuidado!!
    '''
    print (f"El número {num} es par. ")
else:
    print  (f"El número {num} es impar.")