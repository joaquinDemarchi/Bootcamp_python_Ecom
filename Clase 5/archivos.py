
from datetime import datetime
# # Abriendo y leyendo el archivo completo
# with open('http_access_200304.log', 'r') as archivito:
#     contenido = archivito.read()  # Lee todo el contenido del archivo
#     print(contenido[:500])      # Imprime los primeros 500 caracteres

# leer linea por linea
# with open('http_access_200304.log', 'r') as archivo:
#     for linea in archivo:
#         print(linea.strip())  # Imprime cada línea sin los saltos de línea adicionales

# guardar las lineas en una lista:
# with open('http_access_200304.log', 'r') as archivo:
#     lineas = archivo.readlines()  # Lee todas las líneas y las guarda en una lista
#     print(lineas[:5])             # Imprime las primeras 5 líneas

# escribir en un nuevo archivo el proceso
# with open('http_access_200304.log', 'r') as archivo:
#     with open('resumen_codigos_http.txt', 'w') as archivo_salida:
#         for linea in archivo:
#             partes = linea.split(" ")
#             codigo_respuesta = partes[-2]
#             archivo_salida.write(f"Código HTTP: {codigo_respuesta}\n")


with open('http_access_200304.log', 'r') as archivo:
    lineas = archivo.readlines()  # Lee todas las líneas y las guarda en una lista
    
    for linea in lineas:
        parteDeLinea = linea.split(" ")
        #print(parteDeLinea)
        # if (parteDeLinea[0] == '129.118.191.108'):
        #     print(parteDeLinea)
        
        # IMPRIMIR LISTA DE IPS
        ip = parteDeLinea[0]
        #print("Lista de IPs")
        #print(parteDeLinea[0])
        
        #IMPRIMIR TODOS LOS REGISTROS DE ANTES DEL 10 DE ABRIL
        fechaSucia = parteDeLinea[3]
        fechaLimpia = fechaSucia[1:]
        
        fecha_dt = datetime.strptime(fechaLimpia, '%d/%b/%Y:%H:%M:%S')
        abril10 = datetime(2003,4,10)
        
        # if(fecha_dt < abril10):
        #     print(f"{ip} - {fecha_dt}")

#ESCRIBIR LOS CUANTOS CODIGOS 404 HUBIERON  
with open('http_access_200304.log', 'r') as archivo:
    with open('resumen_codigos_http.txt', 'w') as archivo_salida:
        codigo_respuesta = parteDeLinea[8]
        cantLogs = 0
        codigo200 = 0
        
        for linea in lineas:
            cantLogs += 1
            #print(codigo_respuesta) #nose por que todos salen como 200
            if(codigo_respuesta == '200'):
                codigo200 += 1
        archivo_salida.write(f"""
                                cantidad de registros  {cantLogs}
                                cantidad de codigos 200: {codigo200}
                            """)
        print(f"cantidad de registros  {cantLogs}")
        print(f"cantidad de codigos 200: {codigo200}")