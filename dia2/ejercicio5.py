#Pide números hasta que el usuario escriba 0
#Muestra la suma total.

suma = 0
while True:
    num = int(input("Ingrese un número: "))
    if num == 0:
        break

    suma += num 

print("La suma es: ", suma)
        