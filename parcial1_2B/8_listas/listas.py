"""
List (array)
Son collecciones o conjuntos de datos/valores bajo
un mismo nombre, para acceder a los valores, se
hace con un indice numerico

Notas: sus valores si son modificables

La lista es una coleccion ordenada y modificable, permite miembros duplicados.

Las listas son dinamicas y puede ser modificada y agrandarse

El tamaño de la lista puede ser definido. puede ser 0 o 1

python define a las listas, diccionarios, tuplas, etc como un tipo de datos, datos estructurados
"""
import os
os.system("cls")
# Ejemplo 1: crear una lista con datos numericos e imprimir el contenido

# lista=[23, 34]
# print(lista)
# # recorrer la lista con el for
# for i in lista:
#     print(i)


# Recorrer la lista con el while
# i=0
# while i <=len(lista)-1:
#     print(lista[i])
#     i+=1

# Ejemplo #2 Crear una lista de 4 palabras, solicitar una palabra y buscar la coincidencia
# en la lista e indicar si la encontro o no y en que posicion


# Mi metodo
# os.system("cls")

# palabras=["Hola", "2024", "Bye", "UTD"]

# palabra_buscar=input("Dame la palabra buscar: ")

# for i in palabras:
#     if palabra_buscar == i:
#         os.system("cls")
#         print (f"Si se encuentra su palabra")
#         break
#     else:
#         os.system("cls")
#         print(f"Su palabra no se encuentra en la lista")


os.system("cls")

# palabras=["Hola", "2024", "Bye", "UTD"]

# palabra_buscar=input("Dame la palabra buscar: ")

# noencontre=True
# for i in palabras:
#     if palabra_buscar == i:
#         print(f"Encontre la palabra {i}, en la posicion: {palabras.index(i)}")
#         noencontre=False

# if noencontre:
#     print(f"No encontre la palabra")

"""
palabras=["Hola", "2024", "Bye", "UTD"]
palabra_buscar=input("Dame la palabra buscar: ")

i=0
while i < len(palabra_buscar):
    if palabra_buscar == palabras[i]:
        print(f"Su palabra {palabra_buscar[i]}, en la posicion, {i}")
        noencontre=False
    i+=1

if noencontre:
    print(f"No encontre la palabra")

"""
# Ejemplo #3 Agregar o eliminar elementos de una lista 
"""
numeros=[23,34]

print(numeros)


# Agregar numeros
numeros.append(100)   #Con el append coloca donde sigue
print(numeros)
numeros.insert(3, 200)  #Con el inser se coloca la posicion en la que queremos el valor
print(numeros)

# eliminar un elemento
numeros.remove(100)   #indicar el elemento a borrar, si hay dos iguales se van los dos
print(numeros)

numeros.pop(1)   #indicar el indice a borrar
print(numeros)
"""
# Ejemplo #4 Lista multidimensional
"""
agenda=[
    ["Carlos",6181563424],
    ["Karin",6188001127],
    ["Leon",6184536463],
    ["Pedro",6182345646],
]

print (agenda)

for i in agenda:
    print(f"{agenda.index(i)+1}.- {i}")
.
"""




















    # Ejemplo #5 Crear un programa que permita gestionar (administrar) peliculas, colocar un mennu
    # de opciones para agregar, remover, consultar peliculas.

    #Notas
    # 1.- Utilizar funciones y mandar llamar desde otro archivo
    # 2.- Utilizar listas para almacenar los nomnbres de peliculas

from funciones_peliculas import *
import os

bucle=True
while bucle:
    print("\n..::: BLOCKBUSTER :::... \n 1.-Agregar peliculas \n 2.-Remover \n 3.-Consultar peliculas \n 4.-Actualizar lista \n 5.-Salir")
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
    elif opcion == "5":
        os.system("cls")
        print("..:::  VUELVA PRONTO  :::..")
        bucle=False
    else:
        print("Opcion invalida, porfavor ingrese una opcion valida")
        esperaTecla()

    
