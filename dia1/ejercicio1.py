#Pide el nombre y edad y di si puede votar

nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cúantos años tienes? "))

if edad >= 18 :
    print(nombre, "puedes votar")
else: 
    print(nombre, "no puedes votar")