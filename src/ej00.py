import os
import ej01, ej02, ej03, ej04,ej05,ej06,ej07,ej08,ej09,ej10,ej11,ej12,ej13,ej14,ej15,ej16,ej17,ej18,ej19,ej20,ej21,ej22,ej23,ej24,ej25,ej26,ej27,ej28,ej29,ej30

lista_aceptar = ["s", "si", "S", "SI", "y", "YES", "Y", "yes"]

def intro():
    print("Bienvenido a la unidad 1!")


def llamar_app():
        # La variable ejercicio inicializaa a valor limpio
    ejercicio = 0

    while ejercicio < 1 or ejercicio > 30:
    # Crea un bucle para que pida un número que sea aceptado
        ejercicio = int(input("Introduce el nº del programa: "))

        if ejercicio < 1 or ejercicio > 30:
            print("**ERROR** Solo existen programas del 1 al 7.")
        if ejercicio == 1:
            print("ej01: Saludo")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej01.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 2:
            print("ej02: Calcular salario")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej02.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                
        elif ejercicio == 3:
            print("ej03: Calcular")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej03.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 4:
            print("ej04: Medir Farenheits")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej04.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 5:
            print("ej05: Calcular IVA")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej05.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 6:
            print("ej06: Calcular IVA 2")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej06.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 7:
            print("ej07: Suma de tres dígitos")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej07.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 8:
            print("ej08: Suma de tres dígitos con dos variables")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej08.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 9:
            print("ej09: Suma de tres dígitos sin variables")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej09.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 10:
            print("ej10: Operación aritmética")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej10.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 11:
            print("ej11: Suma de los primeros enteros")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej11.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 12:
            print("ej12: Calcular imc")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej12.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 13:
            print("ej13: Cociente y resto")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej13.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 14:
            print("ej14: Calcular peso de paquetes")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej14.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 15:
            print("ej15: Calcular depositos")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej15.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 16:
            print("ej16: Calcular precio pan")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej16.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 17:
            print("ej17: Repetir nombre")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej17.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 18:
            print("ej18: Mayúsculas y minúsculas")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej18.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 19:
            print("ej19: Contar letras de nombre")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej19.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 20:
            print("ej20: Prefijo y extensión")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej20.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 21:
            print("ej21: Frase invertida")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej21.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 22:
            print("ej22: Vocales en mayúsculas")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej22.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 23:
            print("ej23: Dominio ceu.es")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej23.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 24:
            print("ej24: Desglosar precio")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej24.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 25:
            print("ej25: Fecha con formato")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej25.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 26:
            print("ej26: Lista de la compra")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej26.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 27:
            print("ej27: Definir producto")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej27.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 28:
            print("ej28: Distancia entre dígitos")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej28.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 29:
            print("ej29: Definir edad")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej29.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')

        elif ejercicio == 30:
            print("ej30: Cadena con incremento")
            ejecutar = input("¿Desea ejecutar el programa?")
            if ejecutar in lista_aceptar:
                ej30.main()
            else:
                ejercicio = 0
                os.system('cls' if os.name == 'nt' else 'clear')   
        # Crea un bucle para que pida un número que sea aceptado
        

def main():
    intro()
    llamar_app()




if __name__ == "__main__":
    main()
