from conexionBD import *

try:

    micursor=conexion.cursor()

    nombre=input("Ingrese el nombre: ")
    direccion=input("Ingrese la direccion: ")
    tel=input("Ingrese el telefono: ")
    # sql="INSERT INTO `cliente` (`id`, `nombre`, `direccion`, `tel`) VALUES (NULL, 'Daniel Contreras', 'Col. Centro', '6181563424')"

    sql="INSERT INTO `cliente` (`id`, `nombre`, `direccion`, `tel`) VALUES (NULL, %s, %s, %s)"
    valores=(nombre, direccion, tel)

    micursor.execute(sql, valores)

    # Sirve para finalizar de manera exitosa la ejecicion del SQL
    conexion.commit()

except:
    print(f"Se a prducido un erro porfavor verifica")

else:  
    print(f"Registro insertado Exitosamente")