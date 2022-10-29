import json

with open('estado_act.json', 'w') as archivo:

    json.dump(estado_act,archivo)

with open('estado_act', 'r') as archivo:

    libreria_leida=json.load(archivo)

libreria_leida
