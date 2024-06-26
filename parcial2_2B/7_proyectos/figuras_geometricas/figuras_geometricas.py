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
        print(f"La figura {self.figura} es {self.visible}")

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
        self.alto = alto
        self.ancho = ancho

    def getalto(self):
        return self.alto

    def setalto(self, alto):
        self.alto = alto

    def getancho(self):
        return self.ancho

    def setancho(self, ancho):
        self.ancho = ancho

    def ocultar(self):
        print(f"El rectángulo {self.figura} está siendo ocultado")

    def mostrar(self):
        print(f"El rectángulo {self.figura} está siendo mostrado")

    def calcularArea(self):
        return self.alto * self.ancho

    def getInfo(self):
        print(f"x = {self.x()}, y={self.y()}, visible = {self.visibiliada()}, figura = {self.figura()}, alto = {self.alto()}, ancho = {self.ancho()}")
        

class Circulos(Figuras):
    def __init__(self, x, y, visible, figura, radio):
        super().__init__(x, y, visible, figura)
        self.radio = radio

    def ocultar(self):
        print(f"El círculo {self.figura} está siendo ocultado")

    def mostrar(self):
        print(f"El círculo {self.figura} está siendo mostrado")

    def calcularArea(self):
        return ((3.1416) * (self.radio ** 2))

    def getInfo(self):
        print(f"x = {self.x()}, y={self.y()}, visible = {self.visibiliada()}, figura = {self.figura()}, radio = {self.radio()}")
        

rectangulo1 = Rectangulos(x=0, y=0, visible=True, figura="Rectángulo 1", alto=5, ancho=3)
print(f"Área del rectángulo: {rectangulo1.calcularArea()}")

circulo1 = Circulos(x=2, y=2, visible=True, figura="Círculo 1", radio=2)
print(f"Área del círculo: {circulo1.calcularArea()}")
