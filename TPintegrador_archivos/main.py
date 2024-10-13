
#importacion de modulos
from modulos.registrarErrores import *
from modulos.dividirXGenero import *
from modulos.dividirXTipVacuna  import *
from modulos.dosisXJurisdiccion  import *
from modulos.segDosisXJur  import *
from modulos.refuerzosAMas60  import *
from modulos.listarRegistros  import *

registros = listarRegistros('baseMuestra.csv') 


#dic en donde se guardan opciones del menu a imprimir
MENU_PRINCIPAL= {
    1: {"nombre" : "Mostrar la distribucion de vacunas por Genero"},
    2: {"nombre" : "Mostrar la distribucion de vacunas por Tipo de vacuna"},
    3: {"nombre" : "Mostrar la distribucion de vacunas por jurisdiccion"},
    4: {"nombre" : "Mostrar la distribucion de aplicacion de segundas dosis por jurisdiccion"},
    5: {"nombre" : "Mostrar cantidad de mayores de 60 años que recibieron dosis de refuerzo"},
    6: {"nombre" : "Mostrar registro de errores"},
    7: {"nombre" : "Salir",}
}

while True:
    
    print("\nIngrese una de las siguientes opciones:\n")
    
    #imprime todas las opciones del menu, las saca del dic
    for indice, opcionDic in MENU_PRINCIPAL.items():
        print(f"{indice} - {opcionDic['nombre']}")

    mensajeContinuar = "Presiona ENTER para continuar.\n"
    
    opcion = int(input("\n--->"))
    
    #opciones con mensajes personalizados para que tipo de info solicitada
    if opcion == 1:
        print("\nDistribución por Género:\n")
        print(f"Masculino: {dividirXGenero(registros)['M']}")
        print(f"Femenino: {dividirXGenero(registros)['F']}\n")
        #print(f"{MENU_PRINCIPAL[1]['metodo']['F']}")
        print(f"\n{mensajeContinuar}")
        input()
        
    elif opcion == 2:
        total_vacunas = sum(dividirXTipVacuna(registros).values())
        print("\nDistribución por Tipo de vacuna:\n")
        for vacuna, cantidad in dividirXTipVacuna(registros).items():
            proporcion = (cantidad / total_vacunas) * 100
            print(f"{vacuna}: {round(proporcion)}%") 
        print(f"\n{mensajeContinuar}")
        input()
    
    elif opcion == 3:
        print("\nDosis por jurisdiccion:\n")
        for jurisdiccion, cantidad in dosisXJurisdiccion(registros).items():
            if cantidad != 0:
                print(f"{jurisdiccion}: {cantidad}")  
        print(f"\n{mensajeContinuar}")
        input()
    
    elif opcion == 4:
        print("\nSegunda Dosis por Jurisdicción:\n")
        for jurisdiccion, cantidad in segDosisXJur(registros).items():
            if cantidad != 0:
                print(f"{jurisdiccion}: {cantidad}")  
        print(f"\n{mensajeContinuar}")
        input()
    
    elif opcion == 5:
        print(f"\nPersonas mayores de 60 años que recibieron dosis de refuerzo: {refuerzosAMas60(registros)}\n")
        print(f"\n{mensajeContinuar}")
        input()
    
    elif opcion == 6:
        print("\nArchivos de errores generado correctamente\n")
        with open('registroDeErrores.csv', 'w', encoding='utf-8') as f:  
            f.write('Índice,Registro,Observación\n')
            for indice, registro, observacion in registrarErrores(registros):
                f.write(f"{indice},{registro},{observacion}\n") 
                
        print(f"\n{mensajeContinuar}")
        input()
    
    elif opcion == 7:
        print("\nNos vemos, Adios")
        break
    
    else:
        print("La opcion ingresada es incorrecta")
        continue
