import mysql.connector

try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        # database='bd_python'     AQUI NO PONEMOS ESTO, YA QUE ESTO HARIA QUE NOS CONECTE A LA BASE DE DATOS YA CREADA, Y A QUIA VAMOS A CREAR UNA BASE DE DATOS
    )
    
except:
    print(f"Ocurrio un error con el sistema, porfavor verifique mas tarde")

else:
    # Crear un objeto de tipo cursor que permita ejecutar instrucciones sql

    micursor=conexion.cursor()

    # Con este comando sql="" para asignarle un comando a la variable sql y luego usar el micursor.execute() para ejecutar ese comando

    sql="create database bd_python"

    micursor.execute(sql)

    if micursor:
        print(f"se creo la BD exitosamente")

    # Mostrar las BD que existen en el SGBD MySQL

    micursor.execute("show databases")

    for x in micursor:
        print(x)