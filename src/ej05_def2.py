def calcular_con_iva(importe_sin_iva, iva):
    if iva < 0 or iva >100:
        iva = 21
    precio_final = (importe_sin_iva /100) * iva + importe_sin_iva
    return f"El precio final del artículo con IVA {iva:.2f} es {precio_final:.2f}€"
     

def main():
    importe_sin_iva = float(input("Introduzca el inmporte sin IVA: "))
    iva = float(input("Introduzca el IVA a aplicar: "))
    print(calcular_con_iva(importe_sin_iva,iva))


if __name__ == "__main__":
    main()