contador=0
suma_calificaciones_alumnos=0
permiso="SI"
while permiso!="NO":
    nombre = str(input("Ingrese el nombre del alumno: "))
    carrera = str(input("Ingrese el nombre de la carrera: "))
    calificacion1 = int(input("Ingrese la calificacion de la unidad 1: "))
    calificacion2 = int(input("Ingrese la calificacion de la unidad 2: "))
    calificacion3 = int(input("Ingrese la calificacion de la unidad 3: "))
    calificacion_proyecto = int(input("Ingrese la calificacion del proyecto final: "))

    promedio_parciales = (calificacion1+calificacion2+calificacion3)/3
    print(f"El promedio de los parciales es {promedio_parciales}")
    promedio = (promedio_parciales+calificacion_proyecto)/2
    print(f"La calificacion final es {promedio}")

    if promedio < 80 and calificacion_proyecto>50:
        print(f"Tu promedio final fue de {promedio}, PRESENTA EXTRAORDINARIO")
        
    suma_calificaciones_alumnos+=promedio
    contador+=1
    permiso=str(input("¿Desea otra captura: (SI/NO?)"))

promedio_general=suma_calificaciones_alumnos/contador
print(f"Proemedio final general de los alumnos registrados {promedio_general}")