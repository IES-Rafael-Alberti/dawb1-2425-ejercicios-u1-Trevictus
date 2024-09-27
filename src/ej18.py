#Ejercicio 1.2.18
"""Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

"""

def cambiar_nombre():
    nombre = str(input("Ingresa tu nombre completo: "))

    repeticion1: str = (nombre.lower)
    repeticion2: str = (nombre.capitalize)
    repeticion3:str = (nombre.upper)

    print(repeticion1,repeticion2,repeticion3)

cambiar_nombre()