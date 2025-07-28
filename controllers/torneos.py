import utils.screenControllers as sc
from utils.corefiles import readJson, writeJson
from utils.validateData import validateInt
from app.config import JTORNEOS, JEIEQUIPOS
import tabulate 

def registrarPartido():                                          #Funcion para poder administrar torneos y poner golees a cada equipo
    sc.limpiarPantalla()
    print("         Registrar Partido ")

    equipos = readJson(JEIEQUIPOS)
    if len(equipos) < 2:
        print("Registrar al menos 2 equipos.")
        return

    print("        Equipos disponibles ")
    for e in equipos:
        print(f"{e['id']}. {e['nombre']}")

    id_local = validateInt("ID del equipo local: ")
    id_visita = validateInt("ID del equipo visitante: ")

    if id_local == id_visita:
        print("Un equipo no puede jugar contra el mismo.")
        return

    equipoLocal = next((e for e in equipos if e["id"] == id_local), None)
    equipoVisitante = next((e for e in equipos if e["id"] == id_visita), None)

    if not equipoLocal or not equipoVisitante:
        print("Uno o los dos equipos no existen.")
        return

    golesLocal = validateInt(f"Goles de {equipoLocal['nombre']}: ")
    golesVisitante = validateInt(f"Goles de {equipoVisitante['nombre']}: ")

    tabla = readJson(JTORNEOS)
    tabla = actualizarEstadisticas(tabla, equipoLocal['nombre'], golesLocal, golesVisitante)           #actualixa las estadisticas 
    tabla = actualizarEstadisticas(tabla, equipoVisitante['nombre'], golesVisitante, golesLocal)

    writeJson(JTORNEOS, tabla)
    print("Partido registrado y estadísticas actualizadas.")

def actualizarEstadisticas(tabla, nombre_equipo, gf, gc):                         #funcion para actualziar estadisticas a cada equipo
    entry = next((e for e in tabla if e["equipo"] == nombre_equipo), None)

    if not entry:
        entry = {
            "equipo": nombre_equipo,
            "pj": 0, "pg": 0, "pe": 0, "pp": 0,
            "gf": 0, "gc": 0, "pts": 0
        }
        tabla.append(entry)

    entry["pj"] += 1
    entry["gf"] += gf
    entry["gc"] += gc

    if gf > gc:
        entry["pg"] += 1
        entry["pts"] += 3
    elif gf == gc:
        entry["pe"] += 1
        entry["pts"] += 1
    else:
        entry["pp"] += 1

    return tabla

def tablaPosiciones():
    sc.limpiarPantalla()
    print("Proximamente Nueva Funcionalidad  (Fase Beta)")