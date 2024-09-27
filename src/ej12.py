#Ejercicio 1.2.12
"""Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales."""

def pedir_peso_altura():
    peso = float(input("Introduce tu peso en kg: "))
    altura = float(input("Introduce tu altura en m: "))
    imc = peso / (altura * altura)

    print(f"Tu índice de masa corporal es:", round(imc, 2))

pedir_peso_altura()