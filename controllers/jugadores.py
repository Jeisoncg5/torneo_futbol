import utils.validateData as vD
import utils.screenControllers as sc 
from utils.corefiles import leerjson, escribirjson


JEIJUGADORES = "data/jugadores.json"
JEIEQUIPOS = "data/equipos.json"

def registrarJugador():
    sc.limpiarPantalla()
    print("         Registro de Jugador  ")

    nombre = vD.validatetext ("Nombre del jugador: ")
    posicion = vD.validatetext("Posición (Portero, Defensa, Delantero): ")
    dorsal = vD.validateInt("Número dorsal: ")

    equipos = leerjson(JEIEQUIPOS)
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

    jugadores = leerjson(JEIJUGADORES)
    nuevo_jugador = {
        "id": idJugador(),
        "nombre": nombre,
        "posicion": posicion,
        "dorsal": dorsal,
        "equipo_id": equipo_id
    }

    jugadores.append(nuevo_jugador)
    escribirjson(JEIJUGADORES, jugadores)
    print("Jugador registrado")

def listaJugadores():
    sc.limpiarPantalla()
    print("            Lista de Jugadores ")

    jugadores = leerjson(JEIJUGADORES)
    equipos = leerjson(JEIEQUIPOS)

    if not jugadores:
        print("No hay jugadores registrados")
        return

    for jugador in jugadores:
        equipo = next((e["nombre"] for e in equipos if e["id"] == jugador["equipo_id"]), "Sin equipo")
        print(f"- ID: {jugador['id']}, Nombre: {jugador['nombre']}, Posición: {jugador['posicion']}, Dorsal: {jugador['dorsal']}, Equipo: {equipo}")

def idJugador():
    jugadores = leerjson(JEIJUGADORES)
    if not jugadores:
        return 1
    return max(j["id"] for j in jugadores) + 1
