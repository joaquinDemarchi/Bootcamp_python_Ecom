def refuerzosAMas60(registros):

    refuerzos_mayores_60 = 0
    contrEdades = ['6','7','8','9','>']
    
    for registro in registros:
        edad = str(registro['grupo_etario'][0]) 
        #print(edad)
        #valida primero sis es refuerzo y luego si es mayor a 60
        if registro['orden_dosis'] > '2' and edad in contrEdades:
            refuerzos_mayores_60 += 1
            
    return refuerzos_mayores_60

