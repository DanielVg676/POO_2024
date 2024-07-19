import mysql.connector
from mysql.connector import Error

class conexion:
    def __init__(self, host, database, user, password):
        self.host=host
        self.database=database
        self.user=user
        self.password=password
        self.conexion = self.crear_conexion()

    def crear_conexion(self):
        try:    
            conexion = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if conexion.is_connected():
                print("Conexión exitosa a la base de datos")
                return conexion
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def cerrar_conexion(self):
        if self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada")

    def crear_empleado(self, nombre, puesto, salario):
        cursor = self.conexion.cursor()
        query = "INSERT INTO empleados (nombre, puesto, salario) VALUES (%s, %s, %s)"
        valores = (nombre, puesto, salario)
        cursor.execute(query, valores)
        self.conexion.commit()
        print("Empleado creado exitosamente")

    def leer_empleados(self):
        cursor = self.conexion.cursor()
        query = "SELECT * FROM empleados"
        cursor.execute(query)
        resultados = cursor.fetchall()
        for fila in resultados:
            print(f"ID: {fila[0]}, Nombre: {fila[1]}, Puesto: {fila[2]}, Salario: {fila[3]}")

    def actualizar_empleado(self, id, nombre, puesto, salario):
        cursor = self.conexion.cursor()
        query = "UPDATE empleados SET nombre = %s, puesto = %s, salario = %s WHERE id = %s"
        valores = (nombre, puesto, salario, id)
        cursor.execute(query, valores)
        self.conexion.commit()
        print("Empleado actualizado exitosamente")

    def eliminar_empleado(self, id):
        cursor = self.conexion.cursor()
        query = "DELETE FROM empleados WHERE id = %s"
        valor = (id,)
        cursor.execute(query, valor)
        self.conexion.commit()
        print("Empleado eliminado exitosamente")
