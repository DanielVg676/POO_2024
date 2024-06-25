   # Ejemplo #5 Crear un programa que permita gestionar (administrar) peliculas, colocar un mennu
    # de opciones para agregar, remover, consultar peliculas.

    #Notas
    # 1.- Utilizar funciones y mandar llamar desde otro archivo
    # 2.- Utilizar listas para almacenar los nomnbres de peliculas

from funciones import esperaTecla, esperaTecla2, insertarPelicula, removerPelicula, actualizarLista, consultarPelicula, vaciar, actualizar
import os

bucle=True
while bucle:
    print("\n..::: BLOCKBUSTER :::... \n 1.-Agregar peliculas \n 2.-Eliminar \n 3.-Buscar \n 4.-Consultar \n 5.-Vaciar \n 6.-Actualizar \n 7.-Salir")
    opcion=input("Ingrese la opcion que desee: ").upper()

    if opcion=="1":
        os.system("cls")
        insertarPelicula()
    elif opcion=="2":
        os.system("cls")
        removerPelicula()
    elif opcion=="3":
        os.system("cls")
        consultarPelicula()
    elif opcion=="4":
        os.system("cls")
        actualizarLista()
    elif opcion=="5":
        vaciar()
        esperaTecla()
        os.system("cls")
    elif opcion=="6":
        os.system("cls")
        actualizar()
    elif opcion == "7":
        os.system("cls")
        print("..:::  VUELVA PRONTO  :::..")
        bucle=False
    else:
        print("Opcion invalida, porfavor ingrese una opcion valida")
        esperaTecla2()