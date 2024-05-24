"""
Existe una estructura de condicion lamada "if"
la cual evalua una condicion para encontrar el valor del "True" o se cumple
la condicion se ejecuta la linea o lineas de codigo

Tenemos 3 tipos de ifs

1.- El if simple
2.- El if compuesto
3.- El if anidado
4.- if y elif

"""
#Ejemplo 1 if simple

color="rojo"

if color== "rojo": 
    print("SOY ROJO")


# Ejemplo 2 if compuesto

color="rojo"

if color== "rojo": 
    print("SOY ROJO")
else: 
    print("NO SOY ROJO")

# Ejemplo 3 if ANIDADO

color="rojo"

if color== "rojo": 
    print("SOY ROJO")
    if color!="rojo":
        print("SOY DE OTRO COLOR")
else: 
    print("NO SOY ROJO")

# Ejemplo 4 if con elif

color="rojo"

if color== "rojo": 
    print("SOY ROJO")
elif color=="negro":
    print("SOY DE COLOR NEGRO")
elif color=="verde":
    print("SOY DE COLOR VERDE")
else:
    print("NO SOY ROJO, VERDE O NEGRO")

