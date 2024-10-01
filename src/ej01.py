#Ejercicio 1.2.1
"""Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.

Escribe tu nombre: Juan
Hola, Juan.
"""


def saludar(nombre:str)->str:
    print(f"Hola, {nombre}")

def main():
    saludar(input("Escribe tu nombre: "))

if __name__ == "__main__":
    main()