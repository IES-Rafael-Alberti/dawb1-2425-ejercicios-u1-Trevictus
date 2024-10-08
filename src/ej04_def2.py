def conversion_celsius():
    farenheits = round(float(input("Introduce que tempratura hace en gº Farenheits, redondeado a dos decimales: ")),2)
    celsius = (farenheits - 32) * (5 / 9)

    return "La temperatura en Celsius es {:.2f}ºC ({:.2f})".format(celsius, farenheits)

def main():
    print(conversion_celsius())

if __name__ == "__main__":
    main()