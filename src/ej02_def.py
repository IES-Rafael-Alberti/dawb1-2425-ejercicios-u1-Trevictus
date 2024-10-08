#  - ej02 => recibe horas y coste y retorna el importe total.


def calcular_salario(horas, precio_hora):
    return round(horas * precio_hora, 2)

def main():
    horas = float(input("Introduce las horas trabajadas: "))
    precio_hora = float(input("Introduce la cuantía que ganas por hora: "))
    total = horas * precio_hora
    print(total)


if __name__ == "__main__":
    main()