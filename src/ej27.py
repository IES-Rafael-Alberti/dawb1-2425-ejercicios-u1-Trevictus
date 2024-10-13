#Ejercicio 1.2.27
"""
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""

def definir_producto():
    nombre = input("Ingresa el nombre del producto: ")
    precio = float(input("Ingresa el coste del producto: "))
    unidades = int(input("Ingresa el nº de unidades del producto: "))

    total = precio * unidades

    print(f"Producto {nombre}, con un precio de {precio:09.2f}€ siendo {unidades:03d} unidades con un coste total de {total:011.2f}€")


def main():
    definir_producto()

if __name__ == "__main__":
    main()