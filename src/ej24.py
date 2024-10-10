#Ejercicio 1.2.24
"""Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

"""

def desglosar_precio():
    precio = input("Ingresa el precio del producto con dos decimales: ")

    euros, centimos = precio.split(".")

    print(f"Son {euros}€ y {centimos}cts.")

desglosar_precio()