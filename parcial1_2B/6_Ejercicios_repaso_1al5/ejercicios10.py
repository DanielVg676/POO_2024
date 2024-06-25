#  Crear un programa que solicite la calificacion de 15 alumnos 
#  e imprimir en pantalla cuantos aproboron y cuantos no aprobaron

alumnos_aprobados=0
alumnos_reprobados=0
for i in range (1,3):
    calificaciones=int(input(f"Ingrese las calificaciones del alumno {i}"))
    if calificaciones>=80 and calificaciones<=100:
        alumnos_aprobados+=1
    else:
        if calificaciones<80:
            alumnos_reprobados+=1


print(f"Alumnos que aprobaron {alumnos_aprobados}")
print(f"Alumnos que reprobaron {alumnos_reprobados}")

