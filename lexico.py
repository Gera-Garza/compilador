import ply.lex as lex

reservadas = {
    'PROGRAM': 'program',
    'ID': 'id',
    'INT': 'int',
    'FLOAT': 'float',
    'CHAR': 'char',
    'IF': 'if',
    'ELSE': 'else',
    'READ': 'read',
    'VOID': 'void',
    'RETURN': 'return',
    'FOR': 'for',
    'WHILE': 'while',
    'AVG': 'avg',
    'MEDIAN': 'median',
    'MODE': 'mode',
    'MAX': 'max',
    'MIN': 'min',
    'STDEV': 'stdev',
    'HIST': 'hist',
    'COLOR': 'color',
    'BINS': 'bins',
    'EDGECOLOR': 'edgecolor',
    'PLT': 'plt',
    'XLABEL': 'xlabel',
    'YLABEL': 'ylabel',
    'TITLE': 'title',
    'SHOW': 'show',
    'BEGIN': 'begin',
    'ENDFUN': 'endfun',
    'LETREROS': 'letreros'
}
tokens = [

    # ; { } , = ( ) [ ]
    'SEMICOLON', 'L_BRACE', 'R_BRACE',
    'COMMA', 'ASSIGN', 'L_PARENTHESIS', 'R_PARENTHESIS',
    'L_BRACKET', 'R_BRACKET', 'BEGIN', 'ENDFUN'

    # operators + - * /
    'PLUS',	'MINUS', 'MULT', 'DIV',

    # bool > < != == && ||
    'GREATER_THAN', 'LESS_THAN', 'DIFF_THAN',
    'EQUALS_TO', 'AND', 'OR',

    # Constants
    'CONST_ID', 'CONST_INT', 'CONST_FLOAT', 'CONST_CHAR', 'LETREROS'
]

tokens = tokens+list(reservadas.values())

t_ignore = '\t\n'

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


def t_CONST_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t


def t_CONST_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_CONST_FLOAT(t):
    r'\d\.\d+'
    t.value = float(t.value)
    return t


def t_CONST_CHAR(t):
    r'[a-zA-Z_0-9]'
    t.value = chr(t.value)
    return t


def t_error(t):
    print("caracter ilegal '%s", t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
