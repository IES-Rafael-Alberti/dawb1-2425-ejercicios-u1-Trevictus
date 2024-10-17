#Ejercicio 1.2.17
"""Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

"""

def pregunta_nombre():
    nombre = input("Ingresa tu nombre: ")
    numero_veces = int(input("Cuantas veces se va a repetir: "))

    repeticion = (nombre + "\n") * numero_veces

    print(repeticion)


def main():
    pregunta_nombre()

if __name__ == "__main__":
    main()