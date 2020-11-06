import basiliskAnalyz

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
                        #print("si entra a la opcion 3")
                        if scriptJs:
                            #print("si entra a al if")
                            basiliskAnalyz.analizacadenaAP(scriptJs)
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
        print()
        print()



def cargar():
    ruta = input(" >>> Ingrese la ruta del archivo: ")
    if ruta:
        global scriptJs
        scriptJs = ruta
        #scriptJs = open (ruta)
        print(" >>> Archivo Cargado")

def mostrar():
    global scriptJs
    for line in scriptJs:
        print(line.rstrip(), "----------")

menu()