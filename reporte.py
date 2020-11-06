from os import linesep, path, system
import json
import webbrowser
from time import sleep

def getsource():
    ruta = path.dirname(path.abspath(__file__)) #Obtiene la ruta del script en ejecución
    #archivo = open(ruta + "/archivo.csv")
    return ruta

def openhtml(archivo):
    try:
        webbrowser.open(archivo)
    except:
        print("Error")


def generaHtml(name, head, reg):
    rutahtml = getsource() + "/"+ str(name).lower() +".html"
    filehtml = open(rutahtml, "w", 5, "utf-8") #open("Reporte.html", "w")
    filehtml.write("<!DOCTYPE html>\n" 
        + "<Html>\n"
        + "\n"
        + "<Head>\n"
        + "    <meta charset=\"UTF-8\">\n"
        + "    <title>REPORTE "+ str(name).upper() + "</title>\n"
        + "    <link rel=\"stylesheet\" href=\"stylerep.css\">\n"
        + "</Head>\n"
        + "<body>\n"
        + "    <h1>"+ str(name).upper()+"</h1>\n"
        + "    <table>\n"
        + "        <tbody>\n" + linesep)
    filehtml.write("            <tr>\n" + linesep)
        
    filehtml.write("                <th> - No. -</th>\n" + linesep)
    for elem in head:
        filehtml.write("                <th>"+ str(elem).upper() + "</th>\n" + linesep)
    filehtml.write("            </tr>" + linesep)
    countR = 0
    for rows in reg:
        countR += 1
        filehtml.write("            <tr>\n" + linesep)
        filehtml.write("                <td>" + str(countR) + "</td>\n" + linesep)
        for cols in rows:
            filehtml.write("                <td>" + str(cols) + "</td>\n" + linesep)
        filehtml.write("            </tr>\n" + linesep)
    filehtml.write(" </table>\n" + "</body>\n" + "</html>" + linesep)
    filehtml.close()

    rutacss = getsource() + "/stylerep.css"
    if not path.isfile(rutacss):
        filecss = open(rutacss, "w")
        filecss.write("body{\n"
            + "    background-color: #018e61e3;\n"
            + "}\n"
            + "h1{\n"
            + "    color: white;\n"
            + "    background-color: #DBA409;\n"
            + "    font-size: 50pt;\n"
            + "    display: block;\n"
            + "    text-align: center;\n"
            + "}\n"
            + "table{\n"
            + "    margin: 0 auto;\n"
            + "    background-color: rgba(0, 0, 0, 0.651);\n"
            + "}\n"
            + "tbody{\n"
            + "    color: white;\n"
            + "    font-size: 18px;\n"
            + "    border: darkred 2px solid;\n"
            + "    border-collapse: collapse;\n"
            + "    margin: 0px 0px;\n"
            + "}\n"
            + "td{\n"
            + "    padding: 10px;\n"
            + "    text-align: center;\n"
            + "    border: darkred 2px solid;\n"
            + "}\n"
            + "th{\n"
            + "    text-align: center;\n"
            + "    border: darkred 2px solid;\n"
            + "}")
        filecss.close()
    print("\n ----------- Reporte generado ---------- ")

    sleep(1)
    openhtml(rutahtml)