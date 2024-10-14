
ARCHIVO CSV

baseMuestra.csv

Se creo un archivo de muestra que replica el la estructura y formato de los datos del CSV proporcionado en el trabajo. Por cuestiones de practicidad en el codigo se trabajara con el mismo. 

MODULOS

listarRegistros.py 

En ete modulo se encuentra la funcion que recibe el CSV y transforma sus datos a una lista de diccionarios.
Para eso lo primero que hago es extraer el encabezado Y creo la lista que almacenara los diccionarios. Luego recorro las lineas del archivo, les quito los espacios blancos y las separo por las comas que se encuentren en las mismas.
Por ultimo con zip combino el encabezado y los datos de las filas, (el encabezado sera la clave del diccioanrio y los datos los valores). Luego de combinados transformo ese iterable devuelto en diccionarios, los cuales los agrego a mi lista.


dividirXGenero.py, dividirXTipVacuna.py, segDosisXJur.py, dosisXJurisdiccion.py


En este modulos lo que hago es primero que hago en la funcion principal es defifir un diccionario que almacenara el conteo de los distintos tipos de segmentaciones que realizare de los registros luego recorrere cada registro e ir aumentando dichos contadores cuando encuentre coincidencias. Por ultimo la funciones devolveran en un diccionario cual se podra acceder a los nombres de las segmentaciones y cuantos registros coinciden con cada una de ellas.


refuerzosAMas60.py

En este modulo realizo un procemiento muy similiar al anterior, en lo unico que cambio el codigo es en la forma en la que valido si el datos del registro ingresado es correcto. 
Para eso extrae el primer caracter de dicho dato y compara si el mismo esta dentro de una lista que contempla todas las posibles formas que podria comenzar un registro que cumpla con las condiciones definidas.
Ademas en este caso la funcion solo devuelve un entero, no una lista como los demas.


registrarErrores.py 

Esta funcion devuelve una lista de tuplas que contiene: el nro de linea del registro erroneo, el registro propiamente dicho y un mensaje que indica el tipo de error de dicho registro.  
La funcion al igual que las demas la lista de los dict que continen todos los datos de los registros. Itera la misma usando un for y un enumerate que nos ayudara a agregarle un idice al error.
Primero defino la variable nulo que me servira para validar que el campo no esta vacio, para no tener dos errores por el mismo campo. 
Dentro del for primero valido justamente que el campo no sea nulo, si lo es agrego un error a la lista.
En los campos siguiente valido que los datos de los registros sean exactamente iguales a la opciones previamente definidas.
En el caso del grupo etario baso la validez en la inclusion de algunos de los caracteres que se visualizo en los ejemplos que siempre estan presentes en el campo.


ARCHIVO PRINCIPAL

main.py

Aqui lo primero que hago es importar todos los modulos anteriormente mencionados.
A continuacion guardo en una variable los registros del CSV transformados a lista de de dict.
Luego creo un dict de dicts en donde se guardaran todas las opciones del menu con el que interactuara el usuario.
Creo un ciclo que reccorra dicho dict e imprima todas las opciones en pantalla.
Defino un mensaje estandar para todas las opciones disponibles
Y por ultimo defino cada uno de los mensajes personalizados que tendran cada opcion disponible en el menu los cuales contendran los resultados de cada solicitud obtenidos por las distintas funciones declaradas en los modulos anteriores.

