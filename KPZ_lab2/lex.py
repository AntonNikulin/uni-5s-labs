"""
Lexical analyser
variant 7
define head of the function
"""

import collections
import re


def tokenize(stream):
    Token = collections.namedtuple('Token', ['typ', 'value'])

    tokenSpec = [
        ('KeyWord', r'def|:'),
        ('Text', r'[a-zA-Z_][a-zA-Z0-9_]*'),
        ('LBrace', r'[(]'),
        ('RBrace', r'[)]'),
        # Skip over spaces and tabs
        ('SKIP', r'[ ]'),
    ]

    tokenRegex = '|'.join('(?P<%s>%s)' % pair for pair in tokenSpec)
    keywords = {
        ':': 'Function Start',
        'def': 'Define Function'
    }

    nextToken = re.compile(tokenRegex).match

    # Fetch the first token ...
    token = nextToken(stream)
    #True when inside parenthesis
    param = False

    # ... and start the processing.
    while token is not None:
        # Fetch the token type
        typ = token.lastgroup
        # Fetch the token value
        if typ != 'SKIP':

            value = token.group(typ)    #get value of token
            if typ == 'LBrace':
                param = True

            if typ == 'RBrace':
                param = False

            if typ == 'Text' and param:
                typ = 'Function parameter'

            if typ == 'Text':
                typ = 'Function Name'

            if typ == 'KeyWord' and value in keywords.keys():
                typ = keywords[value]


            print Token(typ, value)

        pos = token.end()
        token = nextToken(stream, pos)
        #if pos != len(stream):
        #raise


form = "def _Test ( param1 param2):"

tokenize(form)


