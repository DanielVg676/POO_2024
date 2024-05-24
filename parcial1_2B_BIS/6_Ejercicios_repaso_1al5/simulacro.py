# Crear un programa que calcule y obtenga el total a pagar por un producto 
# determinado. Se debera de solicitar el nombre o descripcion del producto,
# codigo, cantidad del producto, precio unitario del product.
# el total a pagar incluye el iva 16% y el descuento.
# si se compran de 1 a 5 productos, si se otorga el 10% de descuento
# si se compran de 6 a 10, se otorga el 15% de descuento y si se compran mas de
# 10 se otorga el 20% de descuento.


producto=input("Ingrese el nombre del producto: ")
codigo=input("Ingrese su codigo: ")
cantidad=int(input("Ingrese la cantidad a comprar: "))
precio_uni=int(input("Ingrese el precio unitario: "))

precio_uni_iva=precio_uni*1.16
precio_sin_iva=cantidad*precio_uni
precio_con_iva=precio_sin_iva*1.16

if cantidad>=1 and cantidad<=5:
    precio_total=precio_con_iva*.90

if cantidad>=6 and cantidad<=10:
    precio_total=precio_con_iva*.85

if cantidad>10:
    precio_total=precio_con_iva*.80


print(f"El producto {producto} con codigo {codigo} con un precio final c/u de {precio_uni_iva} con {cantidad} unidades su cuenta a pagar con descuento por mayoreo es de ${precio_total}")