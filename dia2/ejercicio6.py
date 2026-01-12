#El usuario tiene 3 intentos para escribir "python"

intentos = 0

while intentos < 3:
    palabra = input("Escribe la palabra: ")

    if palabra == "python":
        print("Correcto")
        break
    else:
        intentos += 1
        print("Intento", intentos, "fallido")

if intentos == 3:
    print("Intentos agotados")

