#Ejercicio 1.2.5
"""Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo."""

def calcular_con_iva():

    importesiniva = float(input("Introduzca el inmporte sin IVA: "))
    iva = float(input("Introduzca el IVA a aplicar: "))

    print(((importesiniva /100) * iva) + importesiniva)


def main():
    calcular_con_iva()

if __name__ == "__main__":
    main()