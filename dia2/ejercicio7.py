#Imprime todas las tablas del 1 al 5.

for tabla in range(1,6):
    print("Tabla del", tabla)

    for i in range(1,11):
        print(tabla, "x", i , "=", tabla * i)

    print()
