#Ejercicio 1.2.19
"""Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla "NOMBRE tiene n letras.", donde NOMBRE es el nombre de usuario en mayúsculas y n es el número de letras que tienen el nombre.

"""

def contar_nombre():
    nombre = input("Ingresa tu nombre: ")
    n = len(nombre)
    print(f"{nombre.upper()} tiene {n} letras.")

contar_nombre()