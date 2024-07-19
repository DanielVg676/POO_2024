from conexionBD import *
import hashlib
import datetime


class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre=nombre
        self.apellidos=apellidos
        self.email=email
        self.password=password
        # self.contrasena=self.hash_password(password)
        self.contrasena=password

    # Funcion para encriptar la password
    def hash_password(self, contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()
    
    def registrar(self):
        try:
            fecha=datetime.datetime.now()
            cursor.execute(
                "insert into usuarios values(null, %s, %s, %s, %s, %s)",
                (self.nombre, self.apellidos, self.email, self.contrasena, fecha)
            )
            conexion.commit()
            return True
        except:
            return False
    
# @STATICMETHOD
# AQUI QUITYAMOS EL SELF, PARA ACCEDER A LA CLASE SIN INSTANCIAR EL METODO
    def iniciar_sesion(email, contrasena):
        contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
        try:
            cursor.execute(
                "select * from usuarios where email= %s and password= %s",
                (email, contrasena)
            )
            usuario=cursor.fetchone()
            if usuario:
                return usuario
            else:
                return None
        except:
            return None



# Aqui va a crear un objeto, haciendo uso del constructor usuario y va a recibir los atributos del main
