import mysql.connector

# Conectar con la base de datos en mysql
try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_python'
    )

except Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de excepcion: {type(e).__name__}")
    print(f"Ocurrio un error con el servidor  ... Porfavor verifica ...")
except InterfaceError:
    print(f"No es posible conectarse con el servidor")

else:
# Verificar si la conexion fue exitosa
    if conexion.is_connected():
        print(f"Se creo la conexion con la base de datos exitosamente")
    else:
        print(f"No fue posible conectar con la BD ...verifique...")
