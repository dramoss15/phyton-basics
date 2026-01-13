agenda = {}

while True:
    nombre = input("Nombre (fin para salir): ")

    if nombre == "fin":
        break

    telefono = input("Teléfono: ")
    agenda[nombre] = telefono

print("Agenda:")
for nombre, telefono in agenda.items():
    print(nombre, "→", telefono)
