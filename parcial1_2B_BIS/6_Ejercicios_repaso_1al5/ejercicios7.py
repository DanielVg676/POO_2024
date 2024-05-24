# Hacer un programa que muestre todos los numeros 
# impares entre 2 numeros que decida el usuario


primernumero=int(input("Ingrese el primer numero: "))
segundonumero=int(input("Ingrese el segundo numero: "))
i=primernumero
print(f"Los numeros entre {primernumero} y {segundonumero} son:")


while i<segundonumero:
    i+=1
    if i==segundonumero:
        print("Estos son los resultados")
    else:
        if i%2==0:
            print(f"{i} es par")
        else:
            print(f"{i} es impar")

while i>segundonumero:
    i-=1
    if i==segundonumero:
        print("Estos son los resultados")
    else:
        if i%2==0:
            print(f"{i} es par")
        else:
            print(f"{i} es impar")

            