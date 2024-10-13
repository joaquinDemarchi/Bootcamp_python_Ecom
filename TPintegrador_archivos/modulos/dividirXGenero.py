
def dividirXGenero(registros):
    distribucion_genero = {'M': 0, 'F': 0}

    for registro in registros:
        sexo = registro['sexo']  # Obtiene el sexo del registro
        # Verifica si el sexo es valido 
        if sexo in distribucion_genero:
            #si es valido incrementa el contador
            distribucion_genero[sexo] += 1
    
    #retorna un dic 
    return distribucion_genero
    