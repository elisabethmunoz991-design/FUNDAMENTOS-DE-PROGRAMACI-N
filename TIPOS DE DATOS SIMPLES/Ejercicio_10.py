payasos = int(input("Payasos último pedido:"))
muñecas = int(input("Muñecas último pedido:"))
pesoPayasos = payasos * 112
pesoMuñecas = muñecas * 75
pesoTotal = pesoPayasos + pesoMuñecas

print("El peso total del envio es: " ,pesoTotal ,"g")