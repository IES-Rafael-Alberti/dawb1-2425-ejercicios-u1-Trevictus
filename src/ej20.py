#Ejercicio 1.2.20
"""Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

"""

def telefono():
    numero_tlf = str(input("Ingresa el nº de tlf con el prefifo +34 y la extension 56 separados por '-': "))
    
    print((numero_tlf.replace("+34-","").replace("-56", "")))

telefono()