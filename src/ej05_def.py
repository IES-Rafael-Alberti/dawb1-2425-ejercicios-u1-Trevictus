#  - ej05 => recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.


def calcular_con_iva(importe_sin_iva, iva):

    print("El precio final del articulo es:",((importe_sin_iva /100) * iva) + importe_sin_iva)


def main():
    importe_sin_iva = float(input("Introduzca el inmporte sin IVA: "))
    iva = float(input("Introduzca el IVA a aplicar: "))
    calcular_con_iva(importe_sin_iva,iva)


if __name__ == "__main__":
    main()