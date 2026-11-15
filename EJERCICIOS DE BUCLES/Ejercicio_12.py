'''
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
muestre por pantalla el número de veces que aparece la letra en la frase.
'''
frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")
contador = 0

for i in range(0, len(frase), 1):
    if frase[i] == letra:
         contador += 1

print ("La frase contiene", contador, "veces la letra", letra)

# El print sobre i no funciona porque es un indice
# Hay que sacar contenido de esa posicion frase[i]
# En orden  descendente si habría que quitar una posición!!!
