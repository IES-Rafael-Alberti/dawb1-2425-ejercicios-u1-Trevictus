def conversion_celsius():
    farenheits = float(input("Introduce que tempratura hace n gº Celsius: "))
    celsius = (farenheits - 32) * (5 / 9)

    return "La temperatura en Celsius es {:.2f}ºC ({:.2f})".format(celsius, farenheits)

def main():
    print(conversion_celsius())

if __name__ == "__main__":
    main()