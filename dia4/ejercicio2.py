notas = {
    "Matemática": 15,
    "Programación": 18,
    "Física": 14
}

suma = 0
for nota in notas.values():
    suma += nota

promedio = suma / len(notas)
print("Promedio:", promedio)
