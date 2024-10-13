#Ejercicio 1.2.23
"""Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

"""

def pedir_correo():
    correo = input("Ingresa tu email: ")

    nombre, dominio = correo.split("@")
    nuevo_dominio = nombre + "@ceu.es"

    print(nuevo_dominio)

def main():
    pedir_correo()

if __name__ == "__main__":
    main()