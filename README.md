
GRAMATICA UTILIZADA

    S0 -> let S1
        | var S1
        | const S1
        | if S5
        | while S5
        | switch S7
        | foreach ( idvar in idvar ) { S0 } S0
        | idvar ( S10 ) ; S0
        | epsilon----


    S1 -> idvar = S2

    S2 -> cadena ; S0
        | numero ; S0
        | booleano ; S0
        | ( S3 ) => { S0 } S0

    S3 -> idvar S4
        | epsilon

    S4 -> , idvar S4
        | epsilon

    S5 -> ( S6 ) { S0 } S0

    S6 -> idvar
        | booleano

    S7 -> ( idvar ) { S8 } S0

    S8 -> case S13 : S0 S9
        | default : S0 S9
        | epsilon

    S9 -> case S13 : S0 S9
        | break ; S8
        | epsilon

    S10->  cadena S11
        | numero S11
        | booleano S11
        | idvar S11
        | epsilon

    S11-> , S12
        | epsilon

    S12->  cadena S11
        | numero S11
        | booleano S11
        | idvar S11

    S13->  cadena
        | numero
        | booleano
    */