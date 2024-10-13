
def registrarErrores(registros) :
    
    jurPosibles = [
    "Buenos Aires", "Caba", "Catamarca", "Chaco", "Chubut",
    "Cordoba", "Corrientes", "Entre Rios", "Formosa", "Jujuy",
    "La Pampa", "La Rioja", "Mendoza", "Misiones", "Neuquen",
    "Rio Negro", "Salta", "San Juan", "San Luis", "Santa Cruz",
    "Santa Fe", "Santiago Del Estero", "Tierra Del Fuego", "Tucuman"
    ]

    registros_erroneos = []
    
    for i, registro in enumerate(registros):
        
        # Verificar valores nulos
        
        nulo = False
        
        for campo in registro:
            if registro[campo] == '':
                nulo = True
                registros_erroneos.append((i, registro, f"{campo} es nulo"))
        
        if registro['sexo'] not in ['M', 'F'] and nulo != True:
            registros_erroneos.append((i, registro, "Sexo inválido"))
            
        if registro['vacuna'] not in ['Moderna', 'Sputnik', 'Astrazaneca', 'Sinopharm', 'Pfizer'] and nulo != True:
            registros_erroneos.append((i, registro, "Vacuna inválida"))
            
        if registro['jurisdiccion_residencia'] not in jurPosibles and nulo != True:
            registros_erroneos.append((i, registro, "Jurisdiccion invalida"))
            
        if ( "<" not in registro['grupo_etario']
            and ">" not in registro['grupo_etario']
            and "=" not in registro['grupo_etario']
            and "-" not in registro['grupo_etario']
            ) and nulo != True:
            registros_erroneos.append((i, registro, "Grupo etario invalido"))
            
    nulo = False
        
    #retorna archvivo con lsita de errores
    return registros_erroneos


