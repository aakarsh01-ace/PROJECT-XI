import ply.lex as lex

# list of tokens
tokens = [
    'NUMBERS', 'IDENTIFIER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBEACE', 'SEMICOLON', 'GT', 'LT'
]

# Reserved keywords
reserved = {
    'int' : 'INT',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'print' : 'PRINT',
}

#Token regex definitions
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'('
r_RPAREN = r')'
r_LBRACE = r'{'
r_RBRACE = r'}'
r_SEMICOLON = r';'
r_GT = r'>'
r_RT = r'<'

# Num token
def t_NUMBERS(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Identifier token (Variable names)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER') # reserved words check <-
    return t

# ignoring any tab and/or white spaces
t_ignore = ' \t'

# New line handling
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# handling error
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)
    
# Building the LEXER
lexer = lex.lex()