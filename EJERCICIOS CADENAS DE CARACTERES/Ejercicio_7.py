correo = input("Introduce tu correo electrónico: ")
partes = correo.split("@")
correo = correo.replace(partes[1],"ceu.es")
print(correo)