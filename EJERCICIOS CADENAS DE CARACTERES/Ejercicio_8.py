'''
Escribir un programa que pregunte por consola el precio de un producto en euros
con dos decimales y muestre por pantalla el número de euros y el número de
céntimos del precio introducido
'''
precio = float(input("Introduce precio del producto: "))
precio = round(precio,2)

print (f"El precio es: {precio} euros")

'''
Poner f en los prints y meter variable en llaves para que reconozca la variable 
'''