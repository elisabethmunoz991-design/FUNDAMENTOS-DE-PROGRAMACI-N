'''
Escribir un programa que pregunte por consola por los productos de una cesta de la
compra, separados por comas, y muestre por pantalla cada uno de los productos en
una línea distinta.
'''
compra = input("Introduce lista de la compra; ")
lista = compra.split(",")
print ( sep= "\n",*lista) 



'''
metemos el sep = "\n" para el salto de lineas
cuidado con las comillas 
para que nos de el array por elementos separados usamos * 
'''