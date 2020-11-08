import basiliskAnalyz
import os

def head():
    print("::::::::::::::::::::::::::::::::::::: BASILISK :::::::::::::::::::::::::::::::::::::"
    + "  \n:::::::::::::::::::::::::::::::::::::: SYSTEM ::::::::::::::::::::::::::::::::::::::")

scriptJs = ""
def menu():
    head()
    print()
    while True:
        print("--------------------------------------  MENU  --------------------------------------")
        print("1- Cargar Script")
        print("2- Manejo AFD")
        print("3- Pila Interactiva")
        print("4- Diagrama de Bloques")
        print("5- Salir")
        print()
        global scriptJs
        try:
            opcion = int(input("Seleccione una opción: >> "))
            if opcion:
                if opcion >= 1 and opcion <= 5:
                    if opcion == 1:
                        cargar()
                    if opcion == 2:
                        if scriptJs:
                            basiliskAnalyz.analizacadenaAFD(scriptJs)
                        else:
                            print(">>> Error: No hay ningun archivo en memoria..")
                    if opcion == 3:
                        if scriptJs:
                            basiliskAnalyz.analizacadenaAFD_AP(scriptJs)
                            #basiliskAnalyz.analizacadenaAP(scriptJs)
                            # print(" >>> [1] AFD y AP")
                            # print(" >>> [2] AP")
                            # mode = input(" >>>  Selecciona un modo: ")
                            # if mode:
                            #     if mode == "1":
                            #     elif mode == "2":
                            #     else:
                            #         print(" >>>  Debe seleccionar 1 o 2.")
                            # else:
                            #     print(" >>> Debe seleccionar un modo.")
                        else:
                            print(">>> Error: No hay ningun archivo en memoria..")
                    if opcion == 4:
                        #print("Opción no disponible en la versión beta")
                        if scriptJs:
                            basiliskAnalyz.afdDiag(scriptJs)
                        else:
                            print(">>> Error: No hay ningun archivo en memoria..")
                    if opcion == 5:
                        print("Saliendo del sistema...")
                        #mostrar()
                        return
                else:
                    print("Opción no disponible")
            else:
                print("Debe ingresar una opción")
        except:
            print("<< La opcion solicitada no esta disponible >>")
        stp = input(" >>> Persione enter para continuar... ")
        print()
        print()



def cargar():
    ruta = input(" >>> Ingrese la ruta del archivo: ")
    print()
    if ruta:
        if os.path.isfile(ruta):
            ph, fh = os.path.split(ruta)
            nombre, extension = os.path.splitext(fh)
            if extension == ".js":
                global scriptJs
                scriptJs = ruta
                print(" >>> Archivo Cargado -- ", nombre + extension,"\n")
            else:
                print(" >>> El archivo no es de extensión .js")
        else:
            print(" >>> Fichero no encontrado")
    else:
        print(" >>> Debe ingresar una ruta para usar el archivo deseado")


def mostrar():
    global scriptJs
    for line in scriptJs:
        print(line.rstrip(), "----------")

menu()