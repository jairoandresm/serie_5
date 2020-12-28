'''la idea del programa es seleccionar una capacidad del transformador y que el algoritmo le muestre los datos del serie 5
con la idea de anexar mas adelante la interfaz gráfica del transformador'''

import json

trafo_objetivo = str(input('escriba el valor del transformador : '))

'''El comando with open abre el json como una lista de diccionarios, de esta manera
para acceder a un dato específico se debe usar [0]['KVA'] el cero para la lista y el KVA para la llave del diccionario'''

with open('data/TRAFOS.json') as contenido:
    lista_de_datos = json.loads(contenido.read())

#la variable "Posicion" al íncide de la lista que contiene la info del formato json
    
if trafo_objetivo == '15':
    Posicion = 0
elif trafo_objetivo == '30':
    Posicion = 1
elif trafo_objetivo == '45':
    Posicion = 2
elif trafo_objetivo == '75':
    Posicion = 3
elif trafo_objetivo == '112.5':
    Posicion = 4
elif trafo_objetivo == '150':
    Posicion = 5
elif trafo_objetivo == '225':
    Posicion = 6
else:
    print('Seleccione una potencia válida para el trafo en poste')

#los valores del transformador serie 5
print('*' * 30)
print('DIAGRAMA UNIFILAR SERIE 5 DE ACUERDO A CTU516')
print('*' * 30)
print('Capacidad del transformador {} KVA'.format(lista_de_datos[Posicion]['KVA']))
print('Corriente nominal a 11.4 kV = {} A'.format(lista_de_datos[Posicion]['IN_11']))
print('Corriente nominal a 13.2 kV = {} A'.format(lista_de_datos[Posicion]['IN_13']))
print('Calibre de la bajante en cobre = {} AWG'.format(lista_de_datos[Posicion]['COBRE_CALIBRE']))
print('Fusible dual ref {} según CTU515'.format(lista_de_datos[Posicion]['DUAL']))
print('Corriente nominal BT = {} A'.format(lista_de_datos[Posicion]['IN_TRAFO']))
print('*' * 30)
print('Calibre de conductor de cobre 1 Bajante = {}'.format(lista_de_datos[Posicion]['COBRE_UNA_BAJANTE']))
print('Calibre de conductor de cobre 2 Bajantes = {}'.format(lista_de_datos[Posicion]['COBRE_DOS_BAJANTE']))
print('Calibre de conductor de cobre 3 Bajantes = {}'.format(lista_de_datos[Posicion]['COBRE_TRES_BAJANTE']))
print('*' * 30)
print('Calibre de conductor de Al 1 Bajante = {}'.format(lista_de_datos[Posicion]['ALUMINIO_UNA_BAJANTE']))
print('Calibre de conductor de Al 2 Bajantes = {}'.format(lista_de_datos[Posicion]['ALUMINIO_DOS_BAJANTE']))
print('*' * 30)
print('Fusible NH ref = {} y corriente = {} A'.format(lista_de_datos[Posicion]['NH'], lista_de_datos[Posicion]['CORRIENTE_NH']))
print('Portafusible = {} A'.format(lista_de_datos[Posicion]['PORTA_FUSIBLE']))