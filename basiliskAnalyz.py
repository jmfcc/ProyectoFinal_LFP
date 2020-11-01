import basiliskAFD
import basiliskAP
import reporte

#-------------------------------------------- AFD ------------------------------------------------------------------

#-------------------------------------------- AP ------------------------------------------------------------------
HistAP = []
tksimp = ["(",")","{","}",",",":",";", "=", ">"]
tkcomp = ["let","var","const","if","while","switch","foreach","in","case","default","break"]
tknoreserv = ["numero","booleano","idvar"]

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
    else:
        return False
def getTypeNonReserv(tk):
    try:
        valor = float(tk)
        return "numero"
    except:
        if (tk == "true") or (tk == "false"):
            return "booleano"
        else:
            init = True
            for c in tk:
                if init:
                    if not(c == "_") and not(c.isalpha()):
                        return "None"
                    init = False
                else:
                    if not(c == "_") and not(c.isalpha()) and not(c.isdigit()):
                        return "None"
            return "idvar"

def analizacadenaAP(ruta):
    #print("Entra al metodo de analisis")
    archivo = open(ruta, "r")
    HistAP.clear()
    basiliskAP.limpiaPila()
    estadoActual = "i"
    esValida = False
    esCadena = False  #cadena
    esComentario = False #comment
    needNext = False  #comment
    countRow = 0
    indxItkn = 0
    for lines in archivo:
        token = ""
        countRow += 1
        countCol = 0
        line = lines.rstrip()
        #if line:
            #print(line)
        for character in line:
            countCol += 1
            if (character == "/" or character == "*") and not esCadena:
                if token:
                    if isTypeComp(token):
                        esValida, estadoSiguiente, pilaHist, trnHist = validaToken(estadoActual, token, False, sepCadena(indxItkn,line))#validar si es valida jaja :v
                    elif isTypeNonReserv(token):
                        esValida, estadoSiguiente, pilaHist, trnHist = validaToken(estadoActual, getTypeNonReserv(token), False, sepCadena(indxItkn,line))
                    else:
                        print(" >>> Error")
                        return
                    if esValida:
                        estadoActual = estadoSiguiente
                        #Enviar a mostrar los datos con print      #obtener la cadena en lectura
                        muestraProcesoPila(pilaHist, sepCadena(indxItkn,line), trnHist)
                        esValida = False
                        token = ""
                    else:
                        print(" >>> Error")
                        return
                if esComentario:
                    if character == "*":
                        needNext = True
                    elif character == "/" and needNext:
                        needNext = False
                        esComentario = False
                    else:
                        needNext = False
                else:
                    if character == "/":
                        needNext = True
                    elif character == "*" and needNext:
                        needNext = False
                        esComentario = True
                    else:
                        print(" >>> Error en comentario apr")
                        return
            elif needNext and not esCadena:
                if esComentario:
                    needNext = False
                else:
                    print(" >>> Error ")
                    return
            elif esComentario:
                pass
            else:
                if character == "\"":
                    if esCadena:
                        token += character
                        esValida, estadoSiguiente, pilaHist, trnHist = validaToken(estadoActual, "cadena", False, sepCadena(indxItkn,line))
                        if esValida:
                            estadoActual = estadoSiguiente
                            #Enviar a mostrar los datos con print      #obtener la cadena en lectura
                            muestraProcesoPila(pilaHist, sepCadena(indxItkn,line), trnHist)
                            esValida = False
                            token = ""
                        else:
                            print(" >>> Error")
                            return
                        esCadena = False #enviar token leido
                    else:
                        esCadena = True
                        if token:
                            if isTypeComp(token):
                                esValida, estadoSiguiente, pilaHist, trnHist = validaToken(estadoActual, token, False, sepCadena(indxItkn,line))#validar si es valida jaja :v
                            elif isTypeNonReserv(token):
                                esValida, estadoSiguiente, pilaHist, trnHist = validaToken(estadoActual, getTypeNonReserv(token), False, sepCadena(indxItkn,line))
                            else:
                                print(" >>> Error")
                                return
                            if esValida:
                                estadoActual = estadoSiguiente
                                #Enviar a mostrar los datos con print      #obtener la cadena en lectura
                                muestraProcesoPila(pilaHist, sepCadena(indxItkn,line), trnHist)
                                esValida = False
                                token = ""
                            else:
                                print(" >>> Error")
                                return
                        token += character
                        if len(token) == 1:
                            indxItkn = countCol
                elif esCadena:
                    token += character
                    if countCol == len(line): #a
                        print(" >>> Error")
                        return
                elif not character.isspace():
                    if isTypeSimp(character):
                        if token:
                            if isTypeComp(token):
                                esValida, estadoSiguiente, pilaHist, trnHist = validaToken(estadoActual, token, False, sepCadena(indxItkn,line))#validar si es valida jaja :v
                            elif isTypeNonReserv(token):
                                esValida, estadoSiguiente, pilaHist, trnHist = validaToken(estadoActual, getTypeNonReserv(token), False, sepCadena(indxItkn,line))
                            else:
                                print(" >>> Error")
                                return
                            if esValida:
                                estadoActual = estadoSiguiente
                                #Enviar a mostrar los datos con print      #obtener la cadena en lectura
                                muestraProcesoPila(pilaHist, sepCadena(indxItkn,line), trnHist)
                                esValida = False
                                token = ""
                            else:
                                print(" >>> Error")
                                return
                        #Mando a analizar el caracter directamente
                        esValida, estadoSiguiente, pilaHist, trnHist = validaToken(estadoActual, character, False, sepCadena(countCol,line))
                        if esValida:
                            estadoActual = estadoSiguiente
                            #Enviar a mostrar los datos con print      #obtener la cadena en lectura
                            muestraProcesoPila(pilaHist, sepCadena(countCol,line), trnHist)
                            esValida = False
                            token = ""
                        else:
                            print(" >>> Error")
                            return
                    else:
                        #print("Guardando el Tok: ", character, " en: ", countCol, " y el token es: ", token)
                        token += character
                        if len(token) == 1:
                            #print("Guardando el indxTok: ", countCol)
                            indxItkn = countCol                            
                        elif countCol == len(line): #Si llega al final de la linea verificará si hay un token almacenado y lo evaluará
                            if token:
                                if isTypeComp(token):
                                    esValida, estadoSiguiente, pilaHist, trnHist = validaToken(estadoActual, token, False, sepCadena(indxItkn,line))#validar si es valida jaja :v
                                elif isTypeNonReserv(token):
                                    esValida, estadoSiguiente, pilaHist, trnHist = validaToken(estadoActual, getTypeNonReserv(token), False, sepCadena(indxItkn,line))
                                else:
                                    print(" >>> Error")
                                    return
                                if esValida:
                                    estadoActual = estadoSiguiente
                                    #Enviar a mostrar los datos con print      #obtener la cadena en lectura
                                    muestraProcesoPila(pilaHist, sepCadena(indxItkn,line), trnHist)
                                    esValida = False
                                    token = ""
                                else:
                                    print(" >>> Error")
                                    return 
                else:
                    if token: #El espacio me servirá como delimitador es decir que letvar será tomado como identificador
                        if isTypeComp(token):
                            esValida, estadoSiguiente, pilaHist, trnHist = validaToken(estadoActual, token, False, sepCadena(indxItkn,line))#validar si es valida jaja :v
                        elif isTypeNonReserv(token):
                            esValida, estadoSiguiente, pilaHist, trnHist = validaToken(estadoActual, getTypeNonReserv(token), False, sepCadena(indxItkn,line))
                        else:
                            print(" >>> Error")
                            return
                        if esValida:
                            estadoActual = estadoSiguiente
                            #Enviar a mostrar los datos con print      #obtener la cadena en lectura
                            muestraProcesoPila(pilaHist, sepCadena(indxItkn,line), trnHist)
                            esValida = False
                            token = ""
                        else:
                            print(" >>> Error")
                            return  
    #Validar si la pila es ["#", "S0"]
    esValida, estadoSiguiente, pilaHist, trnHist = validaToken(estadoActual, "#", False, "  #  ")
    if esValida:
        estadoActual = estadoSiguiente
        #Enviar a mostrar los datos con print      #obtener la cadena en lectura
        muestraProcesoPila(pilaHist, "  #  ", trnHist)
        encabezado = ["PILA","ENTRADA","TRANSICION"]
        reporte.generaHtml("Analisis Por Automata de Pila", encabezado, HistAP)
    else:
        print(" >>> Error, la pila no esta vacía")
        return  
    archivo.close()

