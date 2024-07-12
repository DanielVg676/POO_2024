class Personas:
    def __init__(self, nombre, edad, tel):
        self.nombre=nombre
        self.edad=edad
        self.tel=tel

    def info_persona(self):
        print(f"Informacion de la persona: {self.getnombre()}, {self.getedad()}, {self.gettel()}")

    def setnombre(self):
        self.nombre=nombre
    
    def getnombre(self, nombre):
        return self.nombre

    def setedad(self):
        self.edad=edad
    
    def getedad(self, edad):
        return self.edad
    
    def settel(self):
        self.tel=tel
    
    def gettel(self, tel):
        return self.tel


class Estudiantes(Personas):
    def __init__(self, carreara, matricula):
        super().__init__(self, nombre, edad, tel)
        self.carrera=carrera
        self.matricula=matricula

    def getcarrera(self):
        return self.__carrera

    def setcarrera(self, carrera):
        self.__carrera=carrera
    
    def getmatricula(self):
        return self.__matricula

    def setmatricula(self, matricula):
        self.__matricula=matricula

    def informar_matricula(self):
        print(f"Su carreara es la de: {self.getcarrera()}")
    
    def info_persona(self):
        print(f"Informacion de la persona: {self.getnombre()}, {self.getedad()}, {self.gettel()}, {self.getmatricula()}")

class Docentes(Personas):
    def __init__(self, modalidad, num_empleado):
        super.__init__(self, nombre, edad, tel)
        self.modalidad=modalidad
        self.num_empleado=num_empleado
    
    def getModalidad(self):
        return self._modalidad
    
    def getNum_empleado(self):
        return self._num_empleado
    
    def setModalidad(self):
        self._modalidad=modalidad
    
    def setNum_empleado(self, num_empleado):
        self._num_empleado=num_empleado
    
