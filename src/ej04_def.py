#  - ej04 => NO recibe parámetros y retorna una cadena de caracteres con la temperatura convertida en grados Celsius y entre parántesis la temperatura en grados farenheit... ambas temperaturas con 2 posiciones decimales. Por ejemplo, si introduce 212 debe retornar la cadena "100.00ºC (212.00ºF)". Dentro de la función se pedirá al usuario los grados Farenheit.


def conversion_celsius():
    farenheits = float(input("Introduce que tempratura hace en gº Farenheits, redondeado a dos decimales: "))
    celsius = (farenheits - 32) * (5 / 9)

    return "La temperatura en Celsius es {:.2f}ºC ({:.2f})".format(celsius, farenheits)

def main():
    print(conversion_celsius())

if __name__ == "__main__":
    main()