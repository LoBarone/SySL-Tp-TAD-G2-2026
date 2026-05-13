from tad_cola_trabajos import *
from tad_trabajo import *

def main():
    cola = crearCola()
    while True:
        print("--------"*6 + "\nPrograma gestion de impresiones:\n" + "--------"*6)
        print("\n [ 1 ] - Recepción de Documentos.\n [ 2 ] - Cambio de Prioridad Individual.\n [ 3 ] - Procesar Impresión.\n [ 4 ] - Visualización de la Cola de Impresión.\n [ 5 ] - Reajuste masivo por Fecha.\n [ 6 ] - Filtrado por Formato\n [ 7 ] - Filtrado por Franja Horaria\n [ 8 ] - Salir")
        
        
        opcion = int(input("Seleccione la opción que desea utilizar: "))

        match opcion:
            case 1:
                agregarTrabajo(cola)
            case 2:
                cambioDePrioridad(cola)
            case 3:
                pass
            case 4:
                visualizacionCola(cola)
            case 5:
                reajusteMasivoPorFecha(cola)
            case 6:
                pass
            case 7:
                pass
            case 8:
                print("Fin del programa!")
                break
            case 9:
            # Lo agrego para debug trabajo, id, nombre, formato, paginas, prioridad, año, mes, dia, hora, minuto
                t1 = [1, "juan", "pdf", 1, "e", date(1, 1, 1), time(00, 00)]
                t2 = [1, "jorge", "algo", 1, "n", date(1, 1, 1), time(00, 00)]
                t3 = [1, "qsy", "pdf", 1, "b", date(1, 1, 1), time(00, 00)]
                cola.append(t1)
                cola.append(t2)
                cola.append(t3)
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
            nivel =(input("Niveles de Prioridad \n[ b ] - Baja \n[ e ] - Express \n[ n ] - Normal\nIngrese el nivel de prioridad: ")).lower()
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



def visualizacionCola(cola):
    print("--- Visualización de Cola ---")
    #Verifico que la cola no este vacia, si no esta vacia, continua la ejecución.
    if colaVacia(cola):
        print("No hay trabajos pendientes de impresión. ")
        return
    else:
        #Crea una cola auxiliar para no perder los datos
        colaaux = crearCola()
        #Copia los datos de la cola (original) a la cola (auxiliar)
        copiarCola(colaaux, cola)
    
    cont = 1
    while not colaVacia(colaaux):
        #Desencolo elemento por elemento
        t = desencolar(colaaux)

        #Renombramos a "e" y "n" por EXPRESS y NORMAL
        prioridad = verPrioridad(t)
        match prioridad:
            case "b":
                prioridad = "Basica"
            case "n":
                prioridad = "Normal"
            case "e":
                prioridad = "Express"

        #Impresión de los trabajos
        print(f" {cont}. -Job ID: {verId(t)}")
        print(f" - Formato: {verFormato(t)}")
        print(f" - Documento: {verNombre(t)}")
        print(f" - Cantidad de páginas: {verPaginas(t)}")
        print(f" - Prioridad: {prioridad}")
        print(f" - Fecha: {verDia(t):02d}/{verMes(t):02d}/{verAño(t):02d}")
        print(f" - Hora: {verHora(t):02d}:{verMinuto(t):02d}")
        print("---"*6)

        cont += 1

    print("------"*4)


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



def reajusteMasivoPorFecha(cola):
# Dado un mes, actualiza la prioridad a baja a todos los trabajos del mismo.
    if not cola:
        print("Error: La cola esta vacia!")
        return
        

    while True:
        try:
            mesDado = int(input("Ingrese el mes para el que desea bajar la prioridad: "))
            if not (12 >= mesDado >= 1):
                print("Ingrese un mes valido")
                continue

            break
        except ValueError:
            print("Ingrese un valor valido")
    
    trabajos = colaALista(cola)
    for trabajo in trabajos:
        if verMes(trabajo) == mesDado:
            modPrioridad(trabajo, "b")

    
    copiarCola(cola, listaACola(trabajos))
  


if __name__ == "__main__":
    main()
