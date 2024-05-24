# Es un ciclo interactivo que se ejecuta x veces en un rango dependiendo los valores 
# numericos enteros establecidos 

# sintaxis:
# for variable in elemento_iterable(lista, rango, etc)
#     bloque de instrucciones

# ejemplo 1 crear un programa que imprima 5 veces el carater @

# contador=1
for contador in range (1,6):
    print("@")

# Ejemplo 2 crear un programa que imprima los numeros del 1 al 5
# los sume y al final imprima la suma
suma=0
for numero in range(1,6):
    print(numero)
    suma+=numero
print(f"La suma es: {suma}")

# Crear un programa que solicite un numero entero y a continuacion
# imprima la tabla de multiplicar correspondiente

numero=int(input("Ingrese el numero que desee la tabal: "))
multi=0
for i in range (1, 11):
    multi=i*numero
    print(f"{numero} X {i}={multi}")