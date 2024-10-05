#coding: latin1
import requests
# from pip.vendor import requests

api_url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(api_url)

#CREATE
iD = int(input('Cual es el id del programador'))
dni = input('Cual es el dni del programador')
nombre = input('Cual es el nombre')
apellidos = input('Cuales son los apellidos')
telefono = int(input('Cual es el telefono'))
especialidad = input('Cual es la especialidad')

todo = {'id': iD, 'dni': dni, 'nombre': nombre, 'apellidos': apellidos, 'telefono': telefono, 'especialidad': especialidad}
response = requests.post(api_url, json=todo)
print(response.status_code)
print(response.json())

#READ
iD = int(input('Cual iD deseas obtener?'))
apiRead = "https://jsonplaceholder.typicode.com/todos/" + str(iD)
response = requests.get(api_url)
print(response.json())

#UPDATE 
#put
idMod = int(input('Cual id quieres modificar'))
dni = input('Cual es el dni del programador')
nombre = input('Cual es el nombre')
apellidos = input('Cuales son los apellidos')
telefono = int(input('Cual es el telefono'))
especialidad = input('Cual es la especialidad')

todo = {'id': iD, 'dni': dni, 'nombre': nombre, 'apellidos': apellidos, 'telefono': telefono, 'especialidad': especialidad}
response = requests.put(api_url, json=todo)
print(response.status_code)
print(response.json())

#patch
idMod = int(input('Cual id quieres modificar'))
todo

while True:
    modo = int(input('¿Qué quieres modificar? (1: Dni, 2: Nombre, 3: Apellidos, 4: Telefono,  5: Especialidad, 0: Salir)'))

    if modo == 1:
        dni = input('Cual es el dni del programador: ')
        todo = {'dni': dni}
        break
    elif modo == 2:
        nombre = input('Cual es el nombre: ')
        todo = {'nombre': nombre}
        break
    elif modo == 3:
        apellidos = input('Cuales son los apellidos: ')
        todo = {'apellidos': apellidos}
        break
    elif modo == 4:
        telefono = int(input('Cual es el telefono: '))
        todo = {'telefono': telefono}
        break
    elif modo == 5:
        especialidad = input('Cual es la especialidad: ')
        todo = {'especialidad': especialidad}
        break
    elif modo == 0:
        print('Saliendo')
        break
    else:
        print('Esa opción no es válida. Por favor, intenta de nuevo.')

response = requests.put(api_url, json=todo)
print(response.status_code)
print(response.json())

# DELETE
iD = int(input('Cual ID deseas eliminar'))
api = "https://jsonplaceholder.typicode.com/todos/" + str(id)
response = requests.delete(api_url)
print(response.status_code)
print(response.json())