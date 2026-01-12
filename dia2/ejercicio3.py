#Pide contraseña hasta que sea "1234".

while True:
    contraseña = input("Ingrese la contraseña: ")
    if contraseña == "1234":
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta")