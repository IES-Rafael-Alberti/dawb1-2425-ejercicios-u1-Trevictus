#Ejercicio 1.28
"""Realiza un programa en Python que lea dos números enteros, muestre cuál es el menor de los dos y cuántos números existen entre ellos dos.

El segundo número no puede ser igual, si es así, debe mostrar el error: "Los números no pueden ser iguales".
Si los números son diferentes, por ejemplo, 5 y 12, debe mostrar la frase: "El número menor es el 5 y entre ellos existen 7 números enteros"."""

def distancia_numeros(num1: int, num2: int) -> tuple:
   
    while num1 == num2:
        num1 = int(input("Error. Los dos nºs no pueden ser iguales. Vuelve a introducir el 1º: "))
        num2 = int(input("Vuelve a introducir el 2º: "))

    if num1 < num2:
        menor = num1
    if num2 < num1:
        menor = num2
    #elif num1 == num2:
    #    print("Error. Los dos nºs no pueden ser iguales.")
    distancia = abs(num1 - num2) - 1

    return menor, distancia

num1 = int(input("Introduce un nº: "))
num2 = int(input("Introduce el segundo nº: "))

menor, distancia = distancia_numeros(num1, num2)

print(f"El nº menor es {menor} y la distancia entre los dos es {distancia}")
