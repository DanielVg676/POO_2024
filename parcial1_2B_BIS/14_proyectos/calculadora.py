import os
from funciones import esperaTecla, solicitarDatos, getCalculadora, solicitardatos2

opcion = True
while opcion:
    print("\n..::: CALCULADORA BASICA:::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- Division \n 5.- Potencia \n 6.- Raiz \n 7.- SALIR")
    opcion = input("\t Elegir una opcion: ").upper()

    if opcion != "7":
        if opcion == "6":
            n1, n2 = solicitardatos2()
            print(getCalculadora(n1, n2, opcion))
            esperaTecla()
            os.system("cls")
        else:
            n1, n2 = solicitarDatos()
            print(getCalculadora(n1, n2, opcion))
            esperaTecla()
            os.system("cls")
    else:
        opcion = False
        print("Gracias por utilizar la calculadora")