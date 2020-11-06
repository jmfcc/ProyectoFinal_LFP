import os
from os import system
from os import path
import time

def getsource():
    ruta = path.dirname(path.abspath(__file__)) #Obtiene la ruta del script en ejecución
    #print("lo que obtengo ",ruta)
    return ruta

def mimetodo(di):
    try:
        time.sleep(2)
        system (di)
    except:
        print("Error al generar png")
    
def grafo(nodos, enlaces):
    ruta = getsource()
    nombre = ruta + "\\DiagramaBloques"
    file = open(nombre + ".dot", "w")
    file.close()
    #escrituralog("carrito.dot");
    escrituranorm("digraph d{", nombre)
    escrituranorm("\trankdir = LR", nombre)
    escrituranorm("\tgraph [dpi = 300];", nombre)
    escrituranorm("\tnode [shape = box];", nombre)
    #count1 = 1
    #CREACION DE NODOS
    log = "\tnodeStart[shape = point, label=\"\"]"
    escrituranorm(log, nombre)
    #shape=doublecircle

    for n in nodos:
        log = "\tnodeTk" + str(n[1]) + "[label=\"" + n[0] +"\"];"
        escrituranorm(log, nombre)

    log = "\tnodeStart->nodeTk1[constraint = none]"
    escrituranorm(log, nombre)

    for e in enlaces:
        enlaceRaiz = sonRaiz(nodos, e[0], e[1])
        if enlaceRaiz:
            log = "\tnodeTk" + str(e[0]) + " -> nodeTk" + str(e[1]) + "[constraint = none];"
        else:
            log = "\tnodeTk" + str(e[0]) + " -> nodeTk" + str(e[1]) + ";"
            
        escrituranorm(log, nombre)

    log = "}"
    escrituranorm(log, nombre)
    
    #generacmd("grafo.cmd")
    generagraf(nombre)
    
def generagraf(nombre):
    di = "dot -Tpng " +  nombre + ".dot -o " + nombre + "-grafo.png"
    #print(di)
    mimetodo(di)
    openGraf(nombre)

def sonRaiz(nodos, idSalida, idLlegada):
    lvlSalida = 0
    lvlLlegada = 0
    for n in nodos:
        if n[1] == idSalida:
            lvlSalida = n[2]
        if n[1] == idLlegada:
            lvlLlegada = n[2]
    if lvlSalida == lvlLlegada:
        if lvlSalida == 1:
            return True
        else:
            return False
    else:
        return False
    
def escrituranorm(log, nombre):
    file = open(nombre + ".dot", "a")
    file. write(log + os.linesep)
    file. close()

def openGraf(name):
    di = "start " + name + "-grafo.png"
    try:
        time.sleep(2)
        system (di)
    except:
        print("Error al abrir grafo")