from datetime import date, time

def crearTrabajo():
# Crea un TAD trabajo con los siguientes campos: id, nombre, formato, paginas, prioridad, fecha y hora
    return[0, "", "", 0, "", date(0001, 00, 00),time(00, 00)]

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
# Modifica la prioridad
    trabajo[4] = prioridad

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

def modMinute(trabajo, minuto):
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
#Retorna el ID del Trabajo
    return trabajo[0]

def verNombre(trabajo):
#Retorna el nombre
    return trabajo[1]

def verFormato(trabajo):
#Retorna el tipo de formato de impresion
    return trabajo[2]

def verPaginas(trabajo):
#Retorna la cantidad de paginas
    return trabajo[3]

def verPrioridad(trabajo):
#Retorna la prioridad del trabajo
    return trabajo[4]

def verFecha(trabajo):
#Retorna la fecha del trabajo
    return trabajo[5]

def verHora(trabajo):
#Retorna la hora del trabajo
    return trabajo[6]

def asignarTrabajo(t1,t2):
<<<<<<< HEAD
#Asigna los datos de trabajo1 al trabajo2
    modID(t2,verId(t1))
    modNombre(t2,verNombre(t1))
    modFormato(t2,verFormato(t1))
    modPaginas(t2,verPaginas(t1))
    modPrioridad(t2,verPrioridad(t1))
    modFecha(t2,verFecha(t1))
    modHora(t2,verHora(t1))
