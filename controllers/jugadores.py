import utils.validateData as vD
import utils.screenControllers as sc 
from utils.corefiles import readJson, writeJson
from app.config import JEIEQUIPOS, JEIJUGADORES


def registrarJugador():                                      #Funcion para registar jugadores y almacenarlos en JEIJUGADORES
    sc.limpiarPantalla()
    print("         Registro de Jugador  ")

    nombre = vD.validatetext ("Nombre del jugador: ")
    posicion = vD.validatetext("Posición (Portero, Defensa, Delantero): ")
    dorsal = vD.validateInt("Número dorsal: ")

    equipos = readJson(JEIEQUIPOS)
    if not equipos:
        print("No hay equipos registrados")
        return

    print("           Equipos ")
    for equipo in equipos:
        print(f"{equipo['id']}. {equipo['nombre']}")

    equipo_id = input("Ingrese el ID del equipo al que pertenece: ")                            

    if not any(e["id"] == int(equipo_id) for e in equipos):
        print("ID de equipo No existe")
        return

    jugadores = readJson(JEIJUGADORES)
    nuevo_jugador = {
        "id": id_jugador(),
        "nombre": nombre,
        "posicion": posicion,
        "dorsal": dorsal,
        "equipo_id": equipo_id
    }

    jugadores.append(nuevo_jugador)
    writeJson(JEIJUGADORES, jugadores)
    print("Jugador registrado")

def id_jugador():                                             #funcion para crear una ID a cada jugador que se cree
    jugadores = readJson(JEIJUGADORES)
    if not jugadores:
        return 1
    return max(j["id"] for j in jugadores) + 1


def listaJugadores():                                          #Funcion para mostrar el listado de los jugadores
    sc.limpiarPantalla()
    print("       Lista de Jugadores ")

    jugadores = readJson(JEIJUGADORES)
    equipos = readJson(JEIEQUIPOS)

    if not jugadores:
        print(" No hay jugadores registrados.")
        return

    for jugador in jugadores:
        equipo_id = jugador.get("equipo_id")

        equipo_nombre = "Sin equipo"
        for e in equipos:
            if str(e["id"]) == str(equipo_id):  
                equipo_nombre = e["nombre"]    
                break

        print(f"- ID: {jugador['id']}, Nombre: {jugador['nombre']}, Posición: {jugador['posicion']}, Dorsal: {jugador['dorsal']}, Equipo: {equipo_nombre}")
