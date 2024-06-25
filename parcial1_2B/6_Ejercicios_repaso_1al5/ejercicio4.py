#Solicitar 2 numeros al usuario
# y realizar todas las operaciones
# basicas de una calculadora (+,-,*,/)
# y mostrar por pantalla el resultado

primernumero=int(input("Ingrese el primer numero: "))
segundonumero=int(input("Ingrese el segundo numero: "))

resultado=primernumero+segundonumero
print(f"{primernumero} + {segundonumero} = {resultado}")

resultado=primernumero-segundonumero
print(f"{primernumero} - {segundonumero} = {resultado}")

resultado=primernumero/segundonumero
print(f"{primernumero} / {segundonumero} = {resultado}")

resultado=primernumero*segundonumero
print(f"{primernumero} * {segundonumero} = {resultado}")
