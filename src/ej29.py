#Ejercicio 1.29
"""Realiza un programa en Python que solicite un nombre y una edad.

Si el nombre está vacío, debes utilizar el valor "Desconocido". La edad debe pedirse hasta que introduzca una edad comprendida entre 0 y 125 años.
El programa mostrará la siguiente frase: "Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir"."""

def solicitar_informacion():
    nombre = input("Ingresa tu nombre: ") 
    edad = float(input("Ingresa tu edad: "))

    while edad < 0 or edad > 125:
        edad = float(input("Error. La edad debe estar comprendida entre 0 y 125 años. vuelve a ingresarla: "))

    if nombre == "":
        nombre = "Desconocido"

    anios_restantes = 125 - edad

    print(f"Te llamas {nombre} y tienes {edad} años, te quedan {anios_restantes} años por cumplir.")

solicitar_informacion()