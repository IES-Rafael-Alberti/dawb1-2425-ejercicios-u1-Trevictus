#Ejercicio 1.2.21
"""Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

"""

def pedir_frase():
    frase = input("Ingresa tu frase favorita: ")
    separa_palabras = frase.split()
    frase_reves = separa_palabras[::-1]

    frase_invertida = " ".join(frase_reves)

    print(frase_invertida)

pedir_frase()