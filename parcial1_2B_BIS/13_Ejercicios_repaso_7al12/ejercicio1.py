# 1.- 

#  Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado

import os
os.system("cls")

lista=[4,3,2,5,2,7,1,9]

for i in lista:
    print(i)

def recorrer_lista_y_devolver_string(lista):
    resultado = ""
    for numero in lista:
        resultado += str(numero) + " "
    return resultado.strip()  # Elimina el espacio en blanco final

print(recorrer_lista_y_devolver_string(lista))


lista.sort()
print(f"La lista ordenada es {lista}")
print(f"La longitud de la lista es: {len(lista)}")



dame_numero = int(input("Ingrese el número a buscar: "))
i = 0
noencontre = True

while i < len(lista):
    if dame_numero == lista[i]:
        print(f"El número {dame_numero} se encuentra en la posición {i}")
        noencontre = False
    i += 1

if noencontre:
    print(f"No encontré el número {dame_numero}")