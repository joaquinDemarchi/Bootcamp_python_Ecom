
def dividirXTipVacuna(registros):
    distribucion_vacunas = {'Moderna': 0, 'Sputnik': 0, 'Astrazeneca': 0, 'Sinopharm': 0, 'Pfizer': 0}

    for registro in registros:
        vacuna = registro['vacuna']
        if vacuna in distribucion_vacunas:
            distribucion_vacunas[vacuna] += 1
    
    #retorna un dic 
    return distribucion_vacunas