def conversion_celsius(farenheits):
    celsius = (farenheits - 32) * (5 / 9)

    return "La temperatura en Celsius es {:.2f}ºC ({:.2f})".format(celsius, farenheits)

def main():
    farenheits = float(input("Introduce que tempratura hace en gº Farenheits, redondeado a dos decimales: "))
    print(conversion_celsius(farenheits))

if __name__ == "__main__":
    main()