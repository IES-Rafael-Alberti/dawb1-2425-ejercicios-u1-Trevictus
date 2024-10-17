#Ejercicio 1.2.7
"""Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma."""

def sumar_tres_numero():
    cont = 0
    lista = []

    while cont < 3:
        num = float(input("Introduce tres nºs para su suma: "))
        lista.append(num)
        cont += 1

    print("La suma de los tres nºs es:",sum(lista))


def main():
    sumar_tres_numero()

if __name__ == "__main__":
    main()