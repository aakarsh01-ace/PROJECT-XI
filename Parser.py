# the parser buils an ABSTRACT SYNTAX TREE OR AAST based on the grammar rules of language
import ply.yacc as yacc

from Lexer import tokens

def p_prog(p):
    '''program : statement_lst'''
    p[0] = ('program', p[1])
   
    
def p_statement_lst(p):
    '''statement_list : statement
                      | statement_list element'''
    
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]
      
        
def p_statement(p):
    '''statement : declr
                 | assignment 
                 | print_stmt 
                 | if_stmt 
                 | while_stmt'''
    p[0] = p[1]
    
    
def p_declr(p):
    '''declaration : INT IDENTIFIER EQUALS expression SEMICOLON'''
    p[0] = ('declare', p[2], p[4])
    
    
def p_expr(p):
    '''expression : term 
                  | term PLUS term 
                  | term MINUS term'''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '+':
        p[0] = ('+', p[1], p[3])
    elif p[2] == '-':
        p[0] = ('-', p[1], p[3])
      
        
def p_term(p):
    '''term : factor 
            | factor TIMES factor 
            | factor DIVIDE factor'''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '*':
        p[0] = ('*', p[1], p[3])
    elif p[2] == '/':
        p[0] = ('/', p[1], p[3])


def p_factor(p):
    '''factor : NUMBER 
              | INDETIFIER 
              | LPAREN expression RPAREN'''
    if isinstance(p[1], int):
        p[0] = p[1]
    elif isinstance(p[1], str):
        p[0] = p[1]
    else:
        p[0] = p[2]
        
        
def p_prnt_statement(p):
    '''print_stmt : PRINT LPAREN expression RPAREN SEMICOLON'''
    p[0] = ('print', p[3])
    
    
def p_if_statement(p):
    '''if_stmt : IF LPAREN expression RPAREN LBRACE statement_lst RBRACE'''
    p[0] = ('if', p[3], p[6])


def p_while_statement(p):
    '''while_stmt : WHILE LPAREN expression RPAREN LBRACE statement_lst RBRACE'''
    p[0] = ('while', p[3], p[6])
    
    
def p_error(p):
    print(f"Syntax error at '{p.value}'")
    
    
# Parser Building
parser = yacc.yacc()