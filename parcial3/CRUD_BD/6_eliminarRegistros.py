from conexionBD import *

try:
    micursor=conexion.cursor()

    sql="delete from cliente where id=3"
    micursor.execute(sql)

    conexion.commit()

except:
    print(f"Se ha producido un error")

else:
    print(f"Registro eliminado exitosamente")