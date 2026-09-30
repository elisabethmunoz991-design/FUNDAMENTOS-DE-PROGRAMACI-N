'''
Escribir un programa que pregunte el nombre del usuario en la consola y un número
entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces
como el número introducido.
'''
nombre = input("Escribe tu nombre: ")
numero = int(input("Escribe un numero entero: "))

print ((nombre + "\n") * numero)

#Si añadimos \n hace el salto de linea 
#Tambien se podria escribirprint (f"{nombre} \n" * numero)