
# Estructura condicional

print("\t\tIngrese un \nnumero\n")
numero = input("> ")

"""
# if-simple
if not numero.isnumeric():
    print("El valor NO es")
    print("un")
    print("numero")
    
"""  
# if-else
"""
if not numero.isnumeric():
    print("El valor NO es")
    print("un")
    print("numero")
else:
    print("El valor SI es")
    print("un")
    print("numero")

print("----- FIN -----")
"""
"""
if not numero.isnumeric():
    print("El valor NO es")
    print("un")
    print("numero")
else:
    if int(numero) % 2 == 0:
        print("El numero ingresado es PAR")
    else:
        print("El numero ingresado es IMPAR")
    
"""

# elif
"""
if not numero.isnumeric():
    print("El valor NO es")
    print("un")
    print("numero")
elif int(numero) % 2 == 0:
    print("El numero ingresado es PAR")
else:
    print("El numero ingresado es IMPAR")
"""

"""
if numero.isnumeric():
    mensaje = "El valor es un numero"
else:
    mensaje = "El valor no es un numero"
"""

mensaje = "El valor es un numero" if numero.isnumeric() else "El valor no es un numero"

print(mensaje)