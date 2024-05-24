# Hacer un programa que muestre todos los numeros 
# entre 2 numeros que diga el usuario


primernumero=int(input("Ingrese el primer numero: "))
segundonumero=int(input("Ingrese el segundo numero: "))
i=primernumero
print(f"Los numeros entre {primernumero} y {segundonumero} son:")
while i<segundonumero:
    i+=1
    if i==segundonumero:
        print("Estos son los resultados")
    else:
        print(i)

while i>segundonumero:
    i-=1
    if i==segundonumero:
        print("Estos son los resultados")
    else:
        print(i)