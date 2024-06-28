from figuras_geometricas import Figuras, Rectangulos, Circulos

print("Figura1")
rectangulo1=Rectangulos(x=0, y=0, visible=True, figura="Rectángulo 1", alto=5, ancho=3)
print(f"Área del rectángulo: {rectangulo1.calcularArea()} metros cuadrados")
rectangulo1.getInfo()


circulo1=Circulos(x=2, y=2, visible=True, figura="Círculo 1", radio=2)
print(f"Área del círculo: {circulo1.calcularArea()} metros cuadrados")
circulo1.getInfo()