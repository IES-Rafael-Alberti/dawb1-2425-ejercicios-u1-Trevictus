#Ejercicio 1.2.16
"""Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.

"""

def precios_barra():
    BARRA: float = 3.49
    DESCUENTO = 0.6

    barras_ayer_vendidas = int(input("¿Cuántas barras de ayer has vendido?\n"))

    print(f"La barra de hoy sale a un precio de {BARRA}€, si has comprado {barras_ayer_vendidas} barra/s de ayer, recibes un descuento de {DESCUENTO}€ por cada una y el coste total sale a unos {barras_ayer_vendidas * (BARRA * DESCUENTO)}€")


def main():
    precios_barra()

if __name__ == "__main__":
    main()