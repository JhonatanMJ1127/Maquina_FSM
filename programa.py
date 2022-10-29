import json
with open('libreria.json', 'w') as archivo:
    json.dump(libreria,archivo)
    with open('libreria.json', 'r') as archivo:
    libreria_leida=json.load(archivo)
libreria_leida
