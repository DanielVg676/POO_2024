# 5.- 
# Crear una lista y un diccionario con el contenido de esta tabla: 

#   ACCION              TERROR        DEPORTES
#   MAXIMA VELOCIDAD    LA MONJA       ESPN
#   ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
#   RAPIDO Y FURIOSO I  LA MALDICION   ACCION


#   imprimir la información

import os
os.system("cls")

lista=[
    ["Accion", "Maxima velocidad", "Arma mortal 4", "Rapido y furioso I"],
    ["Terror", "La monja", "El conjuro", "La maldicion"],
    ["Deportes", "ESPN", "Mas deportes", "Accion"]
]
print("La lista contiene: ")
for i in lista:
    print(i)

dicti={
    "ACCION": ["MAXIMA VELOCIDAD", "ARMA MORTAL 4", "RAPIDO Y FURIOSO I"],
    "TERROR": ["LA MONJA", "EL CONJURO", "LA MALDICION"],
    "DEPORTES": ["ESPN", "MAS DEPORTE", "ACCION"]
}

print("\nDiccionario con el contenido de la tabla:")
for i, valores in dicti.items():
    print(f"{i}: {valores}")




    