import os
import utils.screenControllers as sc
import utils.validateData as vD
from utils.corefiles import leerjson, escribirjson

JEIEQUIPOS = "data/equipos.json"

def registrarEquipo():
    sc.limpiarPantalla()
    print("=== Registro de Equipo ===")

    nombre = vD.validatetext("Nombre del equipo: ")
    fundacion = vD.validateInt("Fecha de fundación (dia/mes/año): ")
    pais = vD.validatetext("País: ")
    ligaId = vD.validateInt("ID de liga : ")

    nuevo_equipo = {
        "id": id_equipo(),
        "nombre": nombre,
        "fundacion": fundacion,
        "pais": pais,
        "liga_id": ligaId
    }

    equipos = leerjson(JEIEQUIPOS)
    equipos.append(nuevo_equipo)
    escribirjson(JEIEQUIPOS, equipos)

    print("Equipo registrado correctamente.")


def listaEquipos():
    sc.limpiarPantalla()
    print("=== Lista de Equipos Registrados ===\n")

    equipos = leerjson(JEIEQUIPOS)
    if not equipos:
        print("No hay equipos registrados")
    else:
        for equipo in equipos:
            print(f"- ID: {equipo['id']}, Nombre: {equipo['nombre']}, País: {equipo['pais']}, Fundación: {equipo['fundacion']}, Liga ID: {equipo['ligaId']}") 

def id_equipo():
    equipos = leerjson(JEIEQUIPOS)
    if not equipos:
        return 1
    ult_id = max(e["id"] for e in equipos)
    return ult_id + 1