# ------------------
# imports
# ------------------
import time

# ------------------
# libs terceros
# ------------------


# ------------------
# libs propios
# ------------------
from parametros import LISTA_DOCUMENTOS
from funcion.core import validar_documentos


if __name__ == '__main__':
    """
    longuitud: (rango entre 7 y 8)
    # si tiene caracteres especiales (tambien .), son invalidos
    # todos los caracteres deben ser un digito
    # Otras consideraciones por ustedes.
    """
    """
    valores = validar_documentos(LISTA_DOCUMENTOS)
    print("valores-->", valores)
    lista_documentos_validos = valores[0]
    lista_documentos_invalidos = valores[1]
    """
    lista_documentos_validos, lista_documentos_invalidos = validar_documentos(LISTA_DOCUMENTOS)
    print("SUPERSCRIPT-> __name__", __name__)
    print("Documentos validos:", lista_documentos_validos)
    print("Documentos invalidos:", lista_documentos_invalidos)