def muestraProcesoPila(pilaHist, cadena, trnHist):
    encabezado = ["PILA","ENTRADA","TRANSICION"]
    tmpila = max([4, len(pilaHist)])
    tmentrada = max([7, len(cadena)])
    tmtransi = max([10, len(trnHist)])
    sep = separadorvertical(tmpila, tmentrada, tmtransi)
    enc = aniadeespacio(encabezado, tmpila, tmentrada, tmtransi)
    cuerpo = [pilaHist, cadena, trnHist]
    crp = aniadeespacio(cuerpo, tmpila, tmentrada, tmtransi)
    histTempo = [pilaHist, cadena, trnHist]
    HistAP.append(histTempo.copy())
    print(sep)
    print(enc)
    print(sep)
    print(crp)
    print(sep)
    stp = input(" >>> Presione enter para continuar...")
    print()
    print()
    
def separadorvertical(n1,n2,n3):
    sep = ""
    for i in range(0, n1+2):
        sep += "-"
    sep += "||"
    for i in range(0, n2+2):
        sep += "-"
    sep += "||"
    for i in range(0, n3+2):
        sep += "-"
    sep += "||"
    return sep

def aniadeespacio(elem, n1,n2,n3):
    p = n1 - len(elem[0])   #10 - 10 = 0 
    en = n2 - len(elem[1])
    trn = n3 - len(elem[2])
    spaces = ""
    txt = ""
    for i in range(0, p+1):
        spaces = spaces + " "
    txt = " " + elem[0] + spaces + "||"
    spaces = ""
    for i in range(0, en+1):
        spaces = spaces + " "
    txt = txt + " " + elem[1] + spaces + "||"
    spaces = ""
    for i in range(0, trn+1):
        spaces = spaces + " "
    txt = txt + " " + elem[2] + spaces + "||"
    return txt

