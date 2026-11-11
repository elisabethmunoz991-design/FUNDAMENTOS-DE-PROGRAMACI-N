'''
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y
el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y
los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un
programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
que le corresponde.
'''
nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo(M/H): ")

if nombre [0] < "M" and  sexo == "M":
    print ("Perteneces a grupo A")
elif nombre [0] >= "M" and  sexo == "M":
    print ("Perteneces a grupo B")
elif nombre [0] < "M" and  sexo == "H":
    print ("Perteneces a grupo B")
elif nombre [0] >= "M" and  sexo == "H":
    print ("Perteneces a grupo A")

    




'''
para hacer salto de linea:

'''