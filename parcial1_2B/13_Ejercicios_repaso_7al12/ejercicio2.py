# 2.- 
# Escribir un programa  que añada valores a una lista mientras que su longitud 
#  sea menor a 120, y luego mostrar la lista: Usar un while y for


import os
os.system("cls")

lista=[4,3,2,5,2,7,1,9]

while len(lista)<120:
    valor_añadir=int(input("Añada el numero: "))
    lista.append(valor_añadir)

for i in lista:
    print(i)

i=0
while i <=len(lista)-1:
    print(lista[i])
    i+=1