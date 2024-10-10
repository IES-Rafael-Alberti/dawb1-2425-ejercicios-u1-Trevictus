#Ejercicio 1.5
"""Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

Calcula el interés: capital * (1 + interes)"""

def calcular_deposito():
    deposito = float(input("Cantidad a ingresar: "))
    interes = 0.04

    calculoanio1 = deposito * (1 + interes)
    calculoanio2 = (calculoanio1 * (1 + interes))
    calculoanio3 = (calculoanio2 * (1 + interes))


    print(f"La cantidad asciende a {calculoanio1:.2f} el primer año, a {calculoanio2:.2f} el 2º y a {calculoanio3:.2f}")

calcular_deposito()