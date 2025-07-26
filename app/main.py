#import os
import utils.screenControllers as sc
from controllers import equipos
from controllers import jugadores
#from controllers import tranferencias
#from controllers import estadisticas


def menuTorneos():
    while True:
        sc.limpiarPantalla()
        print("       Gestión de Torneos Internacionales de Fútbol ")
        print("1. Registrar equipo")
        print("2. Listar equipos")
        print("3. Registrar jugador")
        print("4. Listar jugadores")
        print("5. Transferencia de jugador (venta o préstamo)")
        print("6. Ver estadísticas")
        print("0. Salir")

        opcion = input("Elija una opción: ")

        match opcion:
            case "1":
                equipos.registrarEquipo()
            case "2":
                equipos.listaEquipos()
            case "3":
                jugadores.registrarJugador()
            case "4":
                jugadores.listaJugadores()
            case "5":
                pass
            case "6":
                pass
            case "0":
                print("Saliendo del programa")
                break
            case _:
                print("Opción inválida")

        input("Presione para continuar. . . . ")

if __name__ == "__main__":
    menuTorneos()