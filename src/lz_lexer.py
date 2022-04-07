#!/usr/bin/env python

"""
Lexer for the LayZ language.
"""

__author__ = 'Jeremy Stevens'
__version__ = '0.1'
__email__ = 'jeremiahstevens@gmail.com'
__status__ = 'Development'
__copyright__ = "(c) 2022 - Jeremy Stevens"

import ply.lex as lex


class LZ_Lexer(object):
    def build(self):
        self.lexer = lex.lex(object=self)

    def input(self, text):
        self.lexer.input(text)

    def token(self):
        self.last_token = self.lexer.token()
        return self.last_token
    # for debugging
    def test(self, text):
        self.input(text)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)

    tokens = (
        # TRUE FALSE
        'TRUE', 'FALSE',
        # get error on line number
        'LINE_NUMBER',
        # import statements
        'IMPORT',

        # functions declarations
        'FUNCTION',
        # function call
        'CALL',
        # function arguments
        'ARGUMENTS',

        # classes and objects
        'CLASS',
        'OBJECT',
        'EXTENDS',
        'NEW',
        'THIS',
        'SUPER',
        'INSTANCE',
        'STATIC',
        'INHERITANCE',
        'OVERRIDE',
        'OVERLOAD',
        'ABSTRACT',
        'PRIVATE',
        'PROTECTED',
        'PUBLIC',


        # variables
        'VAR',
        'INT', 'STRING', 'INTEGER', 'DOUBLE', 'BOOLEAN', 'CHAR', 'FLOAT',

        # keyword assertions test
        'ASSERT','TEST',

        # input and output
        'INPUT', 'OUTPUT',

        # println
        'PRINTLN',
         # variable types

        # flow control
        'IF', 'THEN', 'ELSE', 'ENDIF',
        'WHILE', 'DO','RETURN', 'ENDWHILE',
        'FOR', 'TO', 'NEXT', 'PASS'

        # constants
        'NUll',
        'INT_CONST', 'DOUBLE_CONST', 'STRING_CONST',
        'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 'PERCENT',

        # operators and delimiters
        'FLOORDIV', 'MOD','AND','OR', 'NOT',

        # keywords
        'COMMA', 'NEWLINE',
        'LPAREN', 'RPAREN',
        'LBRACKET', 'RBRACKET',
        'LESS_THAN', 'LESS_EQUAL',
        'GREATER_THAN', 'GREATER_EQUAL',
        'EQUALITY', 'NOT_EQUALITY',
        "PRINT",
        "ECHO",
    )
    reserved = r''.join(["(?!" + keyword + ")" for keyword in tokens])

    # mathematical operators
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_EQUALS = r'='
    t_PERCENT = r'%'
    t_FLOORDIV = r'//'
    t_MOD = r'%'

    # comparison operators
    t_AND = r'&'
    t_OR = r'\|'
    t_LESS_THAN = r'<'
    t_LESS_EQUAL = r'<='
    t_GREATER_THAN = r'>'
    t_GREATER_EQUAL = r'>='
    t_EQUALITY = r'=='
    t_NOT_EQUALITY = r'<>'

    # delimiters
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_COMMA = r'\,'


    # class and object
    t_CLASS = r'CLASS'
    t_OBJECT = r'object'
    t_NEW = r'new'
    t_THIS = r'this'
    t_SUPER = r'super'
    t_INSTANCE = r'instance'
    t_STATIC = r'static'
    t_INHERITANCE = r'inheritance'
    t_OVERRIDE = r'override'
    t_OVERLOAD = r'overload'
    t_ABSTRACT = r'abstract'
    t_PRIVATE = r'PRIVATE'
    t_PROTECTED = r'protected'
    t_PUBLIC = r'public'

    # assert
    t_ASSERT = r'assert'
    t_TEST = r'test'
    t_RETURN = r'RETURN'

    # functions
    t_FUNCTION = r'function'
    t_CALL = r'call'
    t_ARGUMENTS = r'arguments'

    # import statements
    t_IMPORT = r'import'
    t_INT = 'INT'
    t_DOUBLE = 'DOUBLE'

    # variable types
    t_STRING = 'STRING'
    t_INTEGER = 'INTEGER'
    t_BOOLEAN = 'BOOLEAN'
    t_CHAR = 'CHAR'
    t_FLOAT = 'FLOAT'

    # input and output
    t_INPUT = 'INPUT'
    t_OUTPUT = 'OUTPUT'
    t_PRINT = 'PRINT'
    t_ECHO = 'ECHO'

    # println
    t_PRINTLN = 'PRINTLN'

    # flow control
    t_TRUE = r'TRUE'
    t_FALSE = r'FALSE'
    t_IF = 'IF'
    t_THEN = 'THEN'
    t_ELSE = 'ELSE'
    t_ENDIF = 'ENDIF'
    t_WHILE = 'WHILE'
    t_DO = 'DO'
    t_ENDWHILE = 'ENDWHILE'
    t_FOR = 'FOR'
    t_TO = 'TO'
    t_NEXT = 'NEXT'
    t_VAR = reserved + r'[a-zA-Z_][a-zA-Z0-9_]*'
    t_ignore = " \t"


    # line number
    def t_LINE_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_DOUBLE_CONST(self, t):
        r'\d+\.\d*'
        t.value = float(t.value)
        return t
    def t_INT_CONST(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_STRING_CONST(self, t):
        r'".*?"'
        t.value = t.value[1:len(t.value) - 1]
        return t

    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")
        return t

    def t_error(self, t):
        print(f"Illegal character {t.value[0]!r}")
        t.lexer.skip(1)


if __name__ == "__main__":
    m = LZ_Lexer()
    m.build()
    m.test("x = 2 + 2")
    # println
    m.test("print(\"hello world\")")
    # test
    m.test("assert(x == 2)")
    # line number
    m.test("x = 2 + 2")
    # variabl




