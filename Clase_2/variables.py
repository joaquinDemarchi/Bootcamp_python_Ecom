nombre = "Lucas"

apellido = "Ibañez"

PI = 3.14
'''




# --------------------------------------------



formato1 = nombre + " " + apellido

# f-string
formato2 = f"El nombre completo de la persona es: {nombre} {apellido}"

formato3 = "---> %s %s" % (nombre, apellido)

formato4 = "Hola, mi nombre es {} , {}.".format(nombre, apellido)

"""
esto es un comentario multilinea
"""

print("formato1", formato1)
print("formato2", formato2)
print("formato3", formato3)
print("formato4", formato4)

print(f"te llamas '{nombre}'")

texto = """
asdasd
asd
asd
as
da
sd
asd
"""
print("texto", texto)

# str -> string
print("clase", type(nombre))

# int -> integer
print("clase", type(3))

print("clase", type(PI))

nombre = input("Ingresa tu nombre:")
print(f"nombre ingresado: {nombre}")
# print(f"tipo de dato: {type(nombre)}")
# print(f"tipo de dato: {nombre.__class__.__name__}")

'''
# parsear tipos de datos
numero1 = input("Ingrese un numero:")
# bool -> True - False
print(numero1.isnumeric())

"""
numero2 = input("Ingrese un numero:")

print("Suma->", numero1+numero2)
"""