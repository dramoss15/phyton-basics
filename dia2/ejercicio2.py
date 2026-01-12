#Pide un número e imprime su tabla del 1 al 10.

numero = int(input("Dime un número: "))
for i in range(1,11):
    print(numero, "x", i , "=", numero * i)