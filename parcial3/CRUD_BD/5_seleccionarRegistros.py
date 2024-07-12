from conexionBD import *

try:
    micursor=conexion.cursor()

    sql="select * from cliente"
    micursor.execute(sql)


    # Crear un obhjheto para enviar el resultado de la ejecucion del ejecut
    # para posteriormente mostrar el ciclo

    resultado=micursor.fetchall()

except:
    print(f"Ha ocurrido un error")

else:
    for x in resultado:
        print(x)
