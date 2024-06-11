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

""""
# Ejemplo 2: Cuando se solicita un numero y se ingresa otra cosa
from multiprocessing import Value
from prompt_toolkit import PromptSession


try:
    numero=int(input("ingrese un numero entero positivo: "))

    if numero>0:
        print("Soy un numero entero positivo")
    else:
        print("Soy un numero entero negativo")
except ValueError:
    print("No es posible convertir una letra a un numero, verifica por favor...")


"""
# Ejemplo 3 Cuando multiopoples exepciones
try:
    numero=int(input("Ingresa un numero: "))

    print("El cuadrado de un numero es: " +str(numero*numero))

except TypeError:
    print("Es necesario convertir el numero a entero")
except ValueError:
    print("No es posible convertir una letra a un numero, verifia porfavor..")
else:    #Este se ejecuta siempre y cuando en los except no son necesarios y no se ejecutaron
    print("Todo se ejecuto correctamente sin errores")

finally:
    print("Ya termino")