import os

def solicitarDatos():
    print("\n")
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    return n1, n2

def solicitardatos2():
    print("\n")
    n1 = int(input("Ingrese el numero que desee la raiz: "))
    n2 = int(input("Ingrese el índice de la raíz: "))
    return n1, n2

def getCalculadora(num1, num2, operacion):
    if operacion == "1" or operacion == "+" or operacion == "SUMA":
        return f"{num1} + {num2} = {int(num1) + int(num2)}"
        
    elif operacion == "2" or operacion == "-" or operacion == "RESTA":
        return f"{num1} - {num2} = {int(num1) - int(num2)}"
        
    elif operacion == "3" or operacion == "X" or operacion == "MULTIPLICACION":
        return f"{num1} * {num2} = {int(num1) * int(num2)}"
        
    elif operacion == "4" or operacion == "/" or operacion == "DIVISION":
        if int(num2) == 0:
            return "Error: División por cero."
        return f"{num1} / {num2} = {int(num1) / int(num2)}"
    
    elif operacion == "5" or operacion == "^" or operacion == "POTENCIA":
        resultado = 1
        i = 0
        while i < num2:
            resultado *= num1
            i += 1
        return f"Potencia de {num1} a la {num2} es igual a {resultado}"
    
    elif operacion == "6" or operacion == "√" or operacion == "RAIZ":
        if num2 <= 0:
            return "El índice de la raíz debe ser un número positivo."
        resultado = num1 ** (1 / num2)
        return f"Raíz {num2}-ésima de {num1} es igual a {resultado}"
    else:
        return "Opción inválida"

def esperaTecla():
    print("Presione cualquier tecla para continuar...")
    input()




peliculas=["Sirenita","Rey leon","Titanic","Matrix","Spiderman"]

def esperaTecla2():
        print("Presione cualquier tecla para continuar")
        input()
        os.system("cls")

def insertarPelicula():
    pelicula=input("Ingrese el nombre de la pelicula a agregar: ")
    peliculas.append(pelicula)
    print(f"La pelicula {pelicula} ha sido ingresada en el sistema")
    esperaTecla()

def removerPelicula():
    bucle=True
    while bucle:
        pelicula=input("Ingrese el nombre de la pelicula a eliminar exactamente como esta en el sistema: ")
        if pelicula in peliculas:
            peliculas.remove(pelicula)
            print(f"La pelicula {pelicula} ha sido eliminada correctamente")
            esperaTecla()
            bucle=False
        else:
            print(f"La pelicula {pelicula} no se encuentra en el sistema")
            esperaTecla()
            continuar = input("Desea intentar de nuevo? SI/NO ").upper()
            if continuar in ["SI", "S"]:
                bucle=True
            else:
                bucle=False
                os.system("cls")

def actualizarLista():
    print("Las peliculas en stock son: ")
    print(peliculas)
    esperaTecla()
    
def consultarPelicula():
    pelicula = input("Dame la película a buscar: ").strip().lower()
    noencontre = True

    for i in range(len(peliculas)):
        if pelicula == peliculas[i].strip().lower():
            print(f"La película '{peliculas[i]}' sí está disponible")
            continuar = input("Desea eliminar esta pelicula? SI/NO ").upper()
            if continuar in ["SI", "S"]:
                peliculas.remove(pelicula)
                print(f"Se ha removido la pelicula {pelicula} del sistema")
            noencontre = False
            break 
    if noencontre:
        print(f"No se encuentra la película {pelicula}")
    esperaTecla()
        
def vaciar():
    peliculas.clear
    print("Se ha limpiado el sistema")

def actualizar():
    bucle = True
    while bucle:
        print("Películas en el sistema:")
        for i, pelicula in enumerate(peliculas, start=1):
            print(f"{i}. {pelicula}")

        try:
            seleccion = int(input("Seleccione el número de la película que desea editar: "))
            if 1 <= seleccion <= len(peliculas):
                nueva_pelicula = input(f"Ingrese el nuevo nombre para la película '{peliculas[seleccion - 1]}': ").strip()
                if nueva_pelicula:
                    peliculas[seleccion - 1] = nueva_pelicula
                    print(f"La película ha sido actualizada a '{nueva_pelicula}'")
                    bucle = False
                else:
                    print("El nombre de la película no puede estar vacío.")
            else:
                print("Selección no válida. Por favor, ingrese un número de la lista.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
        esperaTecla2()

