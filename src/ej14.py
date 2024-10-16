#Ejercicio 1.2.14
"""Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado."""

def calcular_peso_paquete():
    peso_payaso = 0.112
    peso_muneca = 0.075

    payasos = float(input("¿Cuántos payasos a meter en el paquete a enviar?\n"))
    munecas = float(input("¿Cuántas munecas a meter en el paquete a enviar?\n"))

    total_peso = (peso_payaso * payasos) + (peso_muneca * munecas)

    print("El paquete pesará",total_peso)


def main():
    calcular_peso_paquete()

if __name__ == "__main__":
    main()