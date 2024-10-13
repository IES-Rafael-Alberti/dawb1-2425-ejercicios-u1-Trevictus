#Ejercicio 1.2.9
"""¿Es posible escribir el programa del ejercicio 1.7 sin usar variables? Inténtalo."""

def sumar_tres_numero():
    print("Se sumarán los tres nºs: ", float(input( "Introduce el primero: "))+ float(input( "Introduce el segundo: ")) + float(input( "Introduce el tercero: ")))


def main():
    sumar_tres_numero()

if __name__ == "__main__":
    main()