#  Hacer un programa que solicite numeros indefinidamente 
#  hasta que se introduzca el 111 y salir del programa

numerox=0

while numerox<111 or numerox>111:
    numerox=int(input("Ingrese el numero hasta adivinar: "))
    if numerox<111 or numerox>111:
        print(f"Incorrecto")

print(f"Adivinaste el numero era 111")