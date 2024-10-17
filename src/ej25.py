#Ejercicio 1.2.25
"""Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

"""

def mostrar_fecha():
    fecha = (input("Ingresa tu fecha de nacimiento en el formato dd/mm/aaaa: "))

    dia, mes, anio = fecha.split("/")

    print(f"Nació un {dia} del mes {mes} del año {anio}.")

def main():
    mostrar_fecha()

if __name__ == "__main__":
    main()