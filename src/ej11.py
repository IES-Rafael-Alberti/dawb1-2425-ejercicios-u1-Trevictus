#Ejercicio 1.2.11
"""Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:

"""

def suma_primeros_enteros():
    num = int(input("Ingresa el nº elegido: "))
    suma = ((num * (num + 1))/2)
    
    print(f"La suma de los primeros {num} enteros es: {suma}")


def main():
    suma_primeros_enteros()

if __name__ == "__main__":
    main()