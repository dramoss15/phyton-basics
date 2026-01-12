#Pide nombres hasta escribir "fin"
#Guarda los nombres en una lista
#Muéstralos al final

nombres = []

while True:
    nombre = input("Ingresa un nombre (fin para salir): ")

    if nombre == "fin":
        break

    nombres.append(nombre)

print("Nombres ingresados:")
for n in nombres:
    print(n)
