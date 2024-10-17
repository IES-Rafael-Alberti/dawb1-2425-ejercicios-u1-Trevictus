#Ejercicio 1.7
"""Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma.
"""
def solicitar_tres_numero():
    num1 = float(input("Ingresa el 1er nº: "))
    num2 = float(input("Ingresa el 2º nº: "))
    num3 = float(input("Ingresa el 3er nº: "))

    suma = num1 + num2 + num3

    print(f"La suma de estos tres nºs introducidos es: {suma:.2f}")

solicitar_tres_numero()