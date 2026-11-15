'''
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
una a una las letras de la palabra introducida empezando por la última.
'''
palabra = input("Introduce una palabra: ")


for i in range(len(palabra) -1, -1, -1):
    print (palabra[i])
    
# A palabra le quitamos 1 porque i empieza en 0 
# El indice siempre termina en una posición menor a la longitud