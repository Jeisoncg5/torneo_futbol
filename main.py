#import os
import utils.screenControllers as sc
from controllers import equipos, jugadores, torneos, tranferencias


 
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
                torneos.registrarPartido()             #Funcion para registrar goles a los diferentes equipos como ejercicio de ligabetplay  (pj, pg, pe, pp, gf, gc, pts)
            case "6":
                tranferencias.hacerTransferencias()    #Funcion para realizar las transferencias entre jugadores ya se por venta o por pretamo
            case "7":
                pass
            case "0":
                print("Saliendo del programa")
                break
            case _:
                print("Opción inválida")

        input("Presione para continuar. . . . ")       #pausa

if __name__ == "__main__":
    menuTorneos()