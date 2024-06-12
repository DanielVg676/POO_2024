#  4.- 

#  Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#   y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

import os
os.system("cls")

lista=[10,20,30,40,50]
cadena="Esta es una cadena de texto"
numero=33
valor=True

def tipo(variable):
    if isinstance(variable, list):
        print("La variable es una lista.")
    elif isinstance(variable, str):
        print("La variable es una cadena.")
    elif isinstance(variable, int):
        print("La variable es un entero.")
    elif isinstance(variable, bool):
        print("La variable es un lógico.")
    else:
        print("La variable es de un tipo desconocido.")

tipo(lista)
tipo(cadena)
tipo(numero)
tipo(valor)
