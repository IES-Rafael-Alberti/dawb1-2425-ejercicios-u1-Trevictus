#Ejercicio 1.2.6
"""Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%)."""

def calcular_iva():
    total = float(input("Introduzca el valor total del artículo: "))
    iva = 0.10
    ivapagado = total * 0.1
    importesiniva = total - ivapagado

    print(f"El total con iva es {total}€.\nSuponiendo que has pagado un 10% de IVA la cuota de IVA asciende a {ivapagado}€.\nEl importe del artículo sin el IVA es de {importesiniva}€")
calcular_iva()