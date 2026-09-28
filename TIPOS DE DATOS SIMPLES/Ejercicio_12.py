barras = int(input("Barras con % vendidas:"))
precio = 3.49
descuento = (precio / 100) * 60
CosteF = (precio - descuento) * barras
print ("El precio de la barra de pan es ", precio , "Se hace un descuento de ", descuento, "y el coste final de ", barras, "barras de pan es", CosteF)