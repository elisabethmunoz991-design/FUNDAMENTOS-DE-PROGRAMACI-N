'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
año que dura la inversión.

'''
cantidad = int(input("Cantidad a invertir: "))
interes = float(input("interes anual en %: "))
años = int(input("Duración en años: "))
interes = interes / 100
capitalI = 0
capital = cantidad * interes
i = 1 

while i <= años:
    capitalI = capitalI + capital
    i += 1

print("El capital obtenido es de: ", capitalI, "€")