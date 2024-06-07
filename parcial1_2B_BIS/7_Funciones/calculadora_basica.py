import os

# from varias_funciones import *     (Esto importara todas las funciones del archivo)
from varias_funciones import esperaTecla, solicitarDatos, getCalculadora   #Esto importara las funciones indicadas


# def solicitarDatos():
#     print("\n")
#     global n1,n2,ope    #Funcion global es pa mandarla globnalñlsdsd
#     n1=int(input("Numero 1:"))
#     n2=int(input("Numero 2:"))


# def getCalculadora(num1,num2,operacion):
#     if operacion=="1" or operacion=="+" or operacion=="SUMA":
#         return f"{num1}+{num2}={int(num1)+int(num2)}"
        
#     elif operacion=="2" or operacion=="-" or operacion=="RESTA":
#         return f"{num1}+{num2}={int(num1)-int(num2)}"
        
#     elif operacion=="3" or operacion=="X" or operacion=="MULTIPLICACION":
#         return f"{num1}+{num2}={int(num1)*int(num2)}"
        
#     elif operacion=="4" or operacion=="/" or operacion=="DIVISION":
#         return f"{num1}+{num2}={int(num1)/int(num2)}"
#     else:
#         return "Opcion invalida"

    # def esperaTecla():
    #     print("Presione cualquier tecla para continuar")

opcion=True
while opcion:
    print ("\n..::: CALCULADORA BASICA:::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- Division \n 5.- SALIR")
    opcion=input("\t Elegir una opcion: ").upper()

    if opcion!="5":
        n1,n2=solicitarDatos()
        print(getCalculadora(n1,n2,opcion))
        esperaTecla()
        os.system("cls")
    else:
        opcion=False
        print("Gracias por utilizar la calculadora")

