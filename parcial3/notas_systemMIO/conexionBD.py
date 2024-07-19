import mysql.connector
from mysql.connector import Error

try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_notas'
    )
    cursor=conexion.cursor(buffered=True)
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


# class conexion:

#     def __init__(self, host, user, password, database):
#         self.host=host
#         self.user=user
#         self.password=password
#         self.database=database
#         self.conexion=self.crear_conexion()

#     # Conectar con la base de datos en mysql
#     def crear_conexion(self):
#         try:
#             conexion=mysql.connector.connect(
#                 host=self.host,
#                 user=self.user,
#                 password=self.password,
#                 database=self.database
#             )

#             # Crear un objeto de tipo cursor que tenga un programa 
#             Cursor=conexion.cursor(buffered=True)
#         except Exception as e:
#             print(f"Error: {e}")
#             print(f"Tipo de excepcion: {type(e).__name__}")
#             print(f"Ocurrio un error con el servidor  ... Porfavor verifica ...")
#         except InterfaceError:
#             print(f"No es posible conectarse con el servidor")

#         else:
#         # Verificar si la conexion fue exitosa
#             if self.conexion.is_connected():
#                 print(f"Se creo la conexion con la base de datos exitosamente")
#             else:
#                 print(f"No fue posible conectar con la BD ...verifique...")
        