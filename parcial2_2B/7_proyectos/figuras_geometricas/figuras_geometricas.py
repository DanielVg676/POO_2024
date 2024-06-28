class Figuras:
    def __init__(self, x, y, visible, figura):
        self.x = x
        self.y = y
        self.visible = visible
        self.figura = figura

    def gety(self):
        return self.y

    def sety(self, y):
        self.y = y

    def getx(self):
        return self.x

    def setx(self, x):
        self.x = x

    def getvisible(self):
        return self.visible

    def setvisible(self, visible):
        self.visible = visible

    def getfigura(self):
        return self.figura

    def setfigura(self, figura):
        self.figura = figura

    def estaVisible(self):
        estado = True if self.visible else "no visible"
        print(f"La figura {self.figura} es {estado}")

    def mostrar(self):
        print(f"La figura {self.figura} está siendo mostrada")

    def ocultar(self):
        print(f"La figura {self.figura} está siendo ocultada")

    def mover(self):
        posicion = int(input("Ingrese la posición a donde desea mover la figura: "))
        print(f"La figura {self.figura} ha sido movida a la posición {posicion}")

    def calcularArea(self):
        pass


class Rectangulos(Figuras):
    def __init__(self, x, y, visible, figura, alto, ancho):
        super().__init__(x, y, visible, figura)
        self.__alto = alto
        self.__ancho = ancho

    def getalto(self):
        return self.__alto

    def setalto(self, alto):
        self.__alto = alto

    def getancho(self):
        return self.__ancho

    def setancho(self, ancho):
        self.__ancho = ancho

    def ocultar(self):
        print(f"El rectángulo {self.figura} está siendo ocultado")

    def mostrar(self):
        print(f"El rectángulo {self.figura} está siendo mostrado")

    def calcularArea(self):
        return self.__alto * self.__ancho

    def getInfo(self):
        print(f"x = {self.getx()}, y = {self.gety()}, visible = {self.getvisible()}, figura = {self.getfigura()}, alto = {self.getalto()}, ancho = {self.getancho()}")


class Circulos(Figuras):
    def __init__(self, x, y, visible, figura, radio):
        super().__init__(x, y, visible, figura)
        self.__radio = radio

    def getradio(self):
        return self.__radio

    def setradio(self, radio):
        self.__radio = radio

    def ocultar(self):
        print(f"El círculo {self.figura} está siendo ocultado")

    def mostrar(self):
        print(f"El círculo {self.figura} está siendo mostrado")

    def calcularArea(self):
        return ((3.1416) * (self.radio ** 2))

    def getInfo(self):
        print(f"x = {self.getx()}, y = {self.gety()}, visible = {self.getvisible()}, figura = {self.getfigura()}, radio = {self.getradio()}")
