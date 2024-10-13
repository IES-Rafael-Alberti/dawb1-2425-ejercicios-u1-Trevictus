#Ejercicio 1.2.22
"""Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

"""

def pedir_frase_y_vocal():
    frase = input("Escribe tu frase favorit: ")
    vocal = input("Escoge la vocal a poner en mayusculas: ")

    vocal = vocal.lower()
    vocal_may = vocal.upper()
    letra_cambiada = str.maketrans(vocal, vocal_may)
    frase_cambiada = frase.translate(letra_cambiada)

    print(frase_cambiada)


def main():
    pedir_frase_y_vocal()

if __name__ == "__main__":
    main()