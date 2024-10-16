# Tarea Jueves:
# 1) Validador
# 2) Clase Triangulo con metodos perimetro y area.

# UML Modelado de clases.
# clase: ValidadorDNI
#      - lista_documentos
#      - lista_documentos_validos
#      - lista_documentos_invalidos
#
#      + validar_documento:documento
#      + todo_es_un_numerico:valor
#      + rango_valido:valor
#      + constructor: lista_documentos
#      + obtener_dni_validos:
#      + obtener_dni_invalidos:

dnis = ['40773838','4077aaa8','40766838','407738','hola']

class ValidadorDNI:
    
    def __init__(self,listaDnis): #,listaDnisIN, listaDnisVAL):
        self.listaDnis = listaDnis
        #self.listaDnisIN = listaDnisIN
        #self.listaDnisVAL = listaDnisVAL
    
    def DnisDigito(self):
        for dni in self.listaDnis:
            if (dni.isdigit()):
                print(f"El dni {dni} es un digito")
            else:
                print(f"El dni {dni} no es un digito")
    
    def DnisCantCaracCorr(self):
        for dni in self.listaDnis:
            if (len(dni) == 8 or len(dni) == 7):
                print(f"El dni {dni} tiene numero de caracteres correcto")
            else:
                print(f"El dni {dni} tiene numero de caracteres incorrecto")
    
    def DnisValidos(self):
        dniValidos = []
        
        for dni in self.listaDnis:
            if (dni.isdigit() and (len(dni) == 8 or len(dni) == 7)):
                #print(f"El dni {dni} es valido")
                dniValidos.append(dni)
            
        print(dniValidos)
    
    def DnisInvalidos(self):
        dniInvalidos = []
        
        for dni in self.listaDnis:
            if not (dni.isdigit() and (len(dni) == 8 or len(dni) == 7)):
                #print(f"El dni {dni} es invalido")
                dniInvalidos.append(dni)
            
        print(dniInvalidos)


lista1 = ValidadorDNI(listaDnis = dnis)

lista1.DnisDigito()
lista1.DnisCantCaracCorr()
print("dnis validos")
lista1.DnisValidos()
print("dnis invalidos")
lista1.DnisInvalidos()