from datetime import date, time,datatime

def crearTrabajo():
# Crea un TAD trabajo con los siguientes campos: id, nombre, formato, paginas, prioridad, fecha y hora
    return[0, "", "", 0, "", date(1, 1, 1), time(00, 00)]


def modID(trabajo, id):
# Modifica el ID 
    trabajo[0] = id


def modNombre(trabajo, nombre):
# Modifica el nombre del trabajo
    trabajo[1] = nombre


def modFormato(trabajo, formato):
# Modifica el formato del trabajo
    trabajo[2] = formato


def modPaginas(trabajo, paginas):
# Modifica el numero de paginas
    trabajo[3] = paginas


def modPrioridad(trabajo, prioridad):
# Modifica la prioridad; tipos de prioridad:
# - b: Basica
# - n: Normal
# - e: Express
    if prioridad not in ["b", "n", "e"]:
        raise Exception("Error: No se dio un tipo de prioridad valido")
    trabajo[4] = prioridad.lower()


def modFecha(trabajo, año, mes, dia):
# Modifica la fecha
    trabajo[5] = date(año, mes, dia)


def modAño(trabajo, año):
# Modifica solo el año
    trabajo[5] = trabajo[5].replace(year=año)


def modMes(trabajo, mes):
# Modifica solo el mes
    trabajo[5] = trabajo[5].replace(month=mes)


def modDia(trabajo, dia):
# Modifica solo el dia
    trabajo[5] = trabajo[5].replace(day=dia)


def modHorario(trabajo, hora, minuto):
# Modifica el horario
    trabajo[6] = time(hora, minuto)


def modHora(trabajo, hora):
# Modifica solo la hora
    trabajo[6] = trabajo[6].replace(hour=hora)


def modMinuto(trabajo, minuto):
# Modifica solo el minuto
    trabajo[6] = trabajo[6].replace(minute=minuto)


def cargarTrabajo(trabajo, id, nombre, formato, paginas, prioridad, año, mes, dia, hora, minuto):
# Carga todos los campos de un TAD trabajo.
    modID(trabajo, id)
    modNombre(trabajo, nombre)
    modFormato(trabajo, formato)
    modPaginas(trabajo, paginas)
    modPrioridad(trabajo, prioridad)
    modFecha(trabajo, año, mes, dia)
    modHorario(trabajo, hora, minuto)


def verId(trabajo):
# Retorna el ID del Trabajo
    return trabajo[0]


def verNombre(trabajo):
# Retorna el nombre
    return trabajo[1]


def verFormato(trabajo):
# Retorna el tipo de formato de impresion
    return trabajo[2]


def verPaginas(trabajo):
# Retorna la cantidad de paginas
    return trabajo[3]


def verPrioridad(trabajo):
# Retorna la prioridad del trabajo; tipos de prioridad
# - b: Baja
# - n: Normal
# - e: Express
    return trabajo[4]


def verAño(trabajo):
# Retorna el año del trabajo como entero
    return trabajo[5].year


def verMes(trabajo):
# Retorna el mes del trabajo como entero
    return trabajo[5].month


def verDia(trabajo):
# Retorna el dia del trabajo como entero
    return trabajo[5].day


def verHora(trabajo):
# Retorna la hora del trabajo como entero
    return trabajo[6].hour


def verMinuto(trabajo):
# Retorna el minuto del trabajo como entero
    return trabajo[6].minute


def asignarTrabajo(t1,t2):
# Asigna los datos de trabajo1 al trabajo2
    modID(t2,verId(t1))
    modNombre(t2,verNombre(t1))
    modFormato(t2,verFormato(t1))
    modPaginas(t2,verPaginas(t1))
    modPrioridad(t2,verPrioridad(t1))
    modAño(t2, verAño(t1))
    modMes(t2, verMes(t1))
    modDia(t2, verDia(t1))
    modHora(t2, verHora(t1))
    modMinuto(t2, verMinuto(t1))
