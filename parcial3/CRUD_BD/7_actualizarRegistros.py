from conexionBD import *

try:
    micursor=conexion.cursor()

    sql="update cliente set direccion='Col. Nueva Vizcaya' where id=2"
    micursor.execute(sql)

    conexion.commit()

except:
    print(f"Se ha producido un error")

else:
    print(f"Registro actualizado exitosamente")