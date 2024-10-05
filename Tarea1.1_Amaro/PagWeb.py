#coding: latin1
import requests
# from pip.vendor import requests

api_url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(api_url)

#CREATE
iD = int(input('Cual es el id de la pagina web'))
titulo = input('Cual es el titulo de la web')
tematica = input('Cual es la tematica')
url = input('Cuales es la url')
idProg = int(input('Cual es el id del programador'))
todo = {'id': iD, 'titulo': titulo, 'tematica': tematica, 'url': url, 'idProg': idProg}
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
titulo = input('Cual es el titulo de la web')
tematica = input('Cual es la tematica')
url = input('Cuales es la url')
idProg = int(input('Cual es el id del programador'))

todo = {'id': iD, 'titulo': titulo, 'tematica': tematica, 'url': url, 'idProg': idProg}
response = requests.put(api_url, json=todo)
print(response.status_code)
print(response.json())

#patch
idMod = int(input('Cual id quieres modificar'))
todo

while True:
    modo = int(input('¿Qué quieres modificar? (1: Titulo, 2: Tematica, 3: URL, 4: IdProgramador, 0: Salir)'))

    if modo == 1:
        titulo = input('Cual es el titulo de la web')
        todo = {'titulo': titulo}
        break
    elif modo == 2:
        tematica = input('Cual es la tematica')
        todo = {'tematica': tematica}
        break
    elif modo == 3:
        url = input('Cuales es la url')s
        todo = {'url': url}
        break
    elif modo == 4:
        idProg = int(input('Cual es el id del programador'))
        todo = {'idProg': idProg}
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