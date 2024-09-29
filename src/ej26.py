#Ejercicio 1.2.26
"""Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

"""

def lista_compra():
    lista = input("Introduce los productos de la lista separados por , (coma): ")

    productos = lista.split(",")

    print("\n".join(map(str.strip, productos)))

lista_compra()