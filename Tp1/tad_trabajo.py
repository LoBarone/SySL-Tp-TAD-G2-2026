from datetime import time, timedelta

def crearTrabajo():
# id, nombre, formato, paginas, prioridad, fecha y hora
    return[0, "", "", 0, "", "", ""] 

def modID(trabajo,id):
    trabajo[0]=id

def modNombre(trabajo,nombre):
    trabajo[1] = nombre

def modFormato(trabajo,formato):
    trabajo[2] = formato

def modPaginas(trabajo,paginas):
    trabajo[3] = paginas

def modPrioridad(trabajo,prioridad):
    trabajo[4] = prioridad

def modFecha(trabajo,fecha):
    trabajo[5] = fecha

def modHora(trabajo,hora):
    trabajo[6] = hora


def cargarTrabajo(trabajo,id,nombre,formato,paginas,prioridad,fecha,hora):
    modID(trabajo,id)
    modNombre(trabajo,nombre)
    modFormato(trabajo,formato)
    modPaginas(trabajo,paginas)
    modPrioridad(trabajo,prioridad)
    modFecha(trabajo,fecha)
    modHora(trabajo,hora)


def verId(trabajo):
    return trabajo[0]

def verNombre(trabajo):
    return trabajo[1]

def verFormato(trabajo):
    return trabajo[2]

def verPaginas(trabajo):
    return trabajo[3]

def verPrioridad(trabajo):
    return trabajo[4]

def verFecha(trabajo):
    return trabajo[5]

def verHora(trabajo):
    return trabajo[6]
    
def asignarTrabajo(t1, t2):
    t2[0] = t1[0]
    t2[1] = t1[1]
    t2[2] = t1[2]
    t2[3] = t1[3]
    t2[4] = t1[4]
    t2[5] = t1[5]
    t2[6] = t1[6]
