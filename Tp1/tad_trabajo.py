def crearTrabajo():
    return[0,"","",0,"","",""]#id,nombre,formato,paginas,prioridad, fecha y hs

def modID(trabajo,id):
    trabajo[0]=id
def modNombre(trabajo,nombre):
    trabajo[1]=nombre
def modFormato(trabajo,formato):
    trabajo[2]=formato
def modPaginas(trabajo,paginas):
    trabajo[3]=paginas
def modPrioridad(trabajo,prioridad):
    trabajo[4]=prioridad
def modFecha(trabajo,fecha):
    trabajo[5]=fecha
def modHora(trabajo,hora):
    trabajo[6]=hora

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

def asignarTrabajo(t1,t2):
    modID(t2,verId(t1))
    modNombre(t2,verNombre(t1))
    modFormato(t2,verFormato(t1))
    modPaginas(t2,verPaginas(t1))
    modPrioridad(t2,verPrioridad(t1))
    modFecha(t2,verFecha(t1))
    modHora(t2,verHora(t1))
