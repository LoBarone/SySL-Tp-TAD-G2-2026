from tad_cola import *
from tad_trabajo import *
from datetime import datetime

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
                cancelacionPorFormato(cola)
                pass
            case 7:
                subcola = genSubColaHoraria(cola)
                visualizacionCola(subcola)
                pass
            case 8:
                print("Fin del programa!")
                break
            case 9:
            # Lo agrego para debug trabajo, id, nombre, formato, paginas, prioridad, año, mes, dia, hora, minuto
                t1 = [1, "juan", "pdf", 1, "e", date(1, 1, 1), time(00, 00)]
                t2 = [1, "jorge", "algo", 1, "n", date(1, 1, 1), time(10, 00)]
                t3 = [1, "qsy", "pdf", 1, "b", date(1, 1, 1), time(00, 00)]
                cola.append(t1)
                cola.append(t2)
                cola.append(t3)
            case _:
                print("Error: La opción que usted seleccionó es invalida. ")



def agregarTrabajo(cola):
# Agrega un trabajo a la cola
    print(" RECEPCIÓN DE DOCUMENTOS ")
    # Validación de ID, Nombre, Tipo y Páginas
    # Uso de los try y excepts
    try:
        jobId = int(input("Ingrese el ID (0 para cancelar): "))
        if jobId == 0:
            print("Operación cancelada por el usuario.")
            return
        if jobId < 0:
            print("Error")
            return
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return
    
    nombDocu = input("Ingrese el Nombre del documento: ")
    if not nombDocu:
        print("Error: El nombre no puede estar vacío.")
        return

    tipo = input("Ingrese el Tipo de formato (PDF, DOCX, etc.): ")
    if not tipo:
        print("Error: El tipo de formato no puede estar vacío.")
        return

    try:
        cantPag = int(input("Ingrese la cantidad de Páginas: "))
        if cantPag <= 0:
            print("Error: La cantidad de páginas debe ser mayor a 0.")
            return
    except ValueError:
        print("Error: La cantidad de páginas debe ser un número entero.")
        return
    # Validación de Prioridad 
    nivel = input("Prioridad [ b ]-Básica | [ n ]-Normal | [ e ]-Express: ").lower()
    if nivel not in ["b", "n", "e"]:
        print("Error: Tipo de prioridad inválido.")
        return
    while True:
        try:
            fecha = input("Ingrese fecha de envío (DD/MM/AAAA): ")
            # strptime valida bisiestos y días máximos automáticamente 
            fecha_valida = date.strptime(fecha, "%d/%m/%Y").date()
            # Validación de negocio , es para no permitir fechas invalidad , es decir anterior a la actual
            if fecha_valida < date.today():
                print("Inválido: La fecha no puede ser anterior a hoy.")
                continue
            break
        except ValueError:
            print("Error: Fecha inexistente o formato incorrecto (DD/MM/AAAA).")

    while True:
        try:
            h = input("Ingrese hora de envío (HH:MM): ")
            # Valida que los rangos sean de 00:00 a 23:59
            hora_valida = date.strptime(h, "%H:%M").time()
            break
        except ValueError:
            print("Error: Hora inválida o formato incorrecto (HH:MM).")
    # Separarlos 
    año = fecha_valida.year
    mes = fecha_valida.month
    dia = fecha_valida.day
    
    hora = hora_valida.hour
    minuto = hora_valida.minute
    # Instanciación, Carga y Encolado , ya paso todos los filtros con los try/excepts
    try:
        t = crearTrabajo()
        cargarTrabajo(t, jobId, nombDocu, tipo, cantPag, nivel, año, mes, dia, hora, minuto)
        encolar(cola, t)
        
        print(f"Trabajo Agregado")
        
    except Exception as e:
        # Excepcion del TAD , algun error del mismo , esta solo para evitar que re rompa todo
        print(f"Error")



