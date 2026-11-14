'''
Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
correcta.

'''
passw = "Eli"
contraseña = input("Contraseña: ")
while contraseña != passw:
    contraseña = input("Contraseña: ")
print("Contraseña correcta.")