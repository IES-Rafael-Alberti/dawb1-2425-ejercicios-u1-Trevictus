#Ejercicio 1.2.10

"""Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética
((3+2)/(2*5))*((3+2)/(2*5))
"""

def operacionAritmetica():
    operacion = ((3+2)/(2*5))*((3+2)/(2*5))

    print("La operacion da de resultado:", operacion)


def main():
    operacionAritmetica()

if __name__ == "__main__":
    main()