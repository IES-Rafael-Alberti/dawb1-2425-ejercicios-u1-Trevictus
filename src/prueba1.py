def retornar_mayor(num1,num2):
    if num1 == num2:
        return 0
    if num1 < num2:
        return num2
    else:
        return num1



def main():
    num1 = input("Introduce un nº: ")
    num2 = input("Introduce otro: ")
    retornar_mayor(num1,num2)
    print("El nº mayor es",retornar_mayor(num1,num2))

if __name__ == "__main__":
    main()