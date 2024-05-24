#  Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla 
#  y luego las multiplicaciones del 1 al 10

for j in range (1,11):
    for i in range (1,11):
        resultado=(j*i)
        print (f"Tablas de multplicar de {j}: ")
        print (f"{j} X {i} = {resultado}")
    
    
