# pilares POO:
# 1)abstraccion:
# 2)encacapsulamiento
# 3)herencia
# 4)polimorfismo

# componentes Objeto.
# atributos, caracteristicas
# métodos, servicios
# identificador

# class Coche:
#     """
#     coche: marca, modelo
#     """
#
#     def __init__(self, marca, modelo):
#         self.marca = marca
#         self.modelo = modelo
#
#     def conducir(self):
#         # print(f"Conduciendo el {self.marca} {self.modelo}")
#         return f"Conduciendo el {self.marca} {self.modelo}"
#
# coche1 = Coche(marca="Ford",modelo="Focus")
# print(coche1.marca)
# print(coche1.modelo)
# print(coche1.conducir())
# coche2 = Coche(marca="Ferrari",modelo="F1")
# print(coche2.marca)
# print(coche2.modelo)
# print(coche2.conducir())

# ---------------------------------------------------------------------

# class CuentaBancaria:
#     def __init__(self,saldo):
#         self.__saldo = saldo
#
#     def depositar(self,monto):
#         self.__saldo += monto
#
#     def mostrar_saldo(self):
#         print(f"Saldo actual: {self.__saldo}")
#
#     def get_saldo(self):
#         return self.__saldo
#
# cuenta = CuentaBancaria(1000)
# print(f"Tengo: {cuenta.saldo}")
# cuenta.depositar(500)
# print(f"Tengo ahora: {cuenta.saldo}")
# cuenta.mostrar_saldo()
# # cuenta.saldo = 0 # muestra de que puedo cambiar el valor, porque es publico
# # cuenta.mostrar_saldo()
# cuenta.saldo = 0 #
# cuenta.mostrar_saldo()

# ---------------------------------------------------------------------
# class Animal:
#     def grito(self): # metodo abstracto
#         return NotImplementedError("Este método debe ser sobreescrito por sus clases hijas")
#
#     def mensaje(self):
#         return "soy animal"
#
# class Perro(Animal):
#
#     def grito(self):
#         return "guau!"
#
#     def mensaje(self):
#         return "soy perro"
#
# class Gato(Animal):
#
#     def grito(self):
#         return "miau!"
#
#     # def mensaje(self):
#     #     return "soy gato"
#
# perro = Perro()
# print(perro.grito(), perro.__class__.__name__, perro.mensaje())
# gato = Gato()
# print(gato.grito(), gato.__class__.__name__, gato.mensaje())

# -------------------------------------------------------------------
class Ave:
    def volar(self):
        print("Vuelo")

class Pinguino(Ave):
    def volar(self):
        print("No vuela")

ave = Ave()
pinguino = Pinguino()
ave.volar()
pinguino.volar()


