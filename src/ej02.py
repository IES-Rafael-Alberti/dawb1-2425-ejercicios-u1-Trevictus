#Ejercicio 1.2.2
"""Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.

Horas de trabajo: 6
Coste por hora: 10
Importe total: 60"""

def calcular_horas():

    horas = float(input("Introduce las horas trabajadas: "))
    preciohora = float(input("Introduce la cuantía que ganas por hora: "))

    print(horas * preciohora)

calcular_horas()