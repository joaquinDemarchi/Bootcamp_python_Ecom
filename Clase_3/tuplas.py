frutas = ("manzana", "banana", "naranja", "mango","melon")
# "manzana", "banana", "naranja", "mango","melon"
#     0         1          2         3       4
# print(frutas)
# print(frutas[1])
# print(frutas[2])
# print(frutas[2:4]) # obtengo una tupla comprendida en un rango
# print(frutas[-1]) # obtengo el ultimo elemento
# print(frutas[:3]) # obtengo primeros 3 elementos
# print(frutas[3:]) # obtengo los elementos sin considerar los 3 primeros

# actualizar tupla (OJO, es una trampilla)
# frutas_act = list(frutas)
# print("Soy:",frutas.__class__.__name__)
# print("Ahora soy:",frutas_act.__class__.__name__)
# frutas_act[1] = "SuperBanana"
# frutas = tuple(frutas_act)
# print(frutas)

# algunas operaciones con tuplas
tupla1= ("a", "c", "z")
tupla2 = (10, 23,34)
tupla3 = tupla1 + tupla2
print(tupla3)

print(tupla3.count(2))