def cambioDePrioridad(cola):
# Procedimiento en el cual se evalua la cola de trabajos del sistema de impresión, buscando un id en especifico para modificarle la prioridad.
    print("--- Cambio de Prioridad Individual ---")
    # Se verifica que la cola este vacía. Si lo está, muestra un mensaje y retorna al menú principal.
    if colaVacia(cola):
        print("La cola está vacía. ")
        return
    
    #Se asignan datos para recorrer la cola, y se asignan una variable para el tamaño de la cola.
    idABuscar = int(input("Ingrese el ID de Trabajo que desea modificar: "))
    idEncontrado = False
    cantElementos = tamaño(cola)

    #Mientras la cola no este vacía, se recorre la cola en base a la cantidad de elementos, buscando el ID que se desea modificar.
    for i in range (cantElementos) :
        #Se desencola cada elemento asignandolo como t (trabajo)
        t = desencolar(cola)

        #Si el ID es encontrado, se le asigna una nueva prioridad, y se modifica el trabajo.
        if verId(t) == idABuscar :
            nuevaPrioridad = input("Ingrese la nueva prioridad que desea modificar (n: Normal / e: Express / b: Baja)").lower()

            if nuevaPrioridad in ["n", "e", "b"]:
                modPrioridad(t, nuevaPrioridad)
                print("¡Cambio exitoso! La prioridad ha sido actualizada. ")
                idEncontrado = True
            else:
                print("Error: Prioridad no válida. No se realizaron cambios. ")
        
        #Se vuelve a encolar cada elemento, indistintamente de si se modifico la prioridad.
        encolar(cola, t)

    #Si el ID no es encontrado, se muestra un mensaje de error.
    if not idEncontrado:
        print(f"No se encontró ningún trabajo con el ID {idABuscar}. ")


def visualizacionCola(cola):
# Este procedimiento se encarga de visualizar todos los elementos de la cola, mostrando asi las impresiones de manera ordenada en base al id.
    print("--- Visualización de Cola ---")
    #Verifico que la cola no este vacia, si no esta vacia, continua la ejecución.
    if colaVacia(cola):
        print("No hay trabajos pendientes de impresión. ")
        return
    

    for i in range(tamaño(cola)):
    #Desencolo elemento por elemento
        t = desencolar(cola)

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
        print(f" {i+1}. -Job ID: {verId(t)}")
        print(f" - Formato: {verFormato(t)}")
        print(f" - Documento: {verNombre(t)}")
        print(f" - Cantidad de páginas: {verPaginas(t)}")
        print(f" - Prioridad: {prioridad}")
        print(f" - Fecha: {verDia(t):02d}/{verMes(t):02d}/{verAño(t):02d}")
        print(f" - Hora: {verHora(t):02d}:{verMinuto(t):02d}")
        print("---"*6)

    encolar(cola, t)


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



def genSubColaHoraria(cola):
# Dada una franja horaria, genera una Sub-Cola con solo los trabajos que deben realizarse en esa franja especifica.
    if not cola:
        print("Error: La cola esta vacia!")
        return
    
    # Creo sub-cola
    subcola = crearCola()

    # Cargo franja horaria
    while True:
        try:
            ini = datetime.strptime(input("Ingrese el inicio de la franja horaria (formato HH:MM): "), "%H:%M").time()
            fin = datetime.strptime(input("Ingrese el final de la franja horaria (formato HH:MM): "), "%H:%M").time()

            if(ini > fin): # Veo que sea una franja valida
                print("Ingresa un horario valido!")
                continue

            break
        except ValueError:
            print("Ingresá un horario valido!")

    for i in range(tamaño(cola)):
        t = desencolar(cola)
        hora = time(verHora(t), verMinuto(t))
        if (ini <= hora <= fin):
            encolar(subcola, t)
        encolar(cola, t)

    return subcola



def cancelacionPorFormato(cola):
# Cancela los trabajos con el formato dado.
    print(" CANCELACIÓN POR FORMATO ")

    if colaVacia(cola):
        print("La cola está vacía. No hay trabajos para cancelar")
        return

    # Solicitar el formato a eliminar
    formato_a_eliminar = input("Ingrese el tipo de formato a cancelar (ej: Imagen, PDF): ").strip() # Se va a usar para devolver el formato eliminado
    if not formato_a_eliminar:
        print("Error: Debe ingresar un formato válido.")
        return

    # Contador para ver cuantos trabajos elimine para informar al final
    eliminados = 0
    
    # Crear la cola auxiliar para los que no se descartan
    aux = crearCola()

    # Vaciar la cola original para filtrar
    while not colaVacia(cola):
        trabajo_actual = desencolar(cola)
        
        # Hacemos uso la función del TAD para ver el formato sin modificar la cola original
        if verFormato(trabajo_actual).lower() == formato_a_eliminar.lower():
            eliminados += 1  # si lo encontre, se descarta (no se encola en aux)
        else:
            encolar(aux, trabajo_actual) # No coincide, lo encolo

    # Volver a pasar los que no se descartaron

    copiarCola(cola, aux)

    # Informar si se pudo o no realizar la eliminacion y de haberlo hecho devolver la cantidad y el formato eliminados
    if eliminados > 0:
        print(f"Operación exitosa. Se eliminaron {eliminados} trabajos con formato '{formato_a_eliminar}'.")
    else:
        print(f" No se encontraron trabajos con el formato '{formato_a_eliminar}' en la cola.")
        



if __name__ == "__main__":
    main()
