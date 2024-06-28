class Usuarios:
    def __init__(self, nombre, direccion, tel):
        self.nombre = nombre
        self.direccion = direccion
        self.tel = tel

    def getnombre(self):
        return self.nombre  

    def setnombre(self, nombre):
        self.nombre = nombre

    def getdireccion(self):
        return self.direccion  

    def setdireccion(self, direccion):
        self.direccion = direccion

    def gettel(self):
        return self.tel  

    def settel(self, tel):
        self.tel = tel

    def inf_usuario(self):
        pass

class Clientes(Usuarios):
    def __init__(self, nombre, direccion, tel, num_cliente):
        super().__init__(nombre, direccion, tel)
        self.__num_cliente = num_cliente

    def getnum_cliente(self):
        return self.__num_cliente  

    def setnum_cliente(self, num_cliente):
        self.__num_cliente = num_cliente
    
    def inf_usuario(self):
        print(f"Nombre: {self.getnombre()}, Direccion: {self.getdireccion()}, Telefono: {self.gettel()}, Numero de Cliente: {self.getnum_cliente()}")

class Empleados(Usuarios):
    def __init__(self, nombre, direccion, tel, salario, num_empleado, tipo):
        super().__init__(nombre, direccion, tel)
        self._salario = salario
        self._num_empleado = num_empleado
        self._tipo = tipo

    def getsalario(self):
        return self._salario  

    def setsalario(self, salario):
        self._salario = salario

    def getnum_empleado(self):
        return self._num_empleado  

    def setnum_empleado(self, num_empleado):
        self._num_empleado = num_empleado

    def gettipo(self):
        return self._tipo  

    def settipo(self, tipo):
        self._tipo = tipo
    
    def inf_usuario(self):
        print(f"Nombre: {self.getnombre()}, Direccion: {self.getdireccion()}, Telefono: {self.gettel()}, Numero de Empleado: {self.getnum_empleado()}, Salario: {self.getsalario()}, Tipo: {self.gettipo()}")
