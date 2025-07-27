import os
import utils.screenControllers as sc
import utils.validateData as vD
from utils.corefiles import readJson, writeJson
from app.config import JEIEQUIPOS

def registrarEquipo():                                 #funcion para registrar equipos
    sc.limpiarPantalla()
    print("=== Registro de Equipo ===")

    nombre = vD.validatetext("Nombre del equipo: ")
    fundacion = input("Fecha de fundación (dia/mes/año): ")
    pais = vD.validatetext("País: ")
    ligaId = vD.validateInt("ID de liga : ")

    nuevo_equipo = {                                  #forma en la cual se va a guardar en el Json
        "id": id_equipo(),
        "nombre": nombre,
        "fundacion": fundacion,
        "pais": pais,
        "ligaId": ligaId
    }

    equipos = readJson(JEIEQUIPOS)
    equipos.append(nuevo_equipo)
    writeJson(JEIEQUIPOS, equipos)                   #Guardar equipos en el Json

    print("Equipo registrado correctamente.")


def listaEquipos():                                   #funcion para mostrar la lista de los equipos que fueron ya creados
    sc.limpiarPantalla()
    print("=== Lista de Equipos Registrados ===\n")

    equipos = readJson(JEIEQUIPOS)
    if not equipos:
        print("No hay equipos registrados")
    else:
        for equipo in equipos:
            print(f"- ID: {equipo['id']}, Nombre: {equipo['nombre']}, País: {equipo['pais']}, Fundación: {equipo['fundacion']}, Liga ID: {equipo['ligaId']}") 

def id_equipo():                                      #Funcion para crear una ID a los equipos la cual se llama en registrarEquipo() "id"= id_equipo
    equipos = readJson(JEIEQUIPOS)
    if not equipos:
        return 1
    ult_id = max(e["id"] for e in equipos)
    return ult_id + 1