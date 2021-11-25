import ply.lex as lex
import codecs
import os


reservadas = [
    'PROGRAM', 'program',
    'ID', 'id',
    'INT', 'int',
    'FLOAT', 'float',
    'CHAR', 'char',
    'FUNCTION','function',
    'IF', 'if',
    'THEN','then'
    'ELSE', 'else',
    'READ', 'read',
    'VOID', 'void',
    'RETURN', 'return',
    'FOR', 'for',
    'TO','to',
    'WHILE', 'while',
    'DO','do',
    'SUM','sum',
    'LEN', 'len',
    'AVG', 'avg',
    'MIN', 'min',
    'MAX', 'max'

]
tokens = [

    # ; { } , = ( ) [ ]
    'SEMICOLON', 'L_BRACE', 'R_BRACE',
    'COMMA', 'ASSIGN', 'L_PARENTHESIS', 'R_PARENTHESIS',
    'L_BRACKET', 'R_BRACKET',

    # operators + - * /
    'PLUS', 'MINUS', 'MULT', 'DIV',

    # bool > < != == && ||
    'GREATER_THAN', 'LESS_THAN', 'DIFF_THAN',
    'EQUALS_TO', 'AND', 'OR',

    # Constants
    'VAR', 'CONST_INT', 'CONST_FLOAT', 'CONST_CHAR', 'LETREROS',
]

tokens = tokens + reservadas

t_ignore = '\t\n'
t_ignore_space = '\s'

t_SEMICOLON = r';'
t_L_BRACE = r'\['
t_R_BRACE = r'\]'
t_COMMA = r','
t_ASSIGN = r'='
t_L_PARENTHESIS = r'\('
t_R_PARENTHESIS = r'\)'
t_L_BRACKET = r'\{'
t_R_BRACKET = r'\}'

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_DIV = r'/'

t_GREATER_THAN = r'\>'
t_LESS_THAN = r'\<'
t_DIFF_THAN = r'\!='
t_EQUALS_TO = r'=='
t_AND = r'&&'
t_OR = r'\|\|'

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_CONST_FLOAT(t):
    r'([0-9]*[.])+[0-9]+'
    t.value = float(t.value)
    return t

def t_CONST_INT(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_CONST_CHAR(t):
    r'[a-zA-Z_0-9]'
    t.value = chr(t.value)
    return t

def t_error(t):
    print("caracter ilegal", t.value[0])
    t.lexer.skip(1)

def t_LETREROS(t):
    r'"[a-zA-Z_][a-zA-Z0-9_]*"'
    return t

# def buscarFicheros(directorio):
#     ficheros = []
#     numArchivo = ''
#     respuesta = False
#     cont = 1
#
#     for base, dirs, files in os.walk(directorio):
#         ficheros.append(files)
#
#     for file in files:
#         print(str(cont) + ". " + file)
#         cont = cont + 1
#
#     while respuesta == False:
#         numArchivo = input('\nNumero del test: ')
#         for file in files:
#             if file == files[int(numArchivo) - 1]:
#                 respuesta = True
#             break
#
#     print("Has escogido \"%s\" \n" % files[int(numArchivo) - 1])
#
#     return files[int(numArchivo) - 1]
#
#
# directorio = 'C:\\Users\\Gera\\Documents\\Universidad\\ITC7\\test\\test\\'
# archivo = buscarFicheros(directorio)
# test = directorio + archivo
# fp = codecs.open(test, "r", "utf-8")
# cadena = fp.read()
# fp.close()

analizador = lex.lex()

# analizador.input(cadena)
#
# while True:
#     tok = analizador.token()
#     if not tok: break
#     print(tok)
