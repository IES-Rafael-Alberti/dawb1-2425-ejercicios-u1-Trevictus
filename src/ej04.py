#Ejercicio 1.2.4
"""Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida."""

def calcular_farenheits():
    celsius = float(input("Introduce que tempratura hace n gº Celsius: "))

    farenheits = celsius * 1.8 +32

    print("La temperatura en Farenheits es", farenheits)

calcular_farenheits()