import ply.yacc as yacc
import os
import codecs
import re
from lexico import tokens, analizador
from sys import stdin

precedence = (
    ('left', 'ASSIGN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIP', 'DIVIDE'),
    ('left', 'L_PARENTHESISENTHESIS', 'R_PARENTHESIS')
)


quads = []
dirVar = {}
memo = memoria()
tabla = TablaVars()
numInt = 500
numIntT = 600
numFloat = 750
numFloatT = 850
numchar = 900
numcharT = 1000
numTxt = 1100
numtxtT = 1200
pointT = 1300
n = 0
psaltos = []


def t_program(t):

    if len(t) == 2 and t[1]:
        t[0] = {}
        line, stat = t[1]
        t[0][line] = stat
    elif len(t) == 3:
        t[0] = t[1]
        if not t[0]:
            t[0] = {}
        if t[2]:
            line, stat = t[2]
            t[0][line] = stat


def p_program_error(t):
    '''program : error'''
    t[0] = None
    t.parser.error = 1


def p_program(t):
    print(quads)


def t_vars(t):
    global numInt, numFloat, numTxt
    if t[1] == 'INT':
        tabla.addVar(t[1], t[2], numInt)
        memo.enteros.append(numInt)
        numInt += 1
    elif t[1] == 'FLOAT':
        tabla.addVar(t[1], t[2], numFloat)
        memo.flotantes.append(numFloat)
        numFloat += 1
    else:
        tabla.addVar(t[1], t[2], numTxt)
        memo.text.append(numTxt)
        numTxt += 1


def t_varst(t):
    global numIntT, numFloatT, numtxtT
    if t[1] == 'INT':
        tabla.addVar(t[1], t[2], numIntT)
        memo.ent_temp.append(numIntT)
        numIntT += 1
    elif t[1] == 'FLOAT':
        tabla.addVar(t[1], t[2], numFloatT)
        memo.flot_temp.append(numFloatT)
        numFloatT += 1
    else:
        tabla.addVar(t[1], t[2], numtxtT)
        memo.text_temp.append(numtxtT)
        numtxtT += 1


def t_tipo(t):
    t[0] = t[1]
    pass


def t_asignacion(t):
    global quads
    quads = quads + [(memo.constantes[33], t[3], t[1])]
    pass


def t_lectura(t):
    global quads
    quads = quads + [(memo.especiales[4], t[3], t[1])]
    pass


def t_exp(t):
    global numIntT, quads
    if(len(t) == 2):
        t[0] = t[1]
    elif(t[2] == "&&"):
        numIntT += 1
        memo.ent_temp.append(numIntT)
        quads = quads + [(memo.especiales[5], t[1], t[3], numIntT)]
        t[0] = numIntT
    else:
        # ||
        numIntT += 1
        memo.ent_temp.append(numIntT)
        quads = quads + [(memo.especiales[6], t[1], t[3], numIntT)]
        t[0] = numIntT


def t_exOp(t):
    global numIntT, quads
    if(len(t) == 2):
        t[0] = t[1]
    elif(t[2] == "<"):
        numIntT += 1
        memo.ent_temp.append(numIntT)
        quads = quads + [(memo.especiales[7], t[1], t[3], numIntT)]
        t[0] = numIntT
    elif(t[2] == ">"):
        numIntT += 1
        memo.ent_temp.append(numIntT)
        quads = quads + [(memo.especiales[8], t[1], t[3], numIntT)]
        t[0] = numIntT
    elif(t[2] == "=="):
        numIntT += 1
        memo.ent_temp.append(numIntT)
        quads = quads + [(memo.especiales[9], t[1], t[3], numIntT)]
        t[0] = numIntT
    else:
        #!=
        numIntT += 1
        memo.ent_temp.append(numIntT)
        quads = quads + [(memo.especiales[10], t[1], t[3], numIntT)]
        t[0] = numIntT


def t_exOp(t):
    global numIntT, quads
    if(len(t) == 2):
        t[0] = t[1]
    elif(t[2] == "*"):
        numIntT += 1
        memo.ent_temp.append(numIntT)
        quads = quads + [(memo.especiales[40], t[1], t[3], numIntT)]
        t[0] = numIntT
    elif(t[2] == "/"):
        numIntT += 1
        memo.ent_temp.append(numIntT)
        quads = quads + [(memo.especiales[41], t[1], t[3], numIntT)]
        t[0] = numIntT
    elif(t[2] == "+"):
        numIntT += 1
        memo.ent_temp.append(numIntT)
        quads = quads + [(memo.especiales[42], t[1], t[3], numIntT)]
        t[0] = numIntT
    else:
        # -
        numIntT += 1
        memo.ent_temp.append(numIntT)
        quads = quads + [(memo.especiales[43], t[1], t[3], numIntT)]
        t[0] = numIntT


# Build the parser
parser = yacc.yacc()


def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print(str(cont) + ". " + file)
        cont = cont+1

    while respuesta == False:
        numArchivo = input('\nNumero del test: ')
        for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta = True
                break

    print("Has escogido \"%s\" \n" % files[int(numArchivo) - 1])

    return files[int(numArchivo)-1]


directorio = 'C:\\Users\\Gera\\Documents\\Universidad\\ITC7\\entrega\\compilador'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)

print(result)
