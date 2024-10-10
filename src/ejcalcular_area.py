import math

def pedir_lados(mensaje: str):
    valor = input(mensaje).strip().replace(",",".")

    valor.startswith("-")

    while comprobar_float(valor) == False:
        print ("**ERROR** Nº inválido!")
        valor = input(mensaje).strip().replace(",",".")

    return float(valor)

def comprobar_float(valor: str)->bool:
    if valor.startswith("-"):
        valor = valor[1:]

    pos_punto = valor.find(".")

    if pos_punto >=0:
        valor = valor[:pos_punto] + valor[pos_punto + 1:]

    return valor.isdigit()


def comprobar_triangulo(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)



def calcular_area(a: float, b: float, c: float) ->float:
    semiperimetro = (a + b +c) / 2
    #area = (semiperimetro * (semiperimetro - a) * semiperimetro * (semiperimetro - b) * semiperimetro * (semiperimetro - c))/(semiperimetro * (semiperimetro - a) * semiperimetro * (semiperimetro - b) * semiperimetro * (semiperimetro - c))
    area = math.sqrt(semiperimetro * (semiperimetro - a) * semiperimetro * (semiperimetro - b) * semiperimetro * (semiperimetro - c))

    return area


def main():
    a = pedir_lados("Introduce el valor del 1er lado: ")
    b = pedir_lados("Introduce el valor del 2º lado: ")
    c = pedir_lados("Introduce el valor del 3er lado: ")
    
    if comprobar_triangulo(a, b, c) == True:
        area = calcular_area(a, b, c)
        print(area)
    else:
        print("El triangulo no es válido!")

    




if __name__ == "__main__":
    main()