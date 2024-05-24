#Formas de concatenacion en python

nombre="Daniel Aurelio Villarreal Gallegos"
especialidad="Area de software multiplataforma"
carrera="Ingenieria en Gestion y Desarrollo de Software"

#1er forma
print("Mi nombre es "+nombre+" estoy en la especialidad de "+especialidad+" en la carrera de "+carrera+"")

#2da forma
print("Mi nombre es ",nombre," estoy en la especialidad de ",especialidad," en la carrera de ",carrera,"")

#3ra forma FORMA MAS COMUN EN PYTHON
print(f"Mi nombre es {nombre} estoy en la especialidad de {especialidad} en la carrera de {carrera}")

print("\n")

#4ta forma
print("Mi nombre es {} estoy en la especialidad de {} en la carrera de {}".format(nombre, especialidad, carrera))

print("\n")

#5ta forma
print('Mi nombre es '+nombre+' estoy en la especialidad de '+especialidad+' en la carrera de '+carrera+'')