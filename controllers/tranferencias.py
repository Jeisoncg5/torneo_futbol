import utils.screenControllers as sc
from utils.corefiles import readJson, writeJson
from utils.validateData import validateInt
from app.config import JTRANSFERENCIAS, JEIJUGADORES, JEIEQUIPOS
from datetime import datetime

def hacerTransferencias():                                 #funcion para hacer transferencias de jugadores
    sc.limpiarPantalla()
    print("   Transferencia de Jugador ")

    jugadores = readJson(JEIJUGADORES)                        #Lee los jugadores guardados en JJUGADORES
    equipos = readJson(JEIEQUIPOS)                          #Lee los equipos guardados en JEIEQUIPOS

    if not jugadores:
        print("No hay jugadores registrados.")
        return

    print("        Jugadores disponibles ")
    for j in jugadores:
        print(f"{j['id']}. {j['nombre']} (Equipo ID: {j['equipo_id']})")
    
    id_jugador = validateInt("ID del jugador a transferir: ")
    jugador = next((j for j in jugadores if j["id"] == id_jugador), None)

    if not jugador:
        print(" Jugador no existe")
        return
    
    print("      Equipos ")
    for e in equipos:
        print(f"{e['id']}. {e['nombre']}")

    id_destino = validateInt("ID del equipo destino: ")

    if id_destino == jugador["equipo_id"]:
        print("El jugador ya pertenece a ese equipo.")
        return

    equipo_origen = next((e["nombre"] for e in equipos if e["id"] == jugador["equipo_id"]), "Desconocido")
    equipo_destino = next((e["nombre"] for e in equipos if e["id"] == id_destino), "Desconocido")

    tipo = validateInt("Tipo de transferencia (1. Venta   2. Prestamo): ")

    if tipo not in [1,2]:
        print("Tipo de Tranferencia inválida.")
        return
    
    transferencias = readJson(JTRANSFERENCIAS)


    nueva = {
        "id_jugador": jugador["id"],
        "nombre_jugador": jugador["nombre"],
        "equipo_origen": equipo_origen,
        "equipo_destino": equipo_destino,
        "tipo": tipo,
        "fecha": datetime.today().strftime("%d/%m/%Y")
    }

    transferencias.append(nueva)
    writeJson(JTRANSFERENCIAS, transferencias)

    if tipo == 1:
        jugador["equipo_id"] = id_destino
        writeJson(JEIJUGADORES, jugadores)
    elif tipo == 2:
        print("Jugador prestado")

    print("Transferencia registrada correctamente.")