# funciones --> retorna valor / procedimientos ---> no ratorna un valor
def saludar(nombre, apellido, domicilio=None):

    print(f"Nombre= {nombre}, Apellido={apellido}!")
    
    if domicilio:
        print(f"vive en {domicilio}")
    # return True

# def sumar(*args):
# funcion con argumentos posicionales
def sumar(*todos_los_argumentos):
    suma = 0
    for num in todos_los_argumentos:
        suma+=num

    return suma

# def saludar_args_palabras_claves(**kwargs)
def saludar_2(**todos_los_argumentos):

    print("nombre", todos_los_argumentos.get("nombre", "------"))
    print("apellido", todos_los_argumentos.get("apellido", "******"))
    # print(todos_los_argumentos.__class__.__name__)
# x = saludar(apellido="Ibañez", nombre="Lucas")
# x = saludar(apellido="Ibañez", nombre="Lucas", domicilio="calle 123")

# suma = sumar(5, 6, 4, 8, 7)

# saludar_2(nombre="Lucas", apellido="Ibañez")

# print(f"suma: {suma}")

saludar_2(nombre="Lucas")


