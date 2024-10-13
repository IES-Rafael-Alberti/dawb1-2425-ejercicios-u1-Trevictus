import os
import ej01, ej02, ej03, ej04,ej05,ej06,ej07,ej08,ej09,ej10,ej11,ej12,ej13,ej14,ej15,ej16,ej17,ej18,ej19,ej20,ej21,ej22,ej23,ej24,ej25,ej26,ej27,ej28,ej29,ej30

lista_aceptar = ["s", "si", "S", "SI", "y", "YES", "Y", "yes"]

def intro():
    print("Bienvenido a la unidad 1!")


def llamar_app(ejercicio):
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
            ej02.main()
        elif ejercicio == 3:
            print("ej03: Calcular")
            ej03.main()
        elif ejercicio == 4:
            ej04.main()
        elif ejercicio == 5:
            ej05.main()
        elif ejercicio == 6:
            ej06.main()
        elif ejercicio == 7:
            ej07.main()
        elif ejercicio == 8:
            ej08.main()
        elif ejercicio == 9:
            ej09.main()
        elif ejercicio == 10:
            ej10.main()
        elif ejercicio == 11:
            ej11.main()
        elif ejercicio == 12:
            ej12.main()
        elif ejercicio == 13:
            ej13.main()
        elif ejercicio == 14:
            ej14.main()
        elif ejercicio == 15:
            ej15.main()
        elif ejercicio == 16:
            ej16.main()
        elif ejercicio == 17:
            ej17.main()
        elif ejercicio == 18:
            ej18.main()
        elif ejercicio == 19:
            ej19.main()
        elif ejercicio == 20:
            ej20.main()
        elif ejercicio == 21:
            ej21.main()
        elif ejercicio == 22:
            ej22.main()
        elif ejercicio == 23:
            ej23.main()
        elif ejercicio == 24:
            ej24.main()
        elif ejercicio == 25:
            ej25.main()
        elif ejercicio == 26:
            ej26.main()
        elif ejercicio == 27:
            ej27.main()
        elif ejercicio == 28:
            ej28.main()
        elif ejercicio == 29:
            ej29.main()
        elif ejercicio == 30:
            ej30.main()   
        # Crea un bucle para que pida un número que sea aceptado
        

def main():
    intro()
    llamar_app()




if __name__ == "__main__":
    main()
