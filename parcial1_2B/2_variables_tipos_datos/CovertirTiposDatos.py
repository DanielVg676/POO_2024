"""
Comentario de carias lineas:
se trabaja en pantalla una cadena de caracteres
se trabaja por default con "cadena", es decir python no
puede concatenar otra que no sea un string(str)

"""

texto="Soy una cadena de caracteres"
numero=23

#Concatenar str con str

print("Soy una cadena y "+texto)

#Concatenar str con int
numero_str=str(numero)
print("El numero es: "+numero_str)
print("El numero es: ""\""+numero_str+"\"")


# Concatenar int con str
n1=int('23')
n2=33
suma=n1+n2

print("La suma es: "+ str(suma))

print(f"La suma es: {suma}")

# Concatenar float e int con str
n1=23
n2=33.00
suma=float(n1)+n2

print(f"La suma es: {suma}")

n1=23.99
n2=33.00
suma=int(n1)+n2

print(f"La suma es: {suma}")
