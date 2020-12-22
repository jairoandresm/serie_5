'''la idea del programa es seleccionar una capacidad del transformador y que el algoritmo le muestre los datos del serie 5
con la idea de anexar mas adelante la interfaz gráfica del transformador'''

import json

trafo_objetivo = str(input('escriba el valor del transformador : '))

'''El comando with open abre el json como una lista de diccionarios, de esta manera
para acceder a un dato específico se debe usar [0]['KVA'] el cero para la lista y el KVA para la llave del diccionario'''

with open('data/TRAFOS.json') as contenido:
    lista_de_datos = json.loads(contenido.read())
    

if trafo_objetivo == '15':
    print(lista_de_datos[0]['KVA'])
elif trafo_objetivo == '30':
    print(lista_de_datos[1])
else:
    print('no coincide')