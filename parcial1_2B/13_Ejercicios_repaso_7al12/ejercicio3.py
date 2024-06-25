# 3.- 

# Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#  palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#  el contenido de la lista en mayusculas

import os

lista = []

if not lista:
    print("La lista está vacía. Puedes llenarla con palabras o frases.")

    while True:
        palabra = input("Ingresa una palabra o frase (o escribe 'salir' para terminar): ")
        os.system("cls")

        if palabra.lower() == 'salir':
            break
        
        lista.append(palabra)

print("\nContenido de la lista en mayúsculas:")
for i in lista:
    print(i.upper())