#Ejercicio 1.3
"""Analizar las siguientes expresiones:
ancho / alto
ancho // 2
ancho / 2
ancho * 2
ancho * alto
(5 + 1) * 3
(5 + 1) / 3
Después, mostrar el resultado y el tipo por pantalla de cada expresión para comprobar si habéis acertado.

La salida esperada es:

ancho / alto = 1.4166666666666667 y es de tipo <class 'float'>
"""

ancho = 17
alto = 12.0

print(f"Es de tipo {type(ancho/alto)}, ancho/alto da como resultado: {(ancho/alto)}")

print(f"Es de tipo {type(ancho//2)}, ancho/alto da como resultado: {(ancho//2)}")

print(f"Es de tipo {type(ancho/2)}, ancho/alto da como resultado: {(ancho/2)}")

print(f"Es de tipo {type(ancho*2)}, ancho/alto da como resultado: {(ancho*2)}")

print(f"Es de tipo {type(ancho*alto)}, ancho/alto da como resultado: {(ancho*alto)}")

print(f"Es de tipo {type((5+1)*3)}, ancho/alto da como resultado: {((5+1)*3)}")

print(f"Es de tipo {type((5+1)/3)}, ancho/alto da como resultado: {((5+1)/3)}")