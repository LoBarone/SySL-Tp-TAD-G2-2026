from tad_cola import *
from tad_trabajo import *


def main():
    while True:
        print("--------"*6 + "\nPrograma gestion de impresiones:\n" + "--------"*6)
        print("\n [ 1 ] - Opcion 1\n [ 2 ] - Opcion 2\n [ 3 ] - Opcion 3\n [ 4 ] - Opcion 4\n [ 5 ] - Opcion 5\n [ 6 ] - Opcion 6\n [ 7 ] - Salir")
        # Cambiar nombre opcion por el nombre correcto (me dio paja xd) -lolo
        
        opcion = int(input("Seleccione la opción que desea utilizar:"))

        match opcion:
            case 1:
                #procedimiento o codigo directamente
                pass
            case 2:
                #procedimiento o codigo directamente
                pass
            case 3:
                #procedimiento o codigo directamente
                pass
            case 4:
                #procedimiento o codigo directamente
                pass
            case 5:
                #procedimiento o codigo directamente
                pass
            case 6:
                #procedimiento o codigo directamente
                pass
            case 7:
                print("Fin del programa!")
                break
            case _:
                print("Error: La opción que usted seleccionó es invalida. ")

def ejemplo(): # para cada solucion definamos una funcion que despues vamos a llamar dentro del main.
    pass # el pass es solo para que no marque error, cuando escriban codigo saquenlo.


if __name__ == "__main__":
    main()
