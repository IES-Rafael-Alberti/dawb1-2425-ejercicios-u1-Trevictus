#Pide un nº entero: "hola", 4
#Has introducido 4
#Error eso no es un entero
#while: def comprobar_entero(cadena) -> bool.............dame_numero()-> int y esta debe llamar a comprobar_entero.
#if

def dame_numero()->int:
    cadena = input("Ingresa un nº entero: ")#.strip()

    while not comprobar_numero(cadena):
        cadena = input("Error. Eso no es un nº entero.\nIngresa un nº entero: ")

    return int(cadena)


def comprobar_numero(cadena: str):
    cadena = cadena.strip()

    return cadena.isdigit() or (cadena.startswith("-") and cadena[1:].isdigit())


def main():
    num = dame_numero()
    print(f"Has introducido el nº {num}")

if __name__ == "__main__":
    main()