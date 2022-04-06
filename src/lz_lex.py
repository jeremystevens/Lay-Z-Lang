#!/usr/bin/env python

"""
Lexer for the Lay-Z Language.
"""

__author__ = 'Jeremy Stevens'
__version__ = '0.1'  # 0.1 initial release
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

    # List of token names.   This is always required
    tokens = (
        # variables
        'VAR', 'NUM', 'STR', 'BOOL', 'LIST', 'DICT', 'FUNC',

        # classes and objects
        'CLASS', 'OBJECT', 'INSTANCE', 'STATIC', 'PRIVATE', 'PUBLIC', 'PROTECTED',

        # operators
        'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 'PERCENT', 'FLOORDIV', 'MOD', 'AND', 'OR', 'NOT',
        'NOT_EQUALS',
        'LESS_THAN', 'GREATER_THAN', 'LESS_THAN_EQUAL', 'GREATER_THAN_EQUAL',
        'NOT_IN', 'IS', 'IS_NOT', 'IN_LIST',

        # delimiters
        'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'LBRACE', 'RBRACE',

        # INPUT & PRINT
        'INPUT_NUM', 'INPUT_STR', 'INPUT_BOOL', 'INPUT_LIST', 'INPUT_DICT', 'INPUT_FUNC',
        'INPUT', 'PRINT',
        'PRINTLN', 'PRINT_LIST',
        'PRINT_DICT', 'PRINT_FUNC',

        # keywords
        'IF', 'ELSE', 'ELIF', 'WHILE', 'FOR', 'IN', 'BREAK', 'CONTINUE', 'PASS', 'DEF', 'RETURN', 'IMPORT', 'FROM',
        'AS', 'TRUE', 'FALSE', 'NONE', 'EXCEPT', 'TRY', 'WITH', 'COMMENT',

        # literals
        'STRING', 'NUMBER', 'NAME',
        # end of file
        'EOF',
    )
    reserved = r''.join(["(?!" + keyword + ")" for keyword in tokens])

    # operators
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_EQUALS = r'='
    t_PERCENT = r'%'
    t_FLOORDIV = r'//'
    t_MOD = r'%'
    t_AND = r'&'
    t_OR = r'\|'
    t_LESS_THAN = r'<'
    t_LESS_EQUAL = r'<='
    t_GREATER_THAN = r'>'
    t_GREATER_EQUAL = r'>='
    t_EQUALITY = r'=='
    t_NOT_EQUALITY = r'<>'

    # functions and classes
    t_FUNC = r'\$'
    t_CLASS = r'\@'
    t_OBJECT = r'\#'
    t_INSTANCE = r'\$'
    t_STATIC = r'\@'
    t_PRIVATE = r'\$'
    t_PUBLIC = r'\@'
    t_PROTECTED = r'\#'

    # input and print
    t_INPUT = 'INPUT'
    t_PRINT = 'PRINT'

    # delimiters
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_COMMA = r'\,'
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'

    # literals
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

    # define comment
    def t_COMMENT(self, t):
        r'\#.*'
        pass

    def t_error(self, t):
        print(f"Illegal character {t.value[0]!r}")
        t.lexer.skip(1)


if __name__ == "__main__":
    m = LZ_Lexer()
    m.build()
    # function test
    m.test(2 + 2)
