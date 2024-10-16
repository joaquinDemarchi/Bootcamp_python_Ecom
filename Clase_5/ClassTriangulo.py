from abc import ABC, abstractmethod

# clase abstracta
class FiguraGeometrica(ABC):

    @abstractmethod
    def area(self):
        pass  # Método abstracto

    @abstractmethod
    def perimetro(self):
        pass  # Método abstracto

# subclase 
class CalcularTriangulo(FiguraGeometrica):
    def __init__(self, ladoIzq, ladoDer, base, altura):
        self.ladoIzq = ladoIzq
        self.ladoDer = ladoDer
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura)/2

    def perimetro(self):
        return  self.ladoIzq + self.ladoDer + self.base
    
#objetos
isosceles = CalcularTriangulo(ladoIzq=20, ladoDer=20, base=20, altura= 17.321)

#probar invocaciones
print("TRIANGULO ISOSCELES")
print(f"Área del triangulo: {isosceles.area()}")        # Output: 16
print(f"Perímetro del triangulo: {isosceles.perimetro()}") 