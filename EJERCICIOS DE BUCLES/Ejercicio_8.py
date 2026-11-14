'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1

'''
num = int(input("Introduce un número entero: "))

for i in range(1, num + 1, 2):
    lista = list(range(i, 0, -2))
    print(*lista)

# Si el resultado del bucle cambia en cada fila = bucle dentro de bucle
# añadir * a lista en print para eliminar corchetes