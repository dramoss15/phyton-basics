#El programa tiene un número secreto (7)
# El usuario adivina hasta acertar.

numero_secreto = 7

while True:
    intento = int(input("Adivina el número: "))

    if intento == numero_secreto:
        print("Correcto")
        break
    else:
        print("Incorrecto")
