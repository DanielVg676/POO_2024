# El ciclo while es una estructura de control que itera o repite
# la ejecucion de una serie de instrucciones tantas veces como la condicion se cumpla 
# "True"

# Sintaxis:

# while condicion:
#     bloque de instrucciones

# ejemplo 1 crear un programa que imprima 5 veces el carater @
contador=1
while contador<=5:
    print("@")
    contador+=1

# Ejemplo 2 crear un programa que imprima los numeros del 1 al 5
# los sume y al final imprima la suma

contador=1
suma=0
while contador<=5:
    print(contador)
    print("@")
    contador+=1
print(f"La suma es: {suma}")

# Crear un programa que solicite un numero entero y a continuacion
# imprima la tabla de multiplicar correspondiente

numero=int(input("Ingrese el numero que desee la tabal: "))
multi=0
i=1
while i<=10:
    multi=i*numero
    print(f"{numero} X {i}={multi}")
    i+=1
    


    x=33 
    # nuevo cambio