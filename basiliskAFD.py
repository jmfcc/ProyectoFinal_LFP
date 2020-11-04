tksimp = ["(",")","{","}",",",":",";", "=", ">"]
tkcomp = ["let","var","const","if","while","switch","foreach","in","case","default","break"]
tkdef = ["cadena"]
tknoreserv = ["numero","booleano","idvar"]

infoTkns = {
    "let":["tk_let","Indica que se definirá una variable"],
    "var":["tk_var","Indica que se definirá una variable"],
    "const":["tk_const","Indica que se definirá una variable"],
    "if":["tk_if","Indica una instrucción de control"],
    "while":["tk_while","Indica una instrucción de ciclo"],
    "switch":["tk_switch","Indica una sentencia de control por casos"],
    "foreach":["tk_foreach","Indica una instrucción de ciclo"],
    "in":["tk_in","Es parte de la instrucción foreach que indica una contencion de los datos en una variable"],
    "case":["tk_case","Es parte de la instrucción switch, que indica las distintas opciones dentro del switch"],
    "default":["tk_default","Es parte de la instrucción switch, que indica la opción por defecto si ninguno de los case es valida"],
    "break":["tk_break","Es parte de la instrucción switch, puede o no estar contenida dentro de las instrucciones de un case o default"],
    "numero":["tk_numero","Indica que el token leído es de tipo numerico"],
    "booleano":["tk_bool","Indica que el token leído es de tipo booleano (True/False)"],
    "idvar":["tk_idvar","Indica que el token cumple con las condiciones para un identificador"],
    "comment":["tk_comment","Es un conjunto de caracteres que no es tomado en cuenta como linea de codigo"],
    "cadena":["tk_str","Es un texto que si es tomado en cuenta como valor para asignar a una variable o como valor al llamar una función"],
    "(":["tk_parentesisApertura","Apertura del parentesís para contener parametros"],
    ")":["tk_parentesisCierre","Cierre del parentesís, indica que finaliza la lista de parametros"],
    "{":["tk_llavesApertura","Indican la apertura del contenido o cuerpo de una funcion o sentencia de control"],
    "}":["tk_llavesCierre","Indican el cierre del contenido o cuerpo de una funcion o sentencia de control"],
    ",":["tk_comma","Indica la separación de elementos"],
    ":":["tk_dospuntos","Indican que puede venir varias instrucciones"],
    ";":["tk_puntoycoma","Indica y delimita que es el final de una linea de codigo"],
    "=":["tk_eqls","Indica la asignación o combinada puede definir una funcion"],
    "=>":["tk_flecha","Indica que se creará el cuerpo de una función"],
}

def getDescrpTkn(tkn):
    try:
        return infoTkns[tkn]
    except:
        return ["None","None"]