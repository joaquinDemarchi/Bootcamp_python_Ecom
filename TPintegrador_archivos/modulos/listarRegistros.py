#lista los reg estraidos del csv transformados en diccionarios en una lista
def listarRegistros(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:  
        # Lee la primera línea para obtener los encabezados
        encabezados = f.readline().strip().split(',')
        datos = []
        for linea in f:
            fila = linea.strip().split(',')
            datos.append(dict(zip(encabezados, fila)))  # Combina encabezados con valores
    return datos