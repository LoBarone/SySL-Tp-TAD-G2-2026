#Implementacion de la cola
def crearcola(): #crea y retorna cola vacia
    return []

def colavacia(cola):
    return len(cola)==0

def encolar(cola,elemento):
    cola.append(elemento)

def desencolar(cola):
    if colavacia(cola):
       raise Exception("Error, la cola esta vacía") #función que para la ejecución del programa (a diferencia del print errorxddd)
    return cola.pop(0)

def copiarCola(cola1,cola2): #cola 1 es donde se va a copiar, cola 2 es la cola original
    aux=crearcola() 
    while not colavacia(cola2):
        elemento=desencolar(cola2)
        encolar(aux,elemento)
    while not colavacia(aux):
        elemento=desencolar(aux)
        encolar(cola1, elemento)#cola 1 copiada con los elementos de la cola2
        encolar(cola2, elemento)#reconstruye la cola original

def tamaño(cola):
    return len(cola)

