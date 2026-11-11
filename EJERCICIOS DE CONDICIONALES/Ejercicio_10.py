'''
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.
● Ingredientes vegetarianos: Pimiento y tofu.
● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y
en función de su respuesta le muestre un menú con los ingredientes disponibles
para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el
tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la
pizza elegida es vegetariana o no y todos los ingredientes que lleva.
'''
pizza = input("¿Quiere pizza vegetariana? ")
menu1 = "Pimiento,Tofu"
menu2 = "Peperoni,Jamón,Salmón"
menu0= "Tomate,Mozzarela y"
pizzaV = "Ha elegido una pizza vegetariana"
pizzaN = "Ha elegido una pizza normal"

if pizza == "si":
    print(menu1)
    ingrediente = input("Elige un ingrediente: ")
else:
    print(menu2)
    ingrediente = input("Elige un ingrediente: ")
if ingrediente == "Pimiento":
    print(pizzaV)
    print("Con los siguientes ingredientes:",menu0,ingrediente)
elif ingrediente == "Tofu":
    print(pizzaV)
    print("Con los siguientes ingredientes:",menu0,ingrediente)
elif ingrediente == "Peperoni":
    print(pizzaN)
    print("Con los siguientes ingredientes:",menu0,ingrediente)
elif ingrediente == "Jamón":
    print(pizzaN)
    print("Con los siguientes ingredientes:",menu0,ingrediente)
elif ingrediente == "Salmón":
    print(pizzaN)
    print("Con los siguientes ingredientes:",menu0,ingrediente)
else:
    print("Ingrediente no disponible")



    

    
