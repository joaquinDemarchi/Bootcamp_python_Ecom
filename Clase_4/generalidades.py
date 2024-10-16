def sumar(x,y):
    return x+y

sumar_lambda = lambda x, y: x+y

suma1 = sumar(5, 2)
suma2 = sumar_lambda(5,2)
print("suma1", suma1)
print("suma2", suma2)


lista_valores = [2, 5 ,8, 7, 18]
print("lista_valores", lista_valores)
nueva_valores = []
for el in lista_valores:
    nueva_valores.append(el*2)
print("nueva_valores", nueva_valores)

# lista por comprension
nueva_valores2 = [el*2 for el in lista_valores if el>2]
print("nueva_valores2", nueva_valores2)

# map

nueva_valores_map = list(map(lambda x: x*2, lista_valores))
print("nueva_valores_map", nueva_valores_map)

# filter

nueva_valores_filter = list(filter(lambda x: x % 2 == 0, lista_valores))
print("nueva_valores_filter", nueva_valores_filter)

# reduce 
from functools import reduce
valor = reduce(lambda x, y: x + y, lista_valores)
print("valor", valor)




