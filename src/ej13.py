#Ejercicio 1.2.13
"""Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS: "la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por el usuario, y c y r son el cociente y el resto de la división entera respectivamente."""

def cociente_resto():
    n = float(input("Ingresa un nº: "))
    m = float(input("Ingresa otro nº: "))
    c = n // m
    r = n % m

    print(f"De la division entre {n} y {m} se obtiene el cociente {c} y el resto {r}.")

cociente_resto()