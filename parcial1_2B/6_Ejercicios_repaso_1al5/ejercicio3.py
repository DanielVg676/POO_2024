# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for
#


for i in range (1,61):
     resultado= i*i
     print(f"El cuadrado de {i} es {resultado}")

j=0
resultado2=0
while j<61:
    resultado2=j*j
    print(f"El cuadrado de {j} es {resultado2}")
    j+=1

