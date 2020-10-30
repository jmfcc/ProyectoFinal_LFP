import basiliskAFD
import basiliskAP

#-------------------------------------------- AFD ------------------------------------------------------------------

#-------------------------------------------- AP ------------------------------------------------------------------
HistAP = []
tksimp = ["(",")","{","}",",",":",";","=",">"]
tkcomp = ["let","var","const","if","while","switch","foreach","idvar","in","case","default","break"]
tknoreserv = ["cadena","numero","booleano"]

def isTypeSimp(tk):
    if tk in tksimp:
        return True
    else:
        return False
def isTypeComp(tk):
    if tk in tkcomp:
        return True
    else:
        return False
def isTypeNonReserv(tk):
    tipo = getTypeNonReserv(tk)
    if tipo in tknoreserv:
        return True
    elif tipo == "idvar": ###---------------------------------
        return True
    else:
        return False
def getTypeNonReserv(tk):
    try:
        valor = float(tk)
        return "numero"
    except:
        if tk == "true":
            return "booleano"
        elif tk == "false":
            return "booleano"
        else:
            init = True
            for c in tk:
                if init:
                    if not(c == "_") or not(c.isalpha()):
                        return "None"
                    init == False
                else:
                    if not(c == "_") or not(c.isalpha()) or not(c.isdigit()):
                        return "None"
            return "idvar"



def analizacadenaAP(archivo):
    HistAP.clear()
    basiliskAP.limpiaPila()
    estadoActual = "i"
    encabezado = ["PILA","ENTRADA","TRANSICION"]
    esValida = False
    consumeToken = False
    esCadena = False  #cadena
    esComentario = False #comment
    needNext = False  #comment
    #needClose = False  #
    #ignoreSpaces = True
    countRow = 0
    for lines in archivo:
        token = ""
        countRow += 1
        countCol = 0
        line = lines.rstrip()
        if line:
            pass
        for character in line:
            countCol += 1
            if (character == "/" or character == "*") and not esCadena:
                #VALIDAR SI HAY UN TOKEN EN PLENA LECUTRA
                if esComentario:
                    if character == "*":
                        needNext = True
                    elif character == "/" and needNext:
                        needNext = False
                        esComentario = False
                    else:
                        print(" >>> Error en linea ", countRow, "  columna ", countCol)
                        return
                else:
                    if character == "/":
                        needNext = True
                    elif character == "*" and needNext:
                        needNext = False
                        esComentario = True
                    else:
                        print(" >>> Error en linea ", countRow, "  columna ", countCol)
                        return
            elif needNext and not esCadena:
                print(" >>> Error en linea ", countRow, "  columna ", countCol)
                return
            elif esComentario:
                pass
            else:
                if character == "\"":
                    if esCadena:
                        esCadena = False #enviar token leido
                    else:
                        esCadena = True
                        token += character
                elif esCadena:
                    token += character
                elif not character.isspace(): #palabras reservadas, signos reserv e idvars
                    #Analizar antes de istype para leer un comentario
                    if isTypeSimp(character):
                        if token:
                            #Activo un booleano para indicar que el token si debe ser analizado
                            pass
                        #Mando a analizar el caracter directamente
                    else:
                        token += character
                else:
                    if token:
                        consumeToken = True
                        
                if countCol == len(line): #añadir booleano consumeToken u otro flag
                    if token:
                        #Activar booleano
                        pass
                
                if not esValida:
                    break
    if basiliskAP.peekPila() == "#":
        log = ["#", "-", "(q, $, #; f, $)"]
        
    else:
        print("Cadena Inválida")
    stp = input("Presione enter para continuar...")

def validaToken(estadoActual, token, consumeToken):
    while consumeToken == False:
        consumeTkn, popP, pushP, pushList, estadoSiguiente, trnHist = buscaestadoSiguiente(estadoActual, token, basiliskAP.peekPila())
        if estadoSiguiente == "Ninguno":
            return False, estadoSiguiente, "None", "None" #Retornar que el token no coincide con ninguna transicion
        if popP:
            basiliskAP.popPila()
        if pushP:
            for pL in list(reversed(pushList)):
                basiliskAP.pushPila(pL)
        if consumeTkn:
            pilaHist = basiliskAP.getStatusPila()
            if pilaHist == None:
                pilaHist = "-      -"
            return True, estadoSiguiente, pilaHist, trnHist #hacer el return al consumir el token


def buscaestadoSiguiente(estadoAct, Token, cima):
    catchTrans = "None"
    for t in basiliskAP.getTran():
        if t[0][0] == estadoAct and t[0][1] == "$" and t[0][2] == "$":
            return False, False, True, t[1][1].copy(), t[1][0], dameFormato(t)
        elif t[0][0] == estadoAct and t[0][1] == "$" and t[0][2] == cima:
            if t[1][1][0] == Token:
                return False, True, True, t[1][1].copy(), t[1][0], dameFormato(t)
            elif t[1][1][0] == "epsilon":
                catchTrans = t
        elif t[0][0] == estadoAct and t[0][1] == Token and t[0][2] == cima:
            return True, True, False, t[1][1].copy(), t[1][0], dameFormato(t)
    if catchTrans != "None":
        return False, True, False, catchTrans[1][1].copy(), catchTrans[1][0], dameFormato(catchTrans)
    else:
        return False, False, False, ["Ninguno"], "Ninguno", "Ninguno"
#Retorno  ---------- consumeCaracter[T/F], popPila[T/F], pushPila[T/F], pushPila[list], estSiguiente, tranHistorial

def dameFormato(tr):
    simb = "(" + tr[0][0] + ", " +tr[0][1] + ", " + tr[0][2] + "; " + tr[1][0] + ", "
    for comp in tr[1][1]:
        simb = simb + comp
    return simb + ")"