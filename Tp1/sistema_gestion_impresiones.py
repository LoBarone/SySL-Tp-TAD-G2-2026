from tad_cola_trabajos import *
from tad_trabajo import *


def main():
    cola = crearCola()
    while True:
        print("--------"*6 + "\nPrograma gestion de impresiones:\n" + "--------"*6)
        print("\n [ 1 ] - Recepción de Documentos.\n [ 2 ] - Cambio de Prioridad Individual.\n [ 3 ] - Procesar Impresión.\n [ 4 ] - Visualización de la Cola de Impresión.\n [ 5 ] - Reajuste masivo por Fecha.\n [ 6 ] - Filtrado por Formayo y Franja Horaria.S\n [ 7 ] - Salir\n")
        
        
        opcion = int(input("Seleccione la opción que desea utilizar: "))

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
                

def agregarTrabajo(cola):
    print("--- Carga de Nuevo Trabajo ---")
    jobId = int(input("Ingrese el ID (0 para cancelar): "))
    
    if jobId > 0:
        ok=False #corte de control final
        nombDocu = input("Ingrese el Nombre: ")
        if(nombDocu!="")or(nombDocu!=" "):
            tipo = input("Ingrese el Tipo: ")
            cantPag = int(input("Ingrese la cantidad de Páginas: "))
            nivel =(input("Ingrese Nivel de Prioridad [ e ] - Expres - [ n ] - Normal : ")).lower()
            if((nivel=='e')or(nivel=='n')):
                mes = int(input("Mes [ 1 - 12 ]: "))
                if(mes==2):
                    dia = int(input("Día [ 1 - 28 ] : "))
                    if((dia>=1)and(dia<=28)):
                        año=int(input("Ingrese año [2026 en adelante] :"))
                        ok=True
                elif((mes==1)or(mes==3)or(mes==5)or(mes==7)or(mes==8)or(mes==10)or(mes==12)):
                    dia = int(input("Día [ 1 - 31 ] : "))
                    if((dia>=1)and(dia<=31)):
                        año=int(input("Ingrese año [2026 en adelante] :"))
                        ok=True
                elif((mes==4)or(mes==6)or(mes==9)or(mes==11)):
                    dia = int(input("Día [ 1 - 30 ] : "))
                    if((dia>=1)and(dia<=30)):
                        año=int(input("Ingrese año [2026 en adelante] :"))
                        ok=True
                else:
                    print("Error, Mes invalido")
        
                if(ok):
                    if(año>=2026):
                        hora = int(input("Hora [ 0 - 23 ]: "))
                        if((hora>=0)and(hora<=23)):
                            minuto = int(input("Minuto [ 0 - 59 ]: "))
                            if((minuto>=0)and(minuto<=59)):
                                t = crearTrabajo()
                                cargarTrabajo(t, jobId, nombDocu, tipo, cantPag, nivel, año, mes, dia, hora, minuto)
                                encolar(cola, t)
                                print("Trabajo agregado con éxito.")
            else: print("Error: Nivel Invalido")
    else:
        print("Error: Id ingresado no es valido")


def cambioDePrioridad(cola):
    print("--- Cambio de Prioridad Individual ---")
    # Se verifica que la cola este vacía. Si lo está, muestra un mensaje y retorna al menú principal.
    if colaVacia(cola):
        print("La cola está vacía. ")
        return
    
    #Se asignan datos para recorrer la lista
    idABuscar = int(input("Ingrese el ID de Trabajo que desea modificar: "))
    idEncontrado = False

    lista = colaALista(cola)

    #Mientras la cola no este vacía, se recorre la lista buscando el ID que se desea modificar. 
    #Si el ID es encontrado, se le asigna la prioridad y se modifica el trabajo.
    #Si el ID no es encontrado, se muestra un mensaje de error.
    
    #El for recorre la lista usando a t como trabajo (definida anteriormente)
    for t in lista :
        if verId(t) == idABuscar :
            nuevaPrioridad = input("Ingrese la nueva prioridad que desea modificar (n: Normal / e: Express): ").lower()

            if nuevaPrioridad in ["n", "e"]:
                modPrioridad(t, nuevaPrioridad)
                print("Cambio exitoso! Prioridad Actualizada.")
                idEncontrado = True
            else:
                print("Error: Prioridad no válida. No se realizaron cambios. ")
            break

    if not idEncontrado:
        print(f"No se encontró ningún trabajo con el ID {idABuscar}. ")

    for elemento in lista :
        encolar(cola, elemento )


def colaALista(cola):
# Convierte una cola a una lista. Elimina la cola
    lista = []
    while not colaVacia(cola):
        lista.append(desencolar(cola))

    return lista


def listaACola(lista):
# Convierte una lista a una cola.
    cola = crearCola()
    for trabajo in lista:
        encolar(cola, trabajo)

    return cola



if __name__ == "__main__":
    main()
