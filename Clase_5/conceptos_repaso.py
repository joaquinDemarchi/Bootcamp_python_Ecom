from abc import ABC, abstractmethod

# Definir una clase abstracta
class FiguraGeometrica(ABC):

    @abstractmethod
    def area(self):
        pass  # Método abstracto

    @abstractmethod
    def perimetro(self):
        pass  # Método abstracto

# Intentar instanciar la clase abstracta generará un error
# figura = FiguraGeometrica()  # Esto dará un error

# Crear subclases que implementan los métodos abstractos
class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * (self.radio ** 2)

    def perimetro(self):
        return 2 * 3.14 * self.radio

# Instanciar las subclases y usarlas
cuadrado = Cuadrado(4)
print(f"Área del cuadrado: {cuadrado.area()}")        # Output: 16
print(f"Perímetro del cuadrado: {cuadrado.perimetro()}")  # Output: 16

circulo = Circulo(3)
print(f"Área del círculo: {circulo.area()}")        # Output: 28.26
print(f"Perímetro del círculo: {circulo.perimetro()}")  # Output: 18.84
