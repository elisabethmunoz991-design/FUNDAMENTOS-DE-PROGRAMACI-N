'''
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta
que el usuario escriba “salir” que terminará.
'''
eco = input("Mostrar texto hasta introducir salir: ")
historial = ""
while eco != "salir":
    historial = historial + eco + "\n"
    print (historial)
    eco = input("Mostrar texto hasta introducir salir: ")

# Volver a pedir input dentro de while para que el bucle no sea infinito
