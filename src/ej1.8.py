#Ejercicio 1.8
"""Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes."""

def sumar_tres_numero():
    num = float(input("Introduce el primer nº para su suma: "))
    num += float(input("Introduce el segundo nº para su suma: "))
    num += float(input("Introduce el tercer nº para su suma: "))

    print(f"La suma de todos es: {num:.2f}")

sumar_tres_numero()