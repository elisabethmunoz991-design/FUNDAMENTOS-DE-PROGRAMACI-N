inversion = float(input("Capital inicial: "))
interes = 1.04
capital = (inversion * interes )
#aqui podemos poner 1.04 o 1 + 0.04 porque seria la misma cantidad mas un incremento 4% de interes
print ("Cantidad ahorro 1 año:", round(capital,2))
capital = (capital * interes )
print("Cantidad ahorro 2 año:", round(capital,2))
capital = (capital * interes )
print("Cantidad ahorro 3 año: ", round(capital,2))

