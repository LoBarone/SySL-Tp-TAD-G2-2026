from Tp1.tad_cola_trabajos import *
from tad_trabajo import *


def main():
    cola = crearCola()
    while True:
        print("--------"*6 + "\nPrograma gestion de impresiones:\n" + "--------"*6)
        print("\n [ 1 ] - Cargar Documento\n [ 2 ] - Opcion 2\n [ 3 ] - Opcion 3\n [ 4 ] - Opcion 4\n [ 5 ] - Opcion 5\n [ 6 ] - Opcion 6\n [ 7 ] - Salir")
        # Cambiar nombre opcion por el nombre correcto (me dio paja xd) -lolo
        
        opcion = int(input("Seleccione la opción que desea utilizar:"))

        match opcion:
            case 1:
                agregarTrabajo(cola)
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                print("Fin del programa!")
                break
            case _:
                print("Error: La opción que usted seleccionó es invalida. ")
                

def agregarTrabajo(cola):
    print("--- Carga de Nuevo Trabajo ---")
    jobId = int(input("Ingrese el ID (0 para cancelar): "))
    
    if jobId > 0:
        nombDocu = input("Ingrese el Nombre: ")
        tipo = input("Ingrese el Tipo: ")
        cantPag = int(input("Ingrese la cantidad de Páginas: "))
        nivel = input("Ingrese Nivel de Prioridad: ")
        dia = int(input("Día: "))
        mes = int(input("Mes: "))
        año = int(input("Año: "))
        hora = int(input("Hora: "))
        minuto = int(input("Minuto: ")) 
        t = crearTrabajo()
        cargarTrabajo(t, jobId, nombDocu, tipo, cantPag, nivel, año, mes, dia, hora, minuto)
        encolar(cola, t)
        print("Trabajo agregado con éxito.")
    else:
        raise Exception("Error: Id ingresado no es valido")


if __name__ == "__main__":
    main()
