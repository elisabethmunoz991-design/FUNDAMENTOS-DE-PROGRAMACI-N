'''
Escribir un programa que pregunte por consola el precio de un producto en euros
con dos decimales y muestre por pantalla el número de euros y el número de
céntimos del precio introducido.

'''
precio = input("Introduce precio: ")
precio = precio.replace(",",".")
partes = precio.split(".")
print(partes[0], "euros y", partes[1], "centimos.")
