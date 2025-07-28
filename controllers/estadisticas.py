import utils.screenControllers as sc
from utils.corefiles import readJson
from app.config import JEIEQUIPOS, JEIJUGADORES, JTRANSFERENCIAS
 
def mostrarEstadisticas():                                                       #funcion para mostrar las estadisticas generales
    sc.limpiarPantalla() 
    print("         Estadísticas  ")

    equipos = readJson(JEIEQUIPOS)                                               #llamar a los Json para que los lea
    jugadores = readJson(JEIJUGADORES)
    transferencias = readJson(JTRANSFERENCIAS)

    total_equipos = len(equipos)                                                  #Contar la cantidad de equipos
    print(f"Equipos registrados: {total_equipos}")

 
    total_jugadores = len(jugadores)
    print(f"Total de jugadores registrados: {total_jugadores}")                   # contar la cantidad de jugadores


    print(" Jugadores por equipo:")
    for equipo in equipos:                                                         # Bucle para que cuente la cantidad de jugadores por cada equipo
        equipo_id = equipo.get("id")
        equipo_nombre = equipo.get("nombre", "Equipo sin nombre")

       
        cantidad = sum(1 for j in jugadores if str(j.get("equipo_id")) == str(equipo_id))     #Funciona para contar la cantidad de jugadores  guardados en equipos id

        print(f"- {equipo_nombre}: {cantidad} jugador(es)")

    total_transferencias = len(transferencias)                                       #Para mostrar cuantas transfeerencias se han hecho
    print(f"Total de transferencias : {total_transferencias}")
