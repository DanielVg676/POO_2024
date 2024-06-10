# Los errores de excepciones en un lenguaje de programacion no es otra cosaque los errores en tiempo de ejecucion ...
# Cuando se manejan los errores mediante las excepciones en realidad se dice que se evita que se presenten esos errores
# en programa en tiempo de ejecucion

# Ejemplo se presenta un error cuando no es generada una variable
"""
nombre=input("Dame el nombre completo de una persona: ")
try:
    if len(nombre)>0:
        nombre_usuario="El nombre del usuario del sistema es: "+nombre

    print(nombre_usuario)
except:
    print("Es necesario introducir un nombre de una persona")

"""
# Ejemplo 2: Cuando se solicita un numero y se ingresa otra cosa

numero=int(input("ingrese un numero entero positivo: "))

if numero>0:
    print(f"Soy un numero entero positivo")
else:
    print(f"Soy un numero entero negativo")