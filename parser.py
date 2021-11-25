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


def p_program(p):
    """
program : vars  programA
    | programA
"""
    print("program")


def p_programA(p):
    """
programA : function programC
         | main
"""
    print("program")

# declaracion de variales lista


def p_vars(p):
    """
vars : VARS L_BRACE varsB R_BRACE
"""

# declaracion de variables sencilla y llamada a multiple


def p_varsB(p):
    """
varsB : type  varsC SEMICOLON
      | type  varsC SEMICOLON varsB
"""

# delcaracion de llamada multiple


def p_varsC(p):
    """
varsC : var
      | var COMMA varsC
"""


def p_function(p):
    """
function : FUNCTION func_type ID L_PARENTHESISENTHESISENTHESIS functionB R_PARENTHESIS  block
"""


def p_functionB(p):
    """
functionB : params
      | empty
"""


def p_main(p):
    """
main : MAIN np_set_curr_proc np_GOTO_END L_PARENTHESISENTHESIS R_PARENTHESIS block
"""


def p_type(p):
    """
type : INT
      | FLOAT
      | BOOL
      | CHAR
      | STRING
"""


def p_var(p):
    """
var : ID L_BRACKET CTE_INT R_BRACKET
    | ID
"""


def p_vector(p):
    """
vector : ID L_BRACKET CONST_INT R_BRACKET
"""


def p_func_type(p):
    """
func_type : VOID
          | type
"""


def p_block(p):
    """
block : L_BRACE block2 block3 R_BRACE

block2 : vars
        | empty

block3 : empty
       | statement block3
"""


def p_params(p):
    """
params : param2
       | param2 COMMA params

param2 : type var
"""


def p_statement(p):
    """
statement : assign
       | condicional
       | read
       | write
       | loop_cond
       | loop_range
       | return
       | func_call
"""


def p_assign(p):
    """
assign : var oper_assign  expression SEMICOLON
"""


def p_special_func(p):
    """
special_func : LENGTH L_PARENTHESISENTHESIS vector R_PARENTHESIS
        | MIN L_PARENTHESISENTHESIS vector R_PARENTHESIS
        | MAX L_PARENTHESISENTHESIS vector R_PARENTHESIS
        | AVG L_PARENTHESISENTHESIS vector R_PARENTHESIS
        | MODA L_PARENTHESISENTHESIS vector R_PARENTHESIS
        | VARIANCE L_PARENTHESISENTHESIS vector R_PARENTHESIS
        | SUM L_PARENTHESIS vector R_PARENTHESIS
"""


def p_condicional(p):
    """
condicional : IF L_PARENTHESIS expression  R_PARENTHESIS THEN block cond2

cond2 : ELSE block
      | empty
"""


def p_read(p):
    """
read : READ L_PARENTHESIS read2 R_PARENTHESIS SEMICOLON

read2 : var
      | var COMMA read2
"""


def p_write(p):
    """
write : WRITE L_PARENTHESIS write2 R_PARENTHESIS SEMICOLON

write2 : expression write3
       | letrero write3

write3 : COMMA write2
       | empty
"""


def p_while_loop(p):
    """
loop_cond : WHILE L_PARENTHESIS expression R_PARENTHESIS DO block
"""


def p_for_loop(p):
    """
loop_range : FOR var EQUAL exp TO exp DO block
"""


def p_return(p):
    """
return : RETURN L_PARENTHESIS exp R_PARENTHESIS SEMICOLON
"""


def p_func_call(p):
    """
func_call : ID L_PARENTHESIS func_callB R_PARENTHESIS

func_callB : exp
      | COMMA exp func_callB
      | empty
"""


def p_expression(p):
    """
expression : not logic expression2

expression2 : OR expression
      | AND expression
      | empty
"""


def p_logic(p):
    """
logic : exp logic2

logic2 : LESS_THAN exp
     | GREATER_THAN  exp
     | LESS_THAN  exp
     | EQUALS_TO  exp
     | DIFF_THAN   exp
     | empty
"""


def p_exp(p):
    """
exp : term exp2

exp2 : PLUS exp
     | MINUS  exp
     | empty
"""


def p_term(p):
    """
term : factor term2

term2 : MULT  term
      | DIV  term
      | empty
"""


def p_factor(p):
    """
factor : exponent factorB

factorB : EXP factor
        | empty
"""


def p_exponent(p):
    """
exponent : L_PARENTHESIS expression R_PARENTHESIS
    | exponent2

exponent2 : PLUS var_cte
    | MINUS var_cte
    | var_cte
"""


def p_var_cte(p):
    """
var_cte : var
     | CONST_INT
     | CONST_FLOAT
     | CONST_CHAR
     | LETRERO
"""


def p_error(p):
    print("Syntax error found at line {0} around '{1}'", p)


def p_empty(p):
    """
empty :
"""


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
