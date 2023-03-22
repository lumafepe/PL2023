import ply.lex as lex

# Definir os tokens
import ply.lex as lex

tokens = [
    'COMMENT',
    'INT',
    'FUNCTION',
    'PROGRAM',
    'IDENTIFIER',
    'LBRACE',
    'RBRACE',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'SEMICOLON',
    'ASSIGN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MODULO',
    'LESSTHAN',
    'GREATERTHAN',
    'EQUAL',
    'NOTEQUAL',
    'LESSEQUAL',
    'GREATEREQUAL',
    'LISTGENERATOR',
    'NUMBER',
    'PRINT',
    'FOR',
    'WHILE',
]

# Define as expressões regulares para cada token
t_COMMENT = r'/\*(\n|.)*\*/|//.*'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_SEMICOLON = r';'
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_EQUAL = r'=='
t_NOTEQUAL = r'!='
t_LESSEQUAL = r'<='
t_GREATEREQUAL = r'>='
t_LISTGENERATOR = r'\.\.'
t_NUMBER = r'\d+'
t_INT = r'int(.......................................){0}'
t_FUNCTION = r'function\s\w+\(.*\)(.......................................){0}'
t_PROGRAM = r'program\s\w+(.......................................){0}'
t_PRINT = r'print\(.*\)'
t_FOR = r'for'
t_WHILE = r'while'
t_IDENTIFIER = r'(?u)[a-zA-Z_][a-zA-Z0-9_]*'


t_ignore = ' \t\n'

def t_error(t):
    print(f"Token inválido: {t.value[0]!r}")
    t.lexer.skip(1)

# Criar o analisador léxico
lexer = lex.lex()


data = '''
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/

int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};

// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)