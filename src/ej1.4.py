#Ejercicio 1.4
"""
Formatear la salida de los grados Farenheit a dos posiciones decimales.
Mostrar en pantalla:

La temperatura en grados Farenheit es 0.00ºF (0.00ºC)
"""

celsius = float(input("Introduce que tempratura hace n gº Celsius: "))

farenheits = celsius * 1.8 +32

print(f"La temperatura en Farenheits es {farenheits:.2f}")