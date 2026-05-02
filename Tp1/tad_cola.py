#Implementacion de la cola
def crearCola(): 
# Crea y retorna una cola vacia
    return []

def colaVacia(cola):
# Retorna True si la cola esta vacia
    return len(cola) == 0

def encolar(cola,elemento):
# Agrega un elemento a la cola
    cola.append(elemento)

def desencolar(cola):
# Elimina y retorna el primer elemento de la cola
    if colaVacia(cola):
       raise Exception("Error: la cola esta vacía") # función que para la ejecución del programa (a diferencia del print errorxddd)
    return cola.pop(0)

def copiarCola(cola1, cola2): 
# Cola 1 es donde se va a copiar, cola 2 es la cola original
    aux=crearCola() 
    while not colaVacia(cola2):
        elemento = desencolar(cola2)
        encolar(aux,elemento)
    while not colaVacia(aux):
        elemento = desencolar(aux)
        encolar(cola1, elemento)#cola 1 copiada con los elementos de la cola2
        encolar(cola2, elemento)#reconstruye la cola original

def tamaño(cola):
# Retorna el tamaño de la cola
    return len(cola)

