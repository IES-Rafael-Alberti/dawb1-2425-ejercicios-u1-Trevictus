def convertir_binario(valor, base):
    cociente = valor
    resultado = ""
    while cociente >= base:
        resto = cociente % base
        resultado += str(resto)
        cociente = cociente // base

    resultado += str(cociente)
    resultado = resultado[:-1]
    return resultado

def main():
    valor = int(input("Introduce un nº: "))
    print(convertir_binario(valor,))

if __name__ == "__main__":
    main()