#import os
import utils.screenControllers as sc
from controllers import equipos, jugadores, torneos, tranferencias, estadisticas


 
def menuTorneos():                                      #Menu de Gestion de Torneos
    while True:
        sc.limpiarPantalla()
        print("       Gestión de Torneos Internacionales de Fútbol ")
        print("1. Registrar equipo")
        print("2. Listar equipos")
        print("3. Registrar jugador")
        print("4. Listar jugadores")
        print("5. Administrar Torneos")
        print("6. Transferencia de jugador (venta o préstamo)")
        print("7. Ver estadísticas")
        print("0. Salir")
        opcion = input("Elija una opción: ")

        match opcion:
            case "1":
                equipos.registrarEquipo()              #funcion desde controllers para poder registrar un equipo
            case "2":
                equipos.listaEquipos()                 #funcion desde controllers para poder ver la lista de los equipos
            case "3":
                jugadores.registrarJugador()           #funcion desde controllers para poder registrar un jugador
            case "4":
                jugadores.listaJugadores()             #funcion desde controllers para poder ver la lista de los jugadores
            case "5":
                while True:
                    sc.limpiarPantalla()
                    print("       ADMINISTRACIÓN DE TORNEOS ")
                    print("1. Registrar partido")
                    print("2. Ver tabla de posiciones")
                    print("0. Volver al menú principal")

                    subOpcion = input("Seleccione una opción: ")

                    match subOpcion:
                        case "1":
                            torneos.registrarPartido()   #Funcion para registrar goles a los diferentes equipos como ejercicio de ligabetplay  (pj, pg, pe, pp, gf, gc, pts)
                        case "2":
                            torneos.tablaPosiciones()  # Función para ver la tabla de estadisticas de torneo con tabulate
                        case "0":
                            break
                        case _:
                            print("Opcion invalida.")        
                        
                    input("Presione para continuar. . . . ")    
            
            case "6":
                tranferencias.hacerTransferencias()    #Funcion para realizar las transferencias entre jugadores ya se por venta o por pretamo
            case "7":
                estadisticas.mostrarEstadisticas()     #Funcion para mostrar las estadisticas generales
            case "0":
                print("Saliendo del programa")
                break
            case _:
                print("Opción inválida")

        input("Presione para continuar. . . . ")       #pausa

if __name__ == "__main__":
    menuTorneos()