from tad_cola_trabajos import *
from tad_trabajo import *


def main():
    cola = crearCola()
    while True:
        print("--------"*6 + "\nPrograma gestion de impresiones:\n" + "--------"*6)
        print("\n [ 1 ] - Recepción de Documentos.\n [ 2 ] - Cambio de Prioridad Individual.\n [ 3 ] - Procesar Impresión.\n [ 4 ] - Visualización de la Cola de Impresión.\n [ 5 ] - Reajuste masivo por Fecha.\n [ 6 ] - Filtrado por Formayo y Franja Horaria.S\n [ 7 ] - Salir")
        
        
        opcion = int(input("Seleccione la opción que desea utilizar:"))

        match opcion:
            case 1:
                agregarTrabajo(cola)
            case 2:
                cambioDePrioridad(cola)
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
                

#Inciso 1
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
        print("Error: Id ingresado no es valido")


#Inciso 2
def cambioDePrioridad(cola):
    #Averiguamos si la cola esta vacia (mo hay ningun elemento)
    if colaVacia(cola):
        print("La cola está vacía.")
        return
    
    #Preparamos ciertos datos como el idBuscado, preparamos auxiliares.
    idBuscado = int(input("Ingrese el ID de Trabaji que desea modificar: "))
    idEncontrado = False
    cola_auxiliar = crearCola()

    #Mientras la cola no este vacia, recorremos cada posicion buscando el id de trabajo
    while not colaVacia()
        trabajo= desencolar(cola)

        if verId(trabajo) == idBuscado :
            nuevaPrioridad = input("Ingrese la nueva prioridad (n: Normal / e: Express): ")

            if nuevaPrioridad == "n" or nuevaPrioridad == "e":
                modPrioridad(trabajo, nuevaPrioridad)
                print("Cambio exitoso! Prioridad Actualizada.")
                idEncontrado= True
            else:
                print("Error: Prioridad no válida. No se realizaron cambios. ")

        encolar(cola_auxiliar, trabajo)

        if not idEncontrado:
            print(f"No se encontró ningún trabajo con el ID {idBuscado}. ")

    #Aca la cola original vuelve a ser guardada, ya con los cambios modificados correspondientes
    while not colaVacia(cola_auxiliar):
        encolar(cola, desencolar(cola_auxiliar))






if __name__ == "__main__":
    main()
