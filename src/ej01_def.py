#  - ej01 => recibe un nombre y retorna una cadena de caracteres con el resultado.



def saludar(nombre):
    return f"Hola, {nombre}"

def main():
    mi_amigo = input("Ingresa tu nombre: ")

    print(saludar(mi_amigo))


if __name__ == "__main__":
    main()