def tipo_triangulo(self): 
    if self.lado1 == self.lado2 == self.lado3: 
        return "Equilátero" 
    elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
        return "Isósceles" 

    return "Escaleno"