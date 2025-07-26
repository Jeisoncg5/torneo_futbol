import os
import json

def leerjson(ruta):
    if not os.path.exists(ruta):
        return []
    with open(ruta, 'r', encoding='utf-8') as file:
        return json.load(file)

def escribirjson(ruta, data):
    with open(ruta, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)