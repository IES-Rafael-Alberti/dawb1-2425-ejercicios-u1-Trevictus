#  - ej02 => recibe horas y coste y retorna el importe total.


def calcular_salario(horas, precio_hora):
    return horas * precio_hora

def main():
    horas = float(input("Introduce las horas trabajadas: "))
    precio_hora = float(input("Introduce la cuantía que ganas por hora: "))
    print(calcular_salario(horas, precio_hora))


if __name__ == "__main__":
    main()