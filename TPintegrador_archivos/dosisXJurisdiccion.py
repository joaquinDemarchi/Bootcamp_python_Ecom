def dosisXJurisdiccion(registros):

    dosis_por_jurisdiccion = {"Buenos Aires": 0, "CABA": 0, "Catamarca": 0, "Chaco": 0, "Chubut": 0, "Córdoba": 0, "Corrientes": 0, "Entre Ríos": 0, "Formosa": 0, "Jujuy": 0, "La Pampa": 0, "La Rioja": 0, "Mendoza": 0, "Misiones": 0, "Neuquén": 0, "Río Negro": 0, "Salta": 0, "San Juan": 0, "San Luis": 0, "Santa Cruz": 0, "Santa Fe": 0, "Santiago del Estero": 0, "Tierra del Fuego": 0, "Tucumán": 0}

    for registro in registros:
        jurisdiccion = registro['jurisdiccion_residencia']
        if jurisdiccion in dosis_por_jurisdiccion:
            dosis_por_jurisdiccion[jurisdiccion] += 1

    #retorna un dic  
    return dosis_por_jurisdiccion