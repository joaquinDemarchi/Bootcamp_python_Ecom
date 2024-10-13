from . import validador
# from .validador import todo_es_un_numerico, rango_valido
# from .validador import *

def validar_documentos(lista_documentos):
    lista_documentos_validos = []
    lista_documentos_invalidos = []
    for doc in lista_documentos:
        doc=doc.replace(".", "")
        
        if not validador.todo_es_un_numerico(doc):
            lista_documentos_invalidos.append({
                "value": doc,
                "error": "tiene caracteres especiales"
            })
            continue
        
        doc = int(doc)
        if not validador.rango_valido(doc):
            lista_documentos_invalidos.append({
                "value": doc,
                "error": "supera longitud"
            })
            continue
        lista_documentos_validos.append(doc)
    return lista_documentos_validos, lista_documentos_invalidos