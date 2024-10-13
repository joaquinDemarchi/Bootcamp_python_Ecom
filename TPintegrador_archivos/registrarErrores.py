
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
        
        if registro['sexo'] not in ['M', 'F']:
            registros_erroneos.append((i, registro, "Sexo inválido"))
            
        if registro['vacuna'] not in ['Moderna', 'Sputnik', 'Astrazaneca', 'Sinopharm', 'Pfizer']:
            registros_erroneos.append((i, registro, "Vacuna inválida"))
            
        if registro['jurisdiccion_residencia'] not in jurPosibles:
            registros_erroneos.append((i, registro, "Jurisdiccion invalida"))
        
        # Verificar valores nulos
        for campo in registro:
            if registro[campo] == '':
                registros_erroneos.append((i, registro, f"{campo} es nulo"))
        
    #retorna lista de  
    return registros_erroneos


