

def solicitarDatos():
    print("\n")
    global n1,n2,ope    #Funcion global es pa mandarla globnalñlsdsd
    n1=int(input("Numero 1:"))
    n2=int(input("Numero 2:"))
    ope=input("Operacion: ").upper()
    return n1,n2,ope   #Esto es para mandar al global las locales y 


def getCalculadora(num1,num2,operacion):
    if operacion=="1" or operacion=="+" or operacion=="SUMA":
        resultado=f"{num1}+{num2}={int(num1)+int(num2)}"
        
    elif operacion=="2" or operacion=="-" or operacion=="RESTA":
        resultado=f"{num1}+{num2}={int(num1)-int(num2)}"
        
    elif operacion=="3" or operacion=="X" or operacion=="MULTIPLICACION":
        resultado=f"{num1}+{num2}={int(num1)*int(num2)}"
        
    elif operacion=="4" or operacion=="/" or operacion=="DIVISION":
        resultado=f"{num1}+{num2}={int(num1)/int(num2)}"
    return resultado

print ("\n..::: CALCULADORA BASICA:::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- Division \n 5.- SALIR")
opcion=input("\t Elegir una opcion: ").upper()
n1,n2,ope=solicitarDatos()  #Hay que asignar valores al regresar las variavles locales
print(getCalculadora(n1, n2, ope))
