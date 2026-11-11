'''
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa
anterior para que también funcione cuando el día o el mes se introduzcan con un
solo carácter.
'''
fecha = (input("Introduce tu fecha de nacimiento dd/mm/aaaa : "))
fecha = fecha.split("/")

print(f'Dia: {fecha[0]}')
print(f'Mes: {fecha[1]}')
print(f'Año: {fecha[2]}')


