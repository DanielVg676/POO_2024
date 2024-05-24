contador = 0
registro = "SI"

while registro == "SI":
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))

    imc = peso / (altura * altura)

    print(f"IMC: {imc}")

    if imc < 18.5:
        print("Peso inferior al normal")
    elif 18.5 <= imc <= 24.9:
        print("Normal")
    elif 25.0 <= imc <= 29.9:
        print("Peso superior al normal")
    elif imc >= 30.0:
        print("Obesidad")
    
    contador += 1

    registro = input("¿Desea continuar con otro registro? SI/NO: ")
    if registro == "NO":
        break

print(f"Usted ha registrado a {contador} personas")
