#Ejercicio 1.30 
"""Realiza un programa en Python que pida un número de inicio, un incremento y un total de la serie.

El incremento y el total deben ser mayores que cero. Si no es así, el programa debe finalizar con un error o obligar a que introduzcan un valor correcto para ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes).
Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10"""

def serie_numeros():
    inicio = int(input("Introduce el nº de inicio de la serie: "))
    incremento = int(input("Introduce de cuanto en cuanto aumentará la serie: "))
    total = int(input("Introduce el total de la serie: "))

    while incremento < 1:
        incremento = int(input("Error. El nº debe ser entero positivo. ingresaló de nuevo: "))

    while total < 1:
        total = int(input("Error. Ingresa un valor entero positivo para el total de la serie: "))

    serie = []
    for i in range(total):
        serie.append(inicio + i * incremento)

    print("SERIE=>".join(str(inicio)))

def main():
    serie_numeros()

if __name__ == "__main__":
    main()