
estados = ["i","p","q","f"]

transicion = [
    [["i","$","$"],["p",["#"]]],
    [["p","$","$"],["q",["S0"]]],

    [["q","$","S0"],["q",["let","S1"]]],
    [["q","$","S0"],["q",["var","S1"]]],
    [["q","$","S0"],["q",["const","S1"]]],
    [["q","$","S0"],["q",["if","S5"]]],
    [["q","$","S0"],["q",["while","S5"]]],
    [["q","$","S0"],["q",["switch","S7"]]],
    [["q","$","S0"],["q",["foreach","(","idvar","in","idvar",")","{","S0","}","S0"]]],
    [["q","$","S0"],["q",["idvar","(","S10",")",";","S0"]]],
    [["q","$","S0"],["q",["epsilon"]]],

    [["q","$","S1"],["q",["idvar","=","S2"]]],

    [["q","$","S2"],["q",["cadena",";","S0"]]],
    [["q","$","S2"],["q",["numero",";","S0"]]],
    [["q","$","S2"],["q",["booleano",";","S0"]]],
    [["q","$","S2"],["q",["(","S3",")","=",">","{","S0","}","S0"]]],

    [["q","$","S3"],["q",["idvar","S4"]]],
    [["q","$","S3"],["q",["epsilon"]]],

    [["q","$","S4"],["q",[",","idvar","S4"]]],
    [["q","$","S4"],["q",["epsilon"]]],
    
    [["q","$","S5"],["q",["(","S6",")","{","S0","}","S0"]]],

    [["q","$","S6"],["q",["idvar"]]],
    [["q","$","S6"],["q",["booleano"]]],

    [["q","$","S7"],["q",["(","idvar",")","{","S8","}","S0"]]],

    [["q","$","S8"],["q",["case","S13",":","S0","S9","S8"]]],
    [["q","$","S8"],["q",["default",":","S0","S9","S8"]]],
    [["q","$","S8"],["q",["epsilon"]]],

    #[["q","$","S9"],["q",["case","S13",":","S0","S9"]]],
    [["q","$","S9"],["q",["break",";"]]],
    [["q","$","S9"],["q",["epsilon"]]],

    [["q","$","S10"],["q",["cadena","S11"]]],
    [["q","$","S10"],["q",["numero","S11"]]],
    [["q","$","S10"],["q",["booleano","S11"]]],
    [["q","$","S10"],["q",["idvar","S11"]]],
    [["q","$","S10"],["q",["epsilon"]]],

    [["q","$","S11"],["q",[",","S12"]]],
    [["q","$","S11"],["q",["epsilon"]]],

    [["q","$","S12"],["q",["cadena","S11"]]],
    [["q","$","S12"],["q",["numero","S11"]]],
    [["q","$","S12"],["q",["booleano","S11"]]],
    [["q","$","S12"],["q",["idvar","S11"]]],

    [["q","$","S13"],["q",["cadena"]]],
    [["q","$","S13"],["q",["numero"]]],
    [["q","$","S13"],["q",["booleano"]]],

    [["q","let","let"],["q",["epsilon"]]],
    [["q","var","var"],["q",["epsilon"]]],
    [["q","const","const"],["q",["epsilon"]]],
    [["q","if","if"],["q",["epsilon"]]],
    [["q","while","while"],["q",["epsilon"]]],
    [["q","switch","switch"],["q",["epsilon"]]],
    [["q","foreach","foreach"],["q",["epsilon"]]],
    [["q","idvar","idvar"],["q",["epsilon"]]],
    [["q","(","("],["q",["epsilon"]]],
    [["q","in","in"],["q",["epsilon"]]],
    [["q",")",")"],["q",["epsilon"]]],
    [["q","{","{"],["q",["epsilon"]]],
    [["q","}","}"],["q",["epsilon"]]],
    [["q",";",";"],["q",["epsilon"]]],
    [["q",",",","],["q",["epsilon"]]],
    [["q","case","case"],["q",["epsilon"]]],
    [["q","default","default"],["q",["epsilon"]]],
    [["q","break","break"],["q",["epsilon"]]],
    [["q","cadena","cadena"],["q",["epsilon"]]],
    [["q","numero","numero"],["q",["epsilon"]]],
    [["q","booleano","booleano"],["q",["epsilon"]]],
    [["q",":",":"],["q",["epsilon"]]],
    [["q","=","="],["q",["epsilon"]]],
    [["q",">",">"],["q",["epsilon"]]],
    [["q","#","#"],["f",["epsilon"]]],
]

pila = []

# [        --------------- 0 -----------------             -------------------- 1 --------------------
#         ["estadoAct","caracter","quitaPila"],          ["estadoSig",     ["Push", "Pila"] ]
#           ----0----  ----1----   -----2-----             -----0-----      --------------1------------
#                                                                           ------n-----  -----n1------ 
# ]
    
#METODOS DE RETORNO
def getEstados():
    return estados
def getTran():
    return transicion
#PILA
def pushPila(elemento):
    pila.append(elemento)
def popPila():
    pila.pop()
def peekPila():
    elem = "Vacío"
    for elem in pila:
        pass
    return elem
def pilaVacia():
    if len(pila) == 0:
        return True
    else:
        return False
def getStatusPila():
    ep = ""
    if pilaVacia():
        ep = "Vacío"
    for p in list(reversed(pila)):
        ep = ep + " " + p
    return ep
def printPila():
    print(pila)
def limpiaPila():
    pila.clear()