def sepCadena(indxI, cadena):
    extract = ""
    for i in range(indxI-1, len(cadena)):
        extract += cadena[i]
    #print("el texto extraido es: ", extract, " con los indices: ", indxI, " de la cadena", cadena)
    return extract

def validaToken(estadoAct, token, consumeToken, cadena):
    estadoActual = estadoAct
    while consumeToken == False:
        consumeTkn, popP, pushP, pushList, estadoSiguiente, trnHist = buscaestadoSiguiente(estadoActual, token, basiliskAP.peekPila())
        if estadoSiguiente == "Ninguno":
            return False, estadoSiguiente, "None", "None" #Retornar que el token no coincide con ninguna transicion
        pilaHist = basiliskAP.getStatusPila()
        if pilaHist == None:
            pilaHist = "-      -"
        if popP:
            basiliskAP.popPila()
        if pushP:
            for pL in list(reversed(pushList)):
                basiliskAP.pushPila(pL)
        if consumeTkn:
            return True, estadoSiguiente, pilaHist, trnHist #hacer el return al consumir el token
        else:
            #mandar a mostrar la transicion
            estadoActual = estadoSiguiente
            muestraProcesoPila(pilaHist, cadena, trnHist)

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

def dameFormato(tr):
    simb = "(" + tr[0][0] + ", " +tr[0][1] + ", " + tr[0][2] + "; " + tr[1][0] + ", "
    init = True
    for comp in tr[1][1]:
        if init:
            simb = simb + comp
            init = False
        else:
            simb = simb + " " + comp
    return simb + ")"