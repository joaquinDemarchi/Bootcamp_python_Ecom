
persona = {
    "nombre": "Lucas",
    "apellido": "Ibañez",
    "direccion": "calle 123"
}


# try / except
direccion = None
try:
    direccion = persona["direccion"]
    x = 10 / 2
# except Exception as e:
except ZeroDivisionError:
    print("No se puede dividir por cero")
except Exception as la_excepcion:
    print("ha ocurrido un error:", la_excepcion.__class__.__name__)
else:
    print("elseeeee--> NINGUNA EXC OCURRIO")
finally:
    print("finally--> SIEMPRE")


if direccion is not None:
    print(f"la direccion de la persona es: {direccion}")

