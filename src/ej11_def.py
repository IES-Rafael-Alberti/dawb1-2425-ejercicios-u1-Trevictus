#- ej11 => recibe un número y retorna una cadena de caracteres con el resultado de la función.

def suma_primeros_enteros(num):
    suma = ((num * (num + 1))/2)
    return suma


def main():
    num = int(input("Ingresa el nº elegido: "))
    suma = suma_primeros_enteros(num)

    print(f"La suma de los primeros {num} enteros es: {suma}")

if __name__ == "__main__":
    main()