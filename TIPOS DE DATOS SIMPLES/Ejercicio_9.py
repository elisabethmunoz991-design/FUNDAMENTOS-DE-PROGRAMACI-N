cantidad = float(input("Cantidad a invertir: "))
interes = float(input("Interés anual:"))
años = int(input("Numero de años: "))
capital = cantidad * (1 + interes / 100) ** años

print("Capital obtenido:", capital